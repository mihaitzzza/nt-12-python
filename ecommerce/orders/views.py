from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product
from orders.forms import CartForm, OrderForm


def show_cart(request):
    form = CartForm(session=request.session)

    return render(request, 'orders/cart.html', {
        'form': form
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

    request.session.modified = True

    messages.add_message(request, messages.SUCCESS, f"Product {product.name} was successfully added to the cart.")

    if next_url:
        return redirect(next_url)

    return redirect(reverse('orders:cart'))


def update_cart(request):
    if request.method == 'GET':
        raise Http404('Method not allowed.')

    form = CartForm(session=request.session, data=request.POST)
    if form.is_valid():
        request.session.cart = form.save()
        request.session.modified = True

        messages.add_message(request, messages.SUCCESS, 'Cart was successfully updated.')
    else:
        messages.add_message(request, messages.ERROR, 'Something went wrong! Try again later.')

    return redirect(reverse('orders:cart'))


def checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    total_price = sum([
        product.price * cart[str(product.id)]
        for product in products
    ])

    if request.method == 'GET':
        form = OrderForm()
    else:
        print('request.user', request.user)
        cart = request.session.get('cart', {})
        user = request.user if request.user.is_authenticated else None
        form = OrderForm(data=request.POST, cart=cart, user=user)

        if form.is_valid():
            form.save()
            request.session.cart = {}
            request.session.modified = True
            return redirect(reverse('orders:pay'))

    return render(request, 'orders/checkout.html', {
        'form': form,
        'total_price': total_price
    })


def pay(request):
    return HttpResponse('Add payment data in here.')
