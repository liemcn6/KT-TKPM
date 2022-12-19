from django.urls import include, path
from .views import OrderProcessView, OrderSuccessView

urlpatterns = [
    # path('', CartView.as_view(), name='cart'),
    path('process/', OrderProcessView.as_view(), name='order-process'),
    path('success/', OrderSuccessView.as_view(), name='order-success')
]
