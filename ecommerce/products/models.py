from django.db import models


class SpecificationCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)


class Specification(models.Model):
    specification_category = models.ForeignKey(SpecificationCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False)
    value = models.CharField(max_length=128, null=False)


class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=128, null=False)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True)
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)  # 9999.99
    specifications = models.ManyToManyField(Specification)
