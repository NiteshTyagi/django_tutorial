from django.contrib import admin
from .models import model_fields
# Register your models here.

class model_fields_view(admin.ModelAdmin):
    
    fieldsets = [
        ('Integer Fields' ,{'fields':['biginteger','integer','floatfield','positivesmall','small','positive']}),
        ('Character',{'fields':['text','character']}),
        ('Time and Date Field',{'fields':['date','duration','datetime']}),
        # ('File and other Related Field',{'fields':['binary','filefield','slug','boolean','url','emailfield','nullboolean']}),
    ]

admin.site.register(model_fields,model_fields_view)
