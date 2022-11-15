from django.db import models
from itertools import groupby


class SpecificationCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)


class Specification(models.Model):
    class Meta:
        unique_together = ('specification_category', 'name')

    specification_category = models.ForeignKey(SpecificationCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False)
    value = models.TextField(null=False)


class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=128, null=False, unique=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)  # 9999.99
    specifications = models.ManyToManyField(Specification)

    def specs_categories(self):
        grouped_specs = groupby(self.specifications.all(), key=lambda specs: specs.specification_category.name)

        # for specs_category_name, group in grouped_specs:
        #     print(specs_category_name, list(group))

        return ((specs_category_name, list(group)) for specs_category_name, group in grouped_specs)
