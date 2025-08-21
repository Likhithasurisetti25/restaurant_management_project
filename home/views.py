from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from .models import Restaurant
def homepage(request):
    restaurant=Restaurant.objects.first()
    context={"phone_number":settings.RESTAURANT_PHONE}
    return render(request,'home/home.html',context{'restaurant':restaurant if restaurant else "Tasty Bites"})
def restaurant_location(request):
    return render(request,'home/restaurant_location.html')
def Contact_us(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('contact_us')
    else:
        form=ContactForm()
    return render(request,'home/contact_us.html',{'form':form})

# Create your views here.
