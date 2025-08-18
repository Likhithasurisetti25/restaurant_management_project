from django.shortcuts import render
def home(request):
    context={'restaurant':"Tasty Bites"}
    return render (request,'home.html',context)

# Create your views here.
