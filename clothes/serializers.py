from rest_framework import serializers
from .models import Clothes, KidClothes, MaleClothes, MalePant, MaleShirt, FemaleClothes, FemalePant, FemaleShirt, Dress, ClothesItem, ClothesItemImage
from drf_writable_nested import WritableNestedModelSerializer


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['id', 'productName', 'material', 'countryOfOrigin', 'size', 'pattern', 'plusSize', 'brand']

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ['id', 'length', 'style']
class MalePantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MalePant
        fields = ['id', 'length']

class MaleShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaleShirt
        fields = ['id', 'sleeveLength']
class MaleClothesSerializer(serializers.ModelSerializer):
    clothes = ClothesSerializer()
    dress = DressSerializer()
    malePant = MalePantSerializer()
    maleShirt = MaleShirtSerializer()
    class Meta:
        model = MaleClothes
        fields = ['id', 'tallFit', 'dress', 'malePant', 'maleShirt', 'clothes']


class FemalePantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FemalePant
        fields = ['id', 'bottomsLength', 'waistHeight']
class FemaleShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = FemaleShirt
        fields = ['id', 'neckline', 'croppedTop', 'topLength', 'sleeveLength']
class FemaleClothesSerializer(serializers.ModelSerializer):
    clothes = ClothesSerializer()
    femalePant = FemalePantSerializer()
    femaleShirt = FemaleShirtSerializer()
    class Meta:
        model = FemaleClothes
        fields = ['id', 'petite', 'season', 'occasion', 'femalePant', 'femaleShirt', 'clothes']


class KidClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = KidClothes
        fields = ['id', 'gender', 'recommendedAge', 'productName', 'material', 'countryOfOrigin', 'size', 'pattern', 'plusSize', 'brand']


class ClothesItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesItemImage
        fields = ['id', 'image', 'index']

class ClothesItemSerializer(serializers.ModelSerializer):
    clothes = ClothesSerializer()
    # kidClothes = KidClothesSerializer()
    images = ClothesItemImageSerializer(many=True)
    class Meta:
        model = ClothesItem
        fields = ['id', 'prices', 'description', 'header', 'discount', 'clothes', 'images']
