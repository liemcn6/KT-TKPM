from cart.models import Cart
from user.models import CustomerUser


def cart_info(request):
    user = request.user
    if(user.is_authenticated == True):
        try:
            customer_user = CustomerUser.objects.get(user=user)
            cart = Cart.objects.get(user=customer_user)
            return {
                'cart_total_price': cart.get_total_price(),
                'cart_item_count': cart.get_item_count()
            }
        except CustomerUser.DoesNotExist:
            return {}
    return {}
