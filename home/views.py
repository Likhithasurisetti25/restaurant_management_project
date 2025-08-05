from django.shortcuts import render
from .forms import ContactForm
def home(request):
    return render(request,'home/home.html')
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
