from django.urls import path

from clothes import views
from .views import ClothesItemListAPIView, ClothesItemDetailAPIView, CreateKidClothes, EditKidClothes

app_name = "clothes"
urlpatterns = [
    path('clothes_items/', ClothesItemListAPIView.as_view(), name="clothes_items"),
    path('clothes_items/<int:pk>/', ClothesItemDetailAPIView.as_view(), name="clothes_item_detail"),
    path('edit_kidClothes/<int:pk>/', EditKidClothes.as_view(), name="edit_kidClothes"),
    path('update_kidClothes/', EditKidClothes.as_view(), name="update_kidClothes"),
    path('delete_kidClothes/<int:pk>/', views.delete, name="delete_kidClothes"),
    path('add_kidClothes/', CreateKidClothes.as_view(), name="add_kidClothes"),
]