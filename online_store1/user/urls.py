
from django.urls import include, path

from .views import AuthLoginView, AuthRegisterView, logout_view

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view(), name='auth_login'),
    path('auth/register/', AuthRegisterView.as_view(), name='auth_register'),
    path('auth/logout/', logout_view, name='auth_logout')
]
