from django.urls import path
from users.views import login_view, profile_view, logout_view

urlpatterns = [
    path('login/', login_view),
    path('profile/', profile_view),
    path('logout/', logout_view),
]
