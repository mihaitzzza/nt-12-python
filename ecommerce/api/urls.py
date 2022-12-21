from django.urls import path
from django.http import JsonResponse
from api.products import products_view

urlpatterns = [
    path('products/', products_view)
]
