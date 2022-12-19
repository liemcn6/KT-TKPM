from django.db import models

from product.models import Item
from user.models import CustomerUser

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        cart_items = CartItem.objects.all().filter(cart=self)
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.getItem().getItemInfo().sale_price * cart_item.quantity
        return total_price
    
    def get_item_count(self):
        return CartItem.objects.all().filter(cart=self).count()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def getItem(self):
      return self.item

