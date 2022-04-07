from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass
    # lastName = models.CharField(max_length=25)
    # firstName = models.CharField(max_length=20)
    # phoneNumber = models.CharField(max_length=15)
    # photoUrl = models.ImageField(upload_to='media/images/user_photoURLs/')

class Address(models.Model):
    lastName = models.CharField(max_length=25)
    firstName = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

