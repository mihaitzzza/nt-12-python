# from rest_framework.decorators import api_view
# from django.http import JsonResponse
#
#
# @api_view(['GET', 'POST'])
# def products_view(request):
#     return JsonResponse({
#         'message': f'Products resource accessed on {request.method} method.'
#     }, safe=False)

from rest_framework import serializers, viewsets
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = []
        exclude = []


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
