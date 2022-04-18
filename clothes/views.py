from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from order.models import Cart
from order.serializers import CartSerializer
from .models import Clothes, ClothesItem, ClothesItemImage, KidClothes
from .serializers import ClothesItemSerializer
from django.shortcuts import render

# Create your views here.


class ClothesItemListAPIView(APIView):

    def get(self, request):
        clothes_items = ClothesItem.objects.all()
        serializer = ClothesItemSerializer(clothes_items, many=True) # chuyen ve dang json
        # return Response(serializer.data)
        listClothesItem = serializer.data # 1 list Clothes item
        user_id = request.session.get('user_id')
        try:
            cart = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart = CartSerializer(cart).data
        context = {'listClothesItem': listClothesItem,  'numberOfItems': cart['numberOfItems']}
        return render(request, 'index.html', context)

class ClothesItemDetailAPIView(APIView):

    def get(self, request, pk):
        countImg = 0
        try:
            clothes_item = ClothesItem.objects.get(pk=pk)
            countImg = clothes_item.images.count()


        except ClothesItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothesItemSerializer(clothes_item)
        #return Response(serializer.data)
        clothesItem = serializer.data

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
        context = {'clothesItem': clothesItem, 'list': array,  'numberOfItems': cart['numberOfItems']}

        return render(request, 'detail.html', context)
        # return Response(serializer.data)
def delete(request, pk):
    kidClothes = KidClothes.objects.get(id=pk)
    clothesItem = ClothesItem.objects.filter(clothes=kidClothes)
    # clothesItemImages = ClothesItemImage.objects.filter(clothesItem=clothesItem).values_list('id', flat=True)

    
    kidClothes.delete()
    clothesItem.delete()
    # clothesItemImages.delete()
    return redirect('http://127.0.0.1:8000/homeAdmin')
class EditKidClothes(View):
    def get(self, request, pk):
        kidClothes = KidClothes.objects.get(id=pk)
        kidClothesItem = ClothesItem.objects.get(clothes=kidClothes)
        return render(request, 'clothes/editKidClothes.html', {'kidClothes': kidClothes, 'kidClothesItem': kidClothesItem})

    def post(self, request):
        id_kidClothesItem = request.POST['id_kidClothesItem']
        kidClothesItem = ClothesItem.objects.get(id=id_kidClothesItem)
        kidClothesItem.price = request.POST['price']
        kidClothesItem.description = request.POST['description']
        kidClothesItem.header = request.POST['header']
        kidClothesItem.discount = request.POST['discount']
        kidClothesItem.save()

        id_kidClothes = request.POST['id_kidClothes']
        kidClothes = KidClothes.objects.get(id=id_kidClothes)
        kidClothes.productName = request.POST['productName']
        kidClothes.material = request.POST['material']
        kidClothes.countryOfOrigin = request.POST['countryOfOrigin']
        
        kidClothes.size = request.POST['size']
        kidClothes.pattern = request.POST['pattern']
        try:
            tmp = request.POST['plusSize']
            kidClothes.plusSize = True
        except:
            kidClothes.plusSize = False
        kidClothes.brand = request.POST['brand']
        kidClothes.gender = request.POST['gender']
        kidClothes.recommendedAge = request.POST['recommendedAge']
        kidClothes.save()

        return redirect('http://127.0.0.1:8000/homeAdmin/#kidClothes')

class CreateKidClothes(View):
    def get(self, request):
        return render(request, 'clothes/addKidClothes.html')

    def post(self, request):
        productName = request.POST['productName']
        material = request.POST['material']
        countryOfOrigin = request.POST['countryOfOrigin']
        size = request.POST['size']
        pattern = request.POST['pattern']
        try:
            plusSize = request.POST['plusSize']
        except:
            plusSize = False
        brand = request.POST['brand']
        gender = request.POST['gender']
        recommendedAge = request.POST['recommendedAge']
        kidClothes = KidClothes.objects.create(productName=productName, material=material, countryOfOrigin=countryOfOrigin, size=size,
        pattern=pattern, plusSize=plusSize, brand=brand, gender=gender, recommendedAge=recommendedAge)
        kidClothes.save()

        price = request.POST['price']
        description = request.POST['description']
        header = request.POST['header']
        discount = request.POST['discount']
        clothesItem = ClothesItem.objects.create(price=price, description=description, header=header, discount=discount, clothes=kidClothes)
        clothesItem.save()

        return redirect('http://127.0.0.1:8000/homeAdmin/#kidClothes')