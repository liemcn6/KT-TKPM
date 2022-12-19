from unicodedata import category
from django.shortcuts import render
from django.views import View

from product.models import Book, BookItem, Category, Clothes, ClothesItem, ElectronicsItem, Item, ProductItem, ShoesItem

# Create your views here.


def switchModel(x):
    return {
        'book': BookItem,
        'clothes': ClothesItem,
        'shoes': ShoesItem,
        'electronics': ElectronicsItem
    }[x]

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        items = Item.objects.all().order_by('-id')[:10]
        itemInfos = []

        for item in items:
          itemInfo = switchModel(item.table).objects.get(slug=item.slug)
          itemInfo.productCategory = item.table
          itemInfos.append(itemInfo)
        
        return render(request, 'home_page/index.html', {
          'categories': categories, 
          'products': itemInfos
        })
