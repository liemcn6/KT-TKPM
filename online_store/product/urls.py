
from django.urls import include, path

from .views import ProductListView, ProductView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductView.as_view(), name='product_detail')
]
