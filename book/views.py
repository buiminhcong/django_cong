from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Book, BookItem, Author, Category, Publisher
from order.models import Cart
from order.serializers import CartSerializer
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer, BookItemSerializer
from django.shortcuts import render

# Create your views here.


class BookItemListAPIView(APIView):

    def get(self, request):
        book_items = BookItem.objects.all()
        serializer = BookItemSerializer(book_items, many=True) # chuyen ve dang json
        # return Response(serializer.data)
        listBookItem = serializer.data # 1 list book item
        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        context = {'listBookItem': listBookItem,  'numberOfItems': cart['numberOfItems']}
        return render(request, 'index.html', context)

class BookItemDetailAPIView(APIView):

    def get(self, request, pk):
        countImg = 0
        try:
            book_item = BookItem.objects.get(pk=pk)
            countImg = book_item.images.count()


        except BookItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookItemSerializer(book_item)
        #return Response(serializer.data)
        bookItem = serializer.data

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
        context = {'bookItem': bookItem, 'list': array,  'numberOfItems': cart['numberOfItems']}

        return render(request, 'detail.html', context)
        # return Response(serializer.data)


