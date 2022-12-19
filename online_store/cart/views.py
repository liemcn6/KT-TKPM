from django.shortcuts import redirect, render
from django.views import View

from cart.models import Cart, CartItem
from product.models import Item
from user.models import CustomerUser

# Create your views here.


class CartView(View):
    def get(self, request):
        user = request.user
        customer_user = CustomerUser.objects.get(user=user)
        cart = Cart.objects.get(user=customer_user)
        cart_items = CartItem.objects.all().filter(cart=cart)

        total_price = 0
        for cart_item in cart_items:
            item_info = cart_item.getItem().getItemInfo()
            total_price += item_info.sale_price * cart_item.quantity
            cart_item.item.item_info = item_info

        return render(request, 'cart_page/cart.html', {
            'cart_items': cart_items,
            'total_price': total_price
        })


class AddToCartView(View):
    def post(self, request):
        user = request.user

        if user.is_authenticated == False:
            return redirect('auth_login')

        customer_user = CustomerUser.objects.get(user=user)
        cart = Cart.objects.get(user=customer_user)
        item = Item.objects.get(reflect_id=request.POST.get('id'))
        quantity = int(request.POST.get('quantity'))

        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        if created == True:
            cart_item.quantity = quantity
        else:
            print(cart_item.quantity)
            print(request.POST.get('quantity'))
            cart_item.quantity += quantity
        cart_item.save()

        return redirect('cart')
