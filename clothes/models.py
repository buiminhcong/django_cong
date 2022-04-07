
from django.db import models




class Clothes(models.Model):
    productName = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    countryOfOrigin = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    pattern = models.CharField(max_length=255)
    plusSize = models.BooleanField(default=False)
    brand = models.CharField(max_length=255)


class KidClothes(Clothes):
    gender = models.CharField(max_length=255)
    recommendedAge = models.CharField(max_length=255)

class MaleClothes(Clothes):
    tallFit = models.BooleanField(default=False)


class MalePant(MaleClothes):
    length = models.FloatField()


class MaleShirt(MaleClothes):
    sleeveLength = models.FloatField()


class FemaleClothes(Clothes):
    petite = models.BooleanField(default=False)
    season = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)


class FemalePant(MaleClothes):
    bottomsLength = models.FloatField()
    waistHeight = models.FloatField()


class FemaleShirt(MaleClothes):
    neckline = models.CharField(max_length=255)
    croppedTop = models.BooleanField(default=False)
    topLength = models.FloatField()
    sleeveLength = models.FloatField()


class Dress(MaleClothes):
    length = models.FloatField()
    style = models.CharField(max_length=255)


class ClothesItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.CharField(max_length=255)
    header = models.CharField(max_length=1023)
    discount = models.FloatField(default=0)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)


class ClothesItemImage(models.Model):
    clothesItem = models.ForeignKey(ClothesItem, on_delete=models.CASCADE)
    image = models.CharField(max_length=1023)
    index = models.IntegerField()
