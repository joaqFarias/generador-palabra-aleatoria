
from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.root),
    path('random_word', views.random_word),
    path('random_word/reset', views.reset),
]