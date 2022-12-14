from django.urls import path
from orders.views import show_cart, add_to_cart, update_cart, checkout, pay

app_name = 'orders'

urlpatterns = [
    path('cart/', show_cart, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/', update_cart, name='update_cart'),
    path('checkout/', checkout, name='checkout'),
    path('pay/', pay, name='pay'),
]
