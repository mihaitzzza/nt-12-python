from rest_framework.routers import DefaultRouter
from api.products import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
