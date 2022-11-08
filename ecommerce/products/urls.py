from django.urls import path
from products.views import show_all_products, show_product

# all routes below are prefixed with `products/`
urlpatterns = [
    path('', show_all_products),  # products/
    path('<int:product_id>/', show_product),  # products/<int>/
]
