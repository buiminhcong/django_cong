from django.shortcuts import render, redirect
from requests import delete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order.models import Cart
from order.serializers import CartSerializer
from clothes.models import ClothesItem, FemaleClothes, KidClothes
from clothes.serializers import ClothesItemSerializer, KidClothesSerializer

from book.models import Book, BookItem
from book.serializers import BookItemSerializer
from django.shortcuts import render

# Create your views here.


class HomeAPIView(APIView):

    def get(self, request):
        clothes_items = ClothesItem.objects.all()
        serializerClothes = ClothesItemSerializer(clothes_items, many=True) # chuyen ve dang json
        listClothesItem = serializerClothes.data # 1 list Clothes item

        book_items = BookItem.objects.all()
        serializerBook = BookItemSerializer(book_items, many=True)
        listBookItem = serializerBook.data

        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        context = {'listClothesItem': listClothesItem, 'listBookItem': listBookItem,  'numberOfItems': cart['numberOfItems']}
        return render(request, 'index.html', context)
        return Response(serializer.data)


class HomeAdminAPIView(APIView):
    def get(self, request):
        clothes_items = ClothesItem.objects.all()

        serializerClothes = ClothesItemSerializer(clothes_items, many=True) # chuyen ve dang json
        listClothesItem = serializerClothes.data # 1 list Clothes item

        book_items = BookItem.objects.all()
        serializerBook = BookItemSerializer(book_items, many=True)
        listBookItem = serializerBook.data


        kidClothes = KidClothes.objects.all()
        serializerKidClothes = KidClothesSerializer(kidClothes, many=True)
        listKidClothes = serializerKidClothes.data

        # user_id = request.session.get('user_id')
        # try:
        #     cart = Cart.objects.get(user_id=user_id)
        # except Cart.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        # cart = CartSerializer(cart).data
        context = {'listClothesItem': listClothesItem, 'listBookItem': listBookItem, 'listKidClothes':listKidClothes}
        return render(request, 'homeAdmin/homeAdmin.html', context)
        return Response(serializerBook.data)
        return Response(listClothesItem)
        return Response(serializerClothes.data)
