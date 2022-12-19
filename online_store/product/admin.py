from django.contrib import admin
from .models import Author, Book, BookItem, Clothes, ClothesDesign, ClothesItem, ClothesOrigin, Electronics, ElectronicsItem, ElectronicsOrigin, Item, Product, Category, ProductItem, Publisher, Shoes, ShoesDesign, ShoesItem, ShoesOrigin
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductItem)
admin.site.register(Item)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(ClothesDesign)
admin.site.register(ClothesOrigin)
admin.site.register(Clothes)
admin.site.register(ClothesItem)
admin.site.register(ShoesDesign)
admin.site.register(ShoesOrigin)
admin.site.register(Shoes)
admin.site.register(ShoesItem)
admin.site.register(ElectronicsOrigin)
admin.site.register(Electronics)
admin.site.register(ElectronicsItem)

