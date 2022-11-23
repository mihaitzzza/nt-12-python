import os
from django.core.management.base import BaseCommand
from products.models import Product


# /home/.../.../.../images/d976dd83-a622-418c-800f-dbb2087beac7.jpg => products/d976dd83-a622-418c-800f-dbb2087beac7.jpg
class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.filter(image__startswith='/home').all()
        for product in products:
            image_name = product.image.split('/')[-1]
            product.image = os.path.join('products', image_name)
            product.save()
