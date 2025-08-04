from django import forms
from .models import Contact
class ContactFrom(forms.ModelForm):
    class Meth:
        model=Contact
        fields=['name','email']