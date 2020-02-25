from django.db import models
from django.utils.timezone import now

# Create your models here.

class todoModel(models.Model):
    """ This is the ToDO class for model"""

    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
        


