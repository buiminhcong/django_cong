from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from order.models import Cart
from order.serializers import CartSerializer
from .models import ClothesItem
from .serializers import ClothesItemSerializer
from django.shortcuts import render

# Create your views here.


class ClothesItemListAPIView(APIView):

    def get(self, request):
        clothes_items = ClothesItem.objects.all()
        serializer = ClothesItemSerializer(clothes_items, many=True) # chuyen ve dang json
        # return Response(serializer.data)
        listClothesItem = serializer.data # 1 list Clothes item
        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        context = {'listClothesItem': listClothesItem,  'numberOfItems': cart['numberOfItems']}
        return render(request, 'index.html', context)

class ClothesItemDetailAPIView(APIView):

    def get(self, request, pk):
        countImg = 0
        try:
            clothes_item = ClothesItem.objects.get(pk=pk)
            countImg = clothes_item.images.count()


        except ClothesItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothesItemSerializer(clothes_item)
        #return Response(serializer.data)
        clothesItem = serializer.data

        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        array = [0, 1]
        for i in array:
            print(i)
        print(len(array))
        context = {'clothesItem': clothesItem, 'list': array,  'numberOfItems': cart['numberOfItems']}

        return render(request, 'detail.html', context)
        # return Response(serializer.data)


