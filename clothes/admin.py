from django.contrib import admin
from .models import Clothes, KidClothes, MaleClothes, MalePant, MaleShirt, FemaleClothes, FemalePant, FemaleShirt, Dress, ClothesItem, ClothesItemImage
# Register your models here.
admin.site.register(Clothes)
admin.site.register(KidClothes)
admin.site.register(MaleClothes)
admin.site.register(MalePant)
admin.site.register(MaleShirt)
admin.site.register(FemaleClothes)
admin.site.register(FemalePant)
admin.site.register(FemaleShirt)
admin.site.register(Dress)
admin.site.register(ClothesItem)
admin.site.register(ClothesItemImage)