from django.contrib import admin
from .models import ImbdMovies
# Register your models here.

@admin.register(ImbdMovies)
class ImbdModelAdmin(admin.ModelAdmin):
    list_display =[ 'name','year','language','director']
    