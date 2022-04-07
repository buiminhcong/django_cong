from django.db import models
from book.models import BookItem
from user.models import User, Address

# Create your models here.
class Cart(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

class CartBookItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='bookItems')
    bookItem = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')


class OrderBookItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    bookItem = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Payment(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    total = models.FloatField()


class Cash(Payment):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='cash')


class Credit(Payment):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='credit')
    number = models.CharField(max_length=15)
    expDate = models.DateField()

class Transfer(Payment):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='transfer')
    number = models.CharField(max_length=15)
    bankId = models.CharField(max_length=50)

class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipment')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    shippingFee = models.FloatField()





