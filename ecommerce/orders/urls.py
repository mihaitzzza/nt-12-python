from django.urls import path
from orders.views import show_cart, add_to_cart

app_name = 'orders'

urlpatterns = [
    path('cart/', show_cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
]
