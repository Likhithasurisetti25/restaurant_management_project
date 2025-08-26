from django.shortcuts import render
from datetime import datetime
from django.conf import settings
def home(request):
    context={'restaurant':"Tasty Bites"}
    currentyear=datetime.now().year
    return render(request,"home.html",{"restaurant_name":settings.RESTAURANT_NAME,"year":currentyear})

# Create your views here.
