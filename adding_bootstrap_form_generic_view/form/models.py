from django.db import models

# Create your models here.
class Form_data(models.Model):

    name = models.CharField(max_length=180)
    address = models.TextField()

    def __str__(self):
        return self.name