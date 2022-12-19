from django.db import models
from autoslug import AutoSlugField
from django.dispatch import receiver
from django.db.models.signals import post_save
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


class Item(models.Model):
    slug = models.CharField(max_length=510)
    table = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=510)


class Book(models.Model):
    name = models.CharField(max_length=255, default='')
    publishedDate = models.DateField(null=True)
    numberOfPage = models.IntegerField(default=0)
    summary = models.TextField(default='')
    inventory = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    # author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    image = models.CharField(max_length=510)
    sale_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    slug = AutoSlugField(populate_from='name', default='')
    on_sale = models.BooleanField(default=True)

    def getProduct(self):
        return self.book


class ClothesDesign(models.Model):
    material = models.CharField(max_length=255, default='')
    style = models.CharField(max_length=255, default='')
    model = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255)


class ClothesOrigin(models.Model):
    companyName = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    dateOfManufacture = models.CharField(max_length=4, default='')


class Clothes(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    inventory = models.IntegerField(default=0)
    origin = models.ForeignKey(ClothesOrigin, on_delete=models.DO_NOTHING)
    design = models.ForeignKey(ClothesDesign, on_delete=models.DO_NOTHING)

    def getOrigin(self):
        return self.origin

    def getDesign(self):
        return self.design


class ClothesItem(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    image = models.CharField(max_length=510)
    description = models.TextField(default='')
    sale_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    slug = AutoSlugField(populate_from='name', default='')
    on_sale = models.BooleanField(default=True)

    def getProduct(self):
        return self.clothes


class ShoesDesign(models.Model):
    material = models.CharField(max_length=255, default='')
    style = models.CharField(max_length=255, default='')
    model = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255)


class ShoesOrigin(models.Model):
    companyName = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    dateOfManufacture = models.CharField(max_length=4, default='')


class Shoes(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    inventory = models.IntegerField(default=0)
    origin = models.ForeignKey(ShoesOrigin, on_delete=models.DO_NOTHING)
    design = models.ForeignKey(ShoesDesign, on_delete=models.DO_NOTHING)

    def getOrigin(self):
        return self.origin

    def getDesign(self):
        return self.design


class ShoesItem(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    image = models.CharField(max_length=510)
    description = models.TextField(default='')
    sale_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    slug = AutoSlugField(populate_from='name', default='')
    on_sale = models.BooleanField(default=True)

    def getProduct(self):
        return self.shoes


class ElectronicsOrigin(models.Model):
    companyName = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    dateOfManufacture = models.CharField(max_length=4, default='')
    brand = models.CharField(max_length=255, default='')


class Electronics(models.Model):
    name = models.CharField(max_length=255, default='')
    weight = models.FloatField(default=0)
    category = models.CharField(max_length=255, default='')
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    inventory = models.IntegerField(default=0)
    origin = models.ForeignKey(ElectronicsOrigin, on_delete=models.DO_NOTHING)

    def getOrigin(self):
        return self.origin


class ElectronicsItem(models.Model):
    electronics = models.ForeignKey(Electronics, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    image = models.CharField(max_length=510)
    description = models.TextField(default='')
    sale_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    slug = AutoSlugField(populate_from='name', default='')
    on_sale = models.BooleanField(default=True)

    def getProduct(self):
        return self.electronics


@receiver(post_save, sender=Book)
def create_book_item(sender, instance, created, **kwargs):
    if created:
        bookItem = BookItem.objects.create(
            book=instance,
            name=instance.name
        )

        Item.objects.create(
            slug=bookItem.slug,
            table='book'
        )


@receiver(post_save, sender=Clothes)
def create_clothes_item(sender, instance, created, **kwargs):
    if created:
        clothes = ClothesItem.objects.create(
            clothes=instance,
            name=instance.name
        )

        Item.objects.create(
            slug=clothes.slug,
            table='clothes'
        )


@receiver(post_save, sender=Shoes)
def create_shoes_item(sender, instance, created, **kwargs):
    if created:
        shoes = ShoesItem.objects.create(
            shoes=instance,
            name=instance.name
        )

        Item.objects.create(
            slug=shoes.slug,
            table='shoes'
        )


@receiver(post_save, sender=Electronics)
def create_clothes_item(sender, instance, created, **kwargs):
    if created:
        electronics = ElectronicsItem.objects.create(
            electronics=instance,
            name=instance.name
        )

        Item.objects.create(
            slug=electronics.slug,
            table='electronics'
        )
