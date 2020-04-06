from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',SearchMovie,name='SearchMovie'),
    path('show-movie/',ShowMovie,name='ShowMovie'),
    path('edit-movie/<int:pk>',EditMovie,name='EditMovie')
]

