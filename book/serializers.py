from rest_framework import serializers
from .models import Book, Author, Publisher, Category, BookItem, BookItemImage
from drf_writable_nested import WritableNestedModelSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    publisher = PublisherSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'language', 'publicationDate',
                  'numberOfPages', 'category', 'author', 'publisher']

class BookItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItemImage
        fields = ['id', 'image', 'index']

class BookItemSerializer(serializers.ModelSerializer):
    images = BookItemImageSerializer(many=True)
    price_book = serializers.SerializerMethodField(read_only=True)
    book = BookSerializer()

    class Meta:
        model = BookItem
        fields = ['id', 'price', 'description', 'barcode', 'header', 'discount', 'book', 'images', 'price_book']

    def get_price_book(self, obj):
        book_item = BookItem.objects.get(pk=obj.id)
        price_book = book_item.price * (1 - book_item.discount)
        return round(price_book, 2)