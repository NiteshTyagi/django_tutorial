from django.contrib import admin
from .models import blogs
# Register your models here.

# @admin.register(blogs)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id','author','published_date']

admin.site.register(blogs,ModelAdmin)
