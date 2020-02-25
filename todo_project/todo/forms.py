from django.forms import ModelForm,TextInput
from .models import todoModel

class todoModelForm(ModelForm):

    class Meta:
        model = todoModel
        fields = ['text','active']
        widgets = {
            'text':TextInput(attrs={'placeholder':'Enter your todo work'})
        }