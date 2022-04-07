from django.urls import path
from .views import BookItemListAPIView, BookItemDetailAPIView

app_name = "book"
urlpatterns = [
    path('book_items/', BookItemListAPIView.as_view(), name="book_items"),
    path('book_items/<int:pk>/', BookItemDetailAPIView.as_view(), name="book_item_detail"),
]