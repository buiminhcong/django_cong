from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Publisher(models.Model):
    name = models.CharField(max_length=255)

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=127)
    publicationDate = models.DateField()
    numberOfPages = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class BookItem(models.Model):
    price = models.FloatField(default=0)
    description = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    header = models.CharField(max_length=1024)
    discount = models.FloatField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')

class BookItemImage(models.Model):
    bookItem = models.ForeignKey(BookItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/images/book_items_images/')
