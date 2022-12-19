import json
from django.shortcuts import redirect, render
from django.views import View
from cart.models import Cart

from order.models import Order
from user.models import CustomerUser

# Create your views here.


class OrderProcessView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated == False:
            return redirect('auth_login')
        customer_user = CustomerUser.objects.get(user=user)
        cart = Cart.objects.get(user=customer_user)

        return render(request, 'order_page/order-process.html', {
            'cart': cart,
            'fullname': user.first_name + ' ' + user.last_name,
            'phonenumber': customer_user.phone_number,
            'address': customer_user.address
        })

    def post(self, request):
        user = request.user
        if user.is_authenticated == False:
            return redirect('auth_login')
        customer_user = CustomerUser.objects.get(user=user)
        full_name = request.POST.get('fullname')
        phone_number = request.POST.get('phonenumber')
        address = request.POST.get('address')
        selected_item_ids = json.loads(request.POST.get('selecteditem'))
        cart_id = request.POST.get('cartid')
        cart = Cart.objects.get(id=cart_id)

        Order.objects.create(user=customer_user, cart=cart,
                             shipping_address=address)
        
        return redirect('order-success')

class OrderSuccessView(View):
  def get(self, request):
    user = request.user
    if user.is_authenticated == False:
      return redirect('auth_login')
    return render(request, 'order_page/order-success.html')