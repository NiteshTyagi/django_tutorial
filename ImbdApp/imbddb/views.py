from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
import requests
from .models import ImbdMovies,ImbdMoviesForm
from django.core.files import File
import os
from urllib.request import urlopen
from tempfile import NamedTemporaryFile



API_KEY = '869f6fd3'

def SearchMovie(request):
    values = {
        'movie_name' : request.GET.get('movie_name','')
    }
    if values['movie_name']!='':
        movie_obj = ImbdMovies.objects.filter(name__icontains=values['movie_name'])
        if movie_obj:
            values.update({'movie': movie_obj[0]})
        else:
            urls = 'http://www.omdbapi.com/?t='+values['movie_name']+'&apikey='+API_KEY
            response = requests.get(urls)
            response = response.json()
            if response.get('Response') == 'False':
                values.update({'error':response.get('Error')})
            else:
                record = ImbdMovies(
                    name = response.get('Title'),
                    year = int(response.get('Year','0000')[:4]),
                    released_date = response.get('Released'),
                    Genre = response.get('Genre'),
                    director = response.get('Director'),
                    writer = response.get('Writer'),
                    cast = response.get('Actors'),
                    plot = response.get('Plot'),
                    language = response.get('Language'),
                    Awards = response.get('Awards'),
                    image_url = response.get('Poster')
                )
                record.save()
                if response.get('Poster',None):
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(urlopen(record.image_url).read())
                    img_temp.flush()
                    record.image_file.save(f"image_{record.pk}", File(img_temp))
                values.update({'movie':record})
    return render(request,'index.html',values)



def ShowMovie(request):
    movies = ImbdMovies.objects.all()
    if movies:
        return render(request,'showmovies.html',{'movies':movies}) 
    else:
        return render(request,'showmovies.html')


def EditMovie(request,pk):
    movie = ImbdMovies.objects.get(id=pk)
    form = ImbdMoviesForm(request.POST or None,request.FILES or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('ShowMovie')

    return render(request, 'editform.html', {'form': form})