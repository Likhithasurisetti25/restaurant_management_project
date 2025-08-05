from django.urls import path
from .views import *

urlpatterns = [
    path('restaurant-location/',views.restaurant_location,name='restaurant_location'),
    path('menu/',views.menu_view,name='menu'),
    
]