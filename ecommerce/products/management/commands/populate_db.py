import json
from django.db import transaction
from django.core.management import BaseCommand, CommandError
from products.models import (
    Category,
    Product,
    SpecificationCategory,
    Specification
)


class Command(BaseCommand):
    help = 'Populate database via JSON file.'

    def add_arguments(self, parser):
        parser.add_argument('--json_path', type=str)

    def handle(self, *args, json_path=None, **options):
        if json_path is None:
            raise CommandError('json_path attribute is required!')

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
                                product = Product(
                                    name=product_data['title'],
                                    price=product_data['price'],
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

                                        # specs.
                                        product.specifications.add(specs)
        except Exception as e:
            raise e
