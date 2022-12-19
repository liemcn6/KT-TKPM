from django.shortcuts import render
from django.views import View

from cart.models import Cart

# Create your views here.

class CartView(View):
  def get(self, request):
    cart = Cart.objects.get()
    return render(request, 'cart_page/cart.html')