from django.shortcuts import render, Http404, get_object_or_404
from products.models import Product


def show_all_products(request):
    price = request.GET.get('price')

    products = Product.objects
    if price is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(price=price).all()

    # products = Product.objects
    # if price is not None:
    #     products = products.filter(price=price)
    # products = products.all()

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
