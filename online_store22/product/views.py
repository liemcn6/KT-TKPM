import math
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from product.models import BookItem, Category, ClothesItem, ElectronicsItem, Item, ShoesItem

# Create your views here.


def switchModel(x):
    return {
        'book': BookItem,
        'clothes': ClothesItem,
        'shoes': ShoesItem,
        'electronics': ElectronicsItem
    }[x]


class ProductView(View):
    def get(self, request, slug):
        try:
            item_mapping = Item.objects.get(slug=slug)
            product_item = switchModel(
                item_mapping.table).objects.get(slug=slug)
            product = product_item.getProduct()
        except ObjectDoesNotExist:
            product = None

        if product is not None:
            return render(request, 'product_page/product.html', {
                'product_item': product_item,
                'product': product,
                'category': item_mapping.table
            })

        return HttpResponse('product not found')


class ProductListView(View):
    def get(self, request):
        request_category = request.GET.get('category')
        request_page = request.GET.get('page') or 0

        if request_page != 0:
            request_page = int(request_page)

        items = None
        totalItem = 0

        if request_category == None:
            items = Item.objects.all().order_by('-id')[request_page:12]
        else:
            items = Item.objects.filter(table=request_category)[
                request_page:12]

        if(request_category != None):
            query_model = switchModel(request_category)
            totalItem = query_model.objects.count()
        else:
            totalItem = Item.objects.count()

        total_page = math.ceil(totalItem/4)
        itemInfos = []

        for item in items:
            itemInfo = switchModel(item.table).objects.get(slug=item.slug)
            itemInfo.productCategory = item.table
            itemInfos.append(itemInfo)

        return render(request, 'product_page/product-list.html', {
            'products': itemInfos,
            'prev_page': request_page - 1 if request_page-1 >= 0 else 0,
            'next_page': request_page + 1 if request_page+1 <= total_page else total_page,
            'total_page': total_page
        })
