from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',MenuView.as_view()),
    path('',show_menu,name='show_menu'),