from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blogs'),
    path('post/',views.post,name='post_blogs')
]
