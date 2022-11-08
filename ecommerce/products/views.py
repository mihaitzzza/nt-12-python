import random
from django.shortcuts import render, Http404

products = [
    {
        'id': 1,
        'name': 'Product #1',
        'price': 127.00
    },
    {
        'id': 2,
        'name': 'Product #2',
        'price': 567.00
    },
    {
        'id': 3,
        'name': 'Product #3',
        'price': 15.90
    }
]


def show_all_products(request):
    return render(request, 'products/all_products.html', {
        'products': products,
        'title': random.choice([
            'My dynamic title from server!',
            'My random #1',
            'My random #2',
            'My random #3',
        ])
    })


def show_product(request, product_id):
    filtered_products = [product for product in products if product['id'] == product_id]

    if len(filtered_products) == 0:
        raise Http404('This product is not available.')

    product = filtered_products[0]

    return render(request, 'products/product.html', {
        'product': product
    })
