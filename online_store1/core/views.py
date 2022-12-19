from unicodedata import category
from django.shortcuts import render
from django.views import View

from product.models import Category, ProductItem

# Create your views here.


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = ProductItem.objects.all().order_by('-id')[:10]

        return render(request, 'home_page/index.html', {'categories': categories, 'products': products})
