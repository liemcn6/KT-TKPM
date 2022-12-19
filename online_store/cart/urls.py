from django.urls import include, path
from .views import AddToCartView, CartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add-item', AddToCartView.as_view(), name='add-to-cart')
]
