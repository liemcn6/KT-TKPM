
from django.urls import include, path

from .views import AuthLoginView, AuthRegisterView, UserProfileView, logout_view

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view(), name='auth_login'),
    path('auth/register/', AuthRegisterView.as_view(), name='auth_register'),
    path('auth/logout/', logout_view, name='auth_logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile')
]
