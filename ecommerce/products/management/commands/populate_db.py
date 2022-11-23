import os
import json
import shutil
from django.db import transaction
from django.core.management import BaseCommand, CommandError
from django.conf import settings
from products.models import (
    Category,
    Product,
    SpecificationCategory,
    Specification
)

PRODUCTS_FOLDER = os.path.join(settings.MEDIA_ROOT, 'products')


class Command(BaseCommand):
    help = 'Populate database via JSON file.'

    def add_arguments(self, parser):
        parser.add_argument('--json_path', type=str)
        parser.add_argument('--images_path', type=str)

    def handle(self, *args, json_path=None, images_path=None, **options):
        if json_path is None:
            raise CommandError('json_path attribute is required!')

        if images_path is None:
            raise CommandError('images_path attribute is required!')

        with open(json_path) as json_file:
            input_data = json.load(json_file)

        try:
            with transaction.atomic():
                for department_data in input_data:
                    department = Category(name=department_data['title'])
                    department.save()

                    for category_data in department_data['categories']:
                        category = Category(name=category_data['title'], parent=department)
                        category.save()

                        for subcategory_data in category_data['subcategories']:
                            # subcategory = Category(name=subcategory_data['title'], parent=category)
                            # subcategory.save()
                            subcategory = Category.objects.create(name=subcategory_data['title'], parent=category)

                            for product_data in subcategory_data['products']:
                                image_name = f'{product_data["id"]}.jpg'
                                server_image_path = os.path.join(images_path, image_name)

                                if os.path.exists(server_image_path):
                                    os.makedirs(PRODUCTS_FOLDER, exist_ok=True)
                                    shutil.copy(server_image_path, os.path.join(settings.MEDIA_ROOT, 'products'))

                                    product_image_path = os.path.join('products', image_name)
                                else:
                                    product_image_path = None

                                product = Product(
                                    name=product_data['title'],
                                    price=product_data['price'],
                                    image=product_image_path,
                                    category=subcategory
                                )

                                product.save()

                                for specs_category_name, specs_category_data in product_data['specifications'].items():
                                    # try:
                                    #     specs_category = SpecificationCategory.objects.get(name=specs_category_data)
                                    # except SpecificationCategory.DoesNotExist:
                                    #     specs_category = SpecificationCategory.objects.create(
                                    #         name=specs_category_data
                                    #     )
                                    #     specs_category.save()
                                    specs_category, _ = SpecificationCategory.objects.get_or_create(
                                        name=specs_category_name
                                    )

                                    for specs_name, specs_value in specs_category_data.items():
                                        specs, _ = Specification.objects.get_or_create(
                                            name=specs_name,
                                            specification_category=specs_category,
                                            defaults={'value': specs_value}
                                        )

                                        product.specifications.add(specs)
        except Exception as e:
            raise e
