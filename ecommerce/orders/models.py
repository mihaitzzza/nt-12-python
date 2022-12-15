from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from products.models import Product

AuthUser = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(AuthUser, null=True, default=None, on_delete=models.SET_NULL)
    billing_address = models.CharField(max_length=128)
    shipping_address = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def total_price(self):
        total = 0

        for order_product in self.products.all():
            total += order_product.price * order_product.quantity

        return total

    def __str__(self):
        return f'<Order {self.id}>'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    def __str__(self):
        return f'<OrderProduct {self.id}>'
