
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('alicetele', views.index),               #our domain.com/alicetele will be active
    
]
