from django.contrib import admin
from django.urls import path
from .views import home,procesaGrafo
from . import views

app_name = 'home'

urlpatterns = [

    path('home/',home,name="home"),
    path('procesaGrafo',procesaGrafo,name="procesaGrafo")
    
]