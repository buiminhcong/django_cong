from django.urls import path
from .views import CartDetailAPIView, CartAPIView, OrderListAPIView, OrderDetailAPIView, ListOrderAPIView

app_name = "orders"

urlpatterns = [
    path('carts/', CartAPIView.as_view(), name="carts"),
    path('carts/<int:pk>/', CartDetailAPIView.as_view(), name="addcart"),
    # path('carts/<int:pk>/cart_book_items/', CartBookItemListAPIView.as_view()),
    # path('carts/<int:cart_pk>/cart_book_items/<int:cart_book_item_pk>/', CartBookItemDetailAPIView.as_view()),
    # path('users/<int:pk>/orders/', OrderListAPIView.as_view()),
    path('orders/', OrderListAPIView.as_view(), name="order"),
    path('orders/<int:order_id>/', OrderDetailAPIView.as_view(), name="orderdetail"),
    path('listorder/', ListOrderAPIView.as_view(), name="listorder")
]