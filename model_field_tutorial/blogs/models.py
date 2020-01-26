from django.db import models
from django.utils import timezone


# Create your models here.



class blogs(models.Model):

    author = models.CharField(max_length=120)
    published_date = models.DateTimeField(blank=True,null=True)
    title = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.title
