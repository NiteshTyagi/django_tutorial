from django.contrib import admin

from .models import todoModel

# Register your models here.

@admin.register(todoModel)
class todoModeladmin(admin.ModelAdmin):
    readonly_fields = ['created_date']
    list_display = ['text','created_date','active']
    list_editable = ['active']