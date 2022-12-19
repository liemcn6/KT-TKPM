from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.CharField(default='', max_length=255)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def getCategory(self):
        return self.category


class ProductItem(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    product_img = models.CharField(max_length=510, default='')
    sale_price = models.IntegerField(default=0)
    slug = AutoSlugField(populate_from='title', default='')
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def getProduct(self):
        return self.product
