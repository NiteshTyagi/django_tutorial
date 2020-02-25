from django.urls import path
from .views import *

urlpatterns = [
    path('todo/',home,name='home'),
    path('process_form/',process_form,name='process_form'),
    path('delete/<int:flag>',delete_completed,name='delete_completed'),
    path('edit_todo/<int:pk>',edit_todo,name='edit_todo')
]