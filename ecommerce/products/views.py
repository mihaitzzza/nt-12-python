from django.shortcuts import render, Http404, get_object_or_404
from django.core.paginator import Paginator
from products.models import Product, Category


def show_all_products(request):
    page = request.GET.get('page', 1)

    products = Product.objects.all()

    paginator = Paginator(products, 16)
    paginated_products = paginator.get_page(page)

    return render(request, 'products/all_products.html', {
        'paginated_products': paginated_products,
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


def show_all_categories(request):
    page = request.GET.get('page', 1)

    cateogries = Category.objects.all()

    paginator = Paginator(cateogries, 10)
    paginated_categories = paginator.get_page(page)

    return render(request, 'products/all_categories.html', {
        'paginated_categories': paginated_categories,
    })
