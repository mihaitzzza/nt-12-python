from django.urls import path, include
from django.contrib.auth.views import LoginView
from users.views import profile_view, register_view

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
]
