from django.forms import ModelForm

from .models import blogs

class blogsForms(ModelForm):

    class Meta:
        model = blogs
        fields = ['title','content']