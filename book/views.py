from tkinter import Image
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.test import RequestFactory
from regex import P
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from sqlalchemy import desc
from .models import Book, BookItem, Author, BookItemImage, Category, Publisher
from order.models import Cart
from order.serializers import CartSerializer
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer, BookItemSerializer
from django.shortcuts import render
from django.views import View

# Create your views here.


class BookItemListAPIView(APIView):

    def get(self, request):
        book_items = BookItem.objects.all()
        serializer = BookItemSerializer(
            book_items, many=True)  # chuyen ve dang json
        # return Response(serializer.data)
        listBookItem = serializer.data  # 1 list book item
        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        context = {'listBookItem': listBookItem,
                   'numberOfItems': cart['numberOfItems']}
        return render(request, 'book/bookItems.html', context)


class BookItemDetailAPIView(APIView):
    def delete(self, request, pk):
        snippet = BookItem.objects.get(pk=pk)
        snippet.delete()
        return redirect('http://127.0.0.1:8000/homeAdmin')
        # return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        countImg = 0
        try:
            book_item = BookItem.objects.get(pk=pk)
            countImg = book_item.images.count()

        except BookItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookItemSerializer(book_item)
        # return Response(serializer.data)
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
        context = {'bookItem': bookItem, 'list': array,
                   'numberOfItems': cart['numberOfItems']}

        return render(request, 'detail.html', context)
        # return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def tutorial_list(request, pk):
    if request.method == 'DELETE':
        print('mng')
        bookItem = BookItem.objects.get(id=pk).delete()
        return JsonResponse({'message': ' Tutorials were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    # return Response({"message": "Hello, world!"})


class EditBookItem(View):
    def get(self, request, pk):
        bookItem = BookItem.objects.get(id=pk)
        bookItemImage = BookItemImage.objects.filter(bookItem = bookItem)
        return render(request, 'book/editBook.html', {'bookItem': bookItem, 'bookItemImage': bookItemImage})

    def post(self, request):
        id_bookItem = request.POST['id_bookItem']
        bookItem = BookItem.objects.get(id=id_bookItem)
        bookItem.price = request.POST['price']
        bookItem.description = request.POST['description']
        bookItem.barcode = request.POST['barcode']
        bookItem.header = request.POST['header']
        bookItem.discount = request.POST['discount']
        bookItem.save()

        id_publisher = request.POST['id_publisher']
        publisher = Publisher.objects.get(id=id_publisher)
        publisher.name = request.POST['name_publisher']
        publisher.save()

        id_category = request.POST['id_category']
        category = Category.objects.get(id=id_category)
        category.name = request.POST['name_category']
        category.save()

        id_author = request.POST['id_author']
        author = Author.objects.get(id=id_author)
        author.name = request.POST['name_author']
        author.biography = request.POST['biography']
        author.save()

        id_book = request.POST['id_book']
        book = Book.objects.get(id=id_book)
        book.title = request.POST['title']
        book.language = request.POST['language']
        book.publicationDate = request.POST['publicationDate']
        book.numberOfPages = request.POST['numberOfPages']
        book.save()

        try:
            for image in request.FILES.getlist('img'):
                img = BookItemImage.objects.create(bookItem = bookItem, image = image)
                img.save()
        except:
            pass

        return redirect('http://127.0.0.1:8000/homeAdmin')
class CreateBookItem(View):
    def get(self, request):
        return render(request, 'book/addBook.html')

    def post(self, request):
        name = request.POST['name_publisher']
        publisher = Publisher.objects.create(name=name)
        publisher.save()

        name = request.POST['name_category']
        category = Category.objects.create(name=name)
        category.save()

        name = request.POST['name_author']
        biography = request.POST['biography']
        author = Author.objects.create(name=name, biography=biography)
        author.save()

        title = request.POST['title']
        language = request.POST['language']
        publicationDate = request.POST['publicationDate']
        numberOfPages = request.POST['numberOfPages']
        book = Book.objects.create(title=title, language=language, publicationDate=publicationDate, numberOfPages=numberOfPages, author=author, publisher=publisher, category=category)
        book.save()

        price = request.POST['price']
        description = request.POST['description']
        barcode = request.POST['barcode']
        header = request.POST['header']
        discount = request.POST['discount']
        bookItem = BookItem.objects.create(price=price, description=description, barcode=barcode, header=header, discount=discount, book=book)
        bookItem.save()

        for image in request.FILES.getlist('img'):
            img = BookItemImage.objects.create(bookItem = bookItem, image = image)
            img.save()

        return redirect('http://127.0.0.1:8000/homeAdmin')
def delete(request, pk):
    bookItem = BookItem.objects.get(id=pk)
    book = Book.objects.get(id=bookItem.book.id)
    book.delete()
    bookItem.delete()
    return redirect('http://127.0.0.1:8000/homeAdmin')
