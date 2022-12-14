from django.db import models
from django.contrib.auth import get_user_model
# from django.conf import settings
from django.templatetags.static import static
from itertools import groupby

AuthUser = get_user_model()


class SpecificationCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)


class Specification(models.Model):
    class Meta:
        unique_together = ('specification_category', 'name')

    specification_category = models.ForeignKey(SpecificationCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False)
    value = models.TextField(null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=128, null=False, unique=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='stores/', null=True, default=None, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        ordering = ('name', '-price')

    store = models.ForeignKey(Store, on_delete=models.SET_NULL, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)  # 9999.99
    specifications = models.ManyToManyField(Specification)
    image = models.ImageField(upload_to='products/', null=True, default=None)

    @property
    def image_url(self):
        if self.image:
            return self.image.url

        return static('images/product_placeholder.webp')

    def __str__(self):
        return self.name

    def specs_categories(self):
        grouped_specs = groupby(self.specifications.all(), key=lambda specs: specs.specification_category.name)

        # for specs_category_name, group in grouped_specs:
        #     print(specs_category_name, list(group))

        return ((specs_category_name, list(group)) for specs_category_name, group in grouped_specs)
