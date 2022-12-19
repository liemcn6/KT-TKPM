
from django.urls import include, path

from .views import ProductView

urlpatterns = [
    path('<slug:slug>/', ProductView.as_view(), name='product_detail')
]
