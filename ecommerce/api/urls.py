from django.urls import path, include
# from api.products import products_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.products import ProductViewSet
from api.profile import profile_view

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('products/', products_view),
    path('', include(router.urls)),
    path('profile/', profile_view),
]
