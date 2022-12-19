from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomerUser(models.Model):
    GENDER_UNKNOWN = 'Unknown'
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.user.username
