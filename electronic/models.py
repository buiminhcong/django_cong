from django.db import models

# Create your models here.


class Electronic(models.Model):
    productName = models.CharField(max_length=255)
    batteryCapacity = models.CharField(max_length=255)
    warrantyDuration = models.CharField(max_length=255)
    warrantyType = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    screenSize = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)


class Laptop(Electronic):
    laptopType = models.CharField(max_length=255)
    storageType = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)


class MobilePhone(Electronic):
    processorType = models.CharField(max_length=255)
    storageCapacity = models.CharField(max_length=255)
    mobileCableType = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)


class Tablet(Electronic):
    eReader = models.BooleanField(default=False)
    storageCapacity = models.CharField(max_length=255)


class ElectronicItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.CharField(max_length=255)
    header = models.CharField(max_length=1023)
    discount = models.FloatField(default=0)
    electronic = models.ForeignKey(Electronic, on_delete=models.CASCADE, related_name='electronicItem')


class ElectronicItemImage(models.Model):
    electronicItem = models.ForeignKey(ElectronicItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/images/electronic_items_images/')
    index = models.IntegerField()

