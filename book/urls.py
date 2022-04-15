from django import views
from django.urls import path
from .views import BookItemListAPIView, BookItemDetailAPIView
from .import views

app_name = "book"
urlpatterns = [
    path('book_items/', BookItemListAPIView.as_view(), name="book_items"),
    path('book_items/<int:pk>/', BookItemDetailAPIView.as_view(), name="book_item_detail"),
    # path('<int:pk>/', views.tutorial_list, name="delete_book"),
    path('<int:pk>/', views.delete, name="delete_book"),
    path('edit_book_items/<int:pk>/', views.EditBookItem.as_view(), name="edit_book"),
    path('update_book_items/', views.EditBookItem.as_view(), name="update_book"),
    path('add_book_items/', views.CreateBookItem.as_view(), name="add_book"),
]