import json
from django.core.management import BaseCommand, CommandError
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Populate database via JSON file.'

    def add_arguments(self, parser):
        parser.add_argument('--json_path', type=str)

    def handle(self, *args, json_path=None, **options):
        if json_path is None:
            raise CommandError('json_path attribute is required!')

        with open(json_path) as json_file:
            input_data = json.load(json_file)

        for department_data in input_data:
            department = Category(name=department_data['title'])
            department.save()

            for category_data in department_data['categories']:
                category = Category(name=category_data['title'], parent=department)
                category.save()

                for subcategory_data in category_data['subcategories']:
                    subcategory = Category(name=subcategory_data['title'], parent=category)
                    subcategory.save()

                    for product_data in subcategory_data['products']:
                        product = Product(
                            name=product_data['title'],
                            price=product_data['price'],
                            category=subcategory
                        )
                        product.save()
