from django.shortcuts import render, Http404, get_object_or_404
from products.models import Product


def show_all_products(request):
    products = Product.objects.all()

    return render(request, 'products/all_products.html', {
        'products': products,
    })


def show_product(request, product_id):
    # product = Product.objects.get(id=product_id)
    # try:
    #     product = Product.objects.get(pk=product_id)
    # except Product.DoesNotExist:
    #     raise Http404('Product not found')
    # product = get_object_or_404(Product, id=product_id)
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product.html', {
        'product': product
    })
