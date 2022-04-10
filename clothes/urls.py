from django.urls import path
from .views import ClothesItemListAPIView, ClothesItemDetailAPIView

app_name = "clothes"
urlpatterns = [
    path('clothes_items/', ClothesItemListAPIView.as_view(), name="clothes_items"),
    path('clothes_items/<int:pk>/', ClothesItemDetailAPIView.as_view(), name="clothes_item_detail"),
]