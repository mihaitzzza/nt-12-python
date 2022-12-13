from django import template
from products.models import Product

register = template.Library()


@register.filter(name='total_products')
def get_total_products_from_dict(my_dict):
    return sum(my_dict.values())


@register.simple_tag(name='cart_data', takes_context=True)
def get_cart_data(context):
    cart = context.request.session.get('cart', {})
    amount = 0
    count = 0

    for product_id, product_count in cart.items():
        product = Product.objects.get(pk=product_id)
        amount += product.price * product_count
        count += product_count

    return {
        'total_amount': f'{amount:.2f} RON',
        'total_products': count
    }
