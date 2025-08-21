from django.shortcuts import render
from django.conf import settings
def home(request):
    context={'restaurant':"Tasty Bites"}
    return render (request,'home.html',context)
    return render(request,"home.html",{"restaurant_name":settings.RESTAURANT_NAME})

# Create your views here.
