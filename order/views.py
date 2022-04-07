from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer, OrderSerializer, OrderBookItemSerializer
from .models import Cart, CartBookItem, Order, Shipment, Cash, Credit, Transfer, OrderBookItem
from book.models import BookItem
from user.models import Address, User
from user.serializers import AddressSerializer

# Create your views here.

class CartDetailAPIView(APIView):

    def post(self, request, pk):
        try:
            quantity = request.POST['quantity']
            book_item = BookItem.objects.get(pk=pk)
            user_id = request.session.get('user_id')
            cart = Cart.objects.get(user_id=user_id)
            check = False
            cart_book_items = CartBookItem.objects.filter(cart_id=cart.id)
            for cart_book_item in cart_book_items:
                if cart_book_item.bookItem.id == book_item.id:
                    cart_book_item.quantity = cart_book_item.quantity + int(quantity)
                    cart_book_item.save()
                    check = True
                    break
            if not check:
                CartBookItem(cart=cart, bookItem=book_item, quantity=quantity).save()
            try:
                cart = Cart.objects.get(user_id=user_id)
            except Cart.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CartSerializer(cart)
            response = redirect('/order/carts/')
            return response
            # return Response(serializer.data)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)


class CartAPIView(APIView):
    def get(self, request):
        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        context = {'cart': cart, 'numberOfItems': cart['numberOfItems']}
        # return Response(cart)
        return render(request, 'cart.html', context)


class OrderListAPIView(APIView):
    def get(self, request):
        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
            address = Address.objects.filter(user_id=user_id)[0]
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        address = AddressSerializer(address).data

        total = cart['subTotal'] + 30000

        context = {'cart': cart, 'address': address, 'total': total, 'numberOfItems': cart['numberOfItems']}
        # return Response(cart)
        return render(request, 'checkout.html', context=context)

    def post(self, request):
        user_id = request.session.get('user_id')
        order = Order.objects.create(user_id=user_id)

        cart = Cart.objects.get(user_id=user_id)
        cart_book_items = CartBookItem.objects.filter(cart_id=cart.id)

        total = 0
        for cart_book_item in cart_book_items:
            order_book_items = OrderBookItem(order=order, bookItem=cart_book_item.bookItem, quantity=cart_book_item.quantity)
            total += cart_book_item.bookItem.price * cart_book_item.quantity * (1 - cart_book_item.bookItem.discount)
            order_book_items.save()
            # sau kho oder thi xoa khoi gio hang
            cart_book_item.delete()

        lastName = request.POST['lastName']
        firstName = request.POST['firstName']
        phone = request.POST['phone']
        city = request.POST['city']
        district = request.POST['district']
        detail = request.POST['detail']

        user = User.objects.get(pk=user_id)

        address = Address(lastName=lastName,firstName=firstName, phone=phone, city=city,
                          district=district, detail=detail, user=user)
        address.save()

        shipment_fee = 30000
        shipment = Shipment(order=order, address=address, shippingFee=shipment_fee)
        shipment.save()

        total += shipment_fee

        cash = Cash(total=total, order=order)
        cash.save()

        try:
            order = Order.objects.get(pk=order.id)
        except Order.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        # truyen id sang order detail
        return redirect('/order/orders/' + str(order.id) + '/')

class OrderDetailAPIView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        order_serializer = OrderSerializer(order).data

        order_book_items = OrderBookItem.objects.filter(order_id=order.id)
        order_bookitems_serializer = OrderBookItemSerializer(order_book_items, many=True).data

        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data

        context = {'order': order_serializer, 'orderBookItems': order_bookitems_serializer, 'numberOfItems': cart['numberOfItems']}
        return render(request, 'orderdetail.html', context=context)
        # return Response(order_bookitems_serializer)

class ListOrderAPIView(APIView):
    def get(self, request):
        user_id = request.session.get('user_id')
        orders = Order.objects.filter(user_id=user_id)
        order_serializer = OrderSerializer(orders, many=True).data
        for order in order_serializer:
            # print(order['total'])
            order_book_items = OrderBookItem.objects.filter(order_id=order['id'])
            order_bookitems_serializer = OrderBookItemSerializer(order_book_items, many=True).data
            order['orderBookItem'] = order_bookitems_serializer
        # return Response(order_serializer)

        # return render(request, 'homepage/listorder.html')
        context = {'orders': order_serializer}
        return render(request, 'homepage/listorder.html', context=context)