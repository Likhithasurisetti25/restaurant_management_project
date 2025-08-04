from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class MenuView(APIView):
    def get(self,request):
        menu=[{"name":"Panner Butter Masala","description":"Creamy cottage chese curry","price":150},
        {"name":"Veg Biryani","description":"spicy vegetable rice","price":120},{"name":"Gulab Jam","description":"sweet dessert","price":50}]
        return Response(menu,status=status.HTTP_200_OK)
def show_menu(request):
    response=requests.get("http://127.0.0.1:8000/api/menu")
    menu=response.json()
    return render(request,'menu.html',{'menu':menu})
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
