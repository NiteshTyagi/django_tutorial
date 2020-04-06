from django.db import models
from django import forms

# Create your models here.

class ImbdMovies(models.Model):
    ''' The Class Defines Model(table) 
        to store the Records of movies'''

    name = models.CharField(max_length=100,blank=True,help_text='Movie Name')
    year = models.PositiveIntegerField(blank=True,null=True,help_text='Movie Year')
    released_date = models.CharField(max_length=20,blank=True,help_text='Movie Released Date')
    Genre = models.CharField(max_length=250,blank=True,help_text='Movie Genre')
    director = models.CharField(max_length=500,blank=True,help_text="Movie's  Director Name")
    writer = models.CharField(max_length=500,blank=True,help_text="Movie's Writer Name")
    cast = models.TextField(blank=True,help_text="Movie's Cast Name")
    plot = models.TextField(blank=True,help_text="Movie's Plot Name")
    language = models.CharField(max_length=500,blank=True,help_text="Movie's Language")
    Awards = models.CharField(max_length=500,blank=True,help_text="Movie's Award")
    image_file = models.ImageField(blank=True,upload_to='images/')
    image_url = models.URLField(blank=True,)

    def __str__(self):
        return self.name


class ImbdMoviesForm(forms.ModelForm):
    class Meta:
        model = ImbdMovies
        fields = '__all__'


