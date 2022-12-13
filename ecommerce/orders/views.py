from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404
from django.contrib import messages
from products.models import Product


def show_cart(request):
    cart_data = request.session.get('cart', {})
    cart_products = Product.objects.filter(id__in=cart_data.keys())

    return render(request, 'orders/cart.html', {
        'cart_products': [
            (product, cart_data[str(product.id)], product.price * cart_data[str(product.id)])
            for product in cart_products
        ],
        'total_order': 'XXX.XX RON'
    })


def add_to_cart(request, product_id):
    if request.method == 'GET':
        raise Http404('Method not allowed.')

    product = get_object_or_404(Product, pk=product_id)

    cart_product_key = str(product_id)
    next_url = request.POST.get('next')

    if 'cart' not in request.session:
        request.session['cart'] = {}

    if cart_product_key not in request.session['cart']:
        request.session['cart'][str(product_id)] = 1

    # messages.add_message(request, messages.SUCCESS, f"Product {product.name} was successfully added to the cart.")

    request.session.modified = True

    if next_url:
        return redirect(next_url)

    return redirect(reverse('orders:cart'))
