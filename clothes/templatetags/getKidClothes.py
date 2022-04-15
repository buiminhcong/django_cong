from atexit import register
from django import template

from clothes.serializers import ClothesItemSerializer, KidClothesSerializer
from ..models import Clothes, ClothesItem, KidClothes

register = template.Library()

@register.simple_tag
def get_infor_sell(pk):
    try:
        kidClothes = KidClothes.objects.get(pk=pk)
        return ClothesItem.objects.get(clothes=kidClothes)
    except Exception:
        return 'none'