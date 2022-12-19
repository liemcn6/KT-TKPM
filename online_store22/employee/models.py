from django.db import models

# Create your models here.

class Item(models.Model):
  name = models.CharField(max_length=256)
  description = models.TextField()
  price = models.FloatField()
  discount = models.IntegerField()
  image = models.TextField()