from rest_framework import serializers, viewsets
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()

    image = serializers.SerializerMethodField()

    @staticmethod
    def get_image(obj):
        return obj.image_url


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
