from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from product.models import ProductItem

# Create your views here.


class ProductView(View):
    def get(self, request, slug):
        products = ProductItem.objects.all()
        for product in products:
          print(product.slug)
        try:
            product_item = ProductItem.objects.get(slug=slug)
            product = product_item.getProduct()
            category = product.getCategory()
        except ObjectDoesNotExist:
            product = None

        if product is not None:
            return render(request, 'product_page/product.html', {
                'product': product_item,
                'inventory': product.inventory,
                'category': category,
            })

        return HttpResponse('product not found')
