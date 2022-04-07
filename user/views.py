from django.shortcuts import render, redirect
from .models import User, Address
from order.models import Cart
from django.contrib import auth
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from order.serializers import CartSerializer
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import AllowAny



class signupView(APIView):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        rePassword = request.POST['rePassword']
        if password == rePassword:
            try:
                User.objects.get(username=username)
                return render(request, 'signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                Address.objects.create(phone=phone, firstName=first_name, lastName=last_name, user=user)

                Cart.objects.create(user_id=user.id)
                auth.login(request, user)
                request.session['user_id'] = user.id
                # print("huyen" + request.session.get('user_id'))
                response = redirect('/book/book_items/')
                return response
        else:
            return render(request, 'signup.html', {'error': 'Password does not match!'})

class loginView(APIView):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user.id
            try:
                cart = Cart.objects.get(user_id=user.id)
            except Cart.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            response = redirect('/v1/api/book_items/')
            return response
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})

class logoutView(APIView):

    def get(self, request):
        auth.logout(request)
        return redirect('home')

class logoutView(APIView):

    def get(self, request):
        return render(request, 'profile.html')

# class UserDetailAPIView(APIView):
#
#     def get(self, request, pk):
#         is_staff = request.user.is_staff
#         id = request.user.id
#         if not is_staff and id!=pk:
#             return Response({
#                 'status': '400',
#                 'message': 'Not has permission'
#             })
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({
#                 'status': 404,
#                 'message': 'User not found'
#             })
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#
# class UserAPIView(CreateAPIView):
#     permission_classes = [AllowAny]
#     model = User
#     serializer_class = UserCreateSerializer


