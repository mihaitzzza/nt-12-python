from django import forms
from products.models import Product
from orders.models import Order, OrderProduct


class CartForm(forms.Form):
    def __init__(self, *args, session=None, **kwargs):
        if not session:
            raise ValueError('Session is not defined.')
        self._session = session

        super().__init__(*args, **kwargs)

        cart = self._session.get('cart', {})
        self._products = Product.objects.filter(id__in=cart.keys())
        for product in self._products:
            product_key = str(product.id)
            self.fields[product_key] = forms.IntegerField(
                label=product.name,
                min_value=0,
                step_size=1,
                initial=cart[product_key]
            )

    @property
    def products(self):
        return self._products

    # my_instance.products <> my_instance.products()

    def clean(self):
        print('cleaned_data', self.cleaned_data)

        for product_key, quantity in self.cleaned_data.items():
            try:
                product = Product.objects.get(id=product_key)
            except Product.DoesNotExist:
                product = None

            if not product:
                raise forms.ValidationError(f'Product with key = {product_key} is not available.')

        return self.cleaned_data

    def save(self):
        self._session['cart'] = {
            product_key: quantity
            for product_key, quantity in self.cleaned_data.items()
            if quantity >= 1
        }
        # self._session.modified = True


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('billing_address', 'shipping_address')

    def __init__(self, *args, cart=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self._cart = cart
        self._user = user

    def save(self, commit=True):
        order = super().save(commit=False)
        if self._user:
            order.user = self._user

        if commit:
            order.save()

            for product_key, quantity in self._cart.items():
                product = Product.objects.get(id=product_key)

                order_product = OrderProduct(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )
                order_product.save()

        return order
