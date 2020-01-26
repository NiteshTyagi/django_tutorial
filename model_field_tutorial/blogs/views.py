from django.shortcuts import render,HttpResponse,redirect
from .form import blogsForms
from django.utils import timezone
from .models import blogs
# Create your views here.

def post(request):

    if request.method =='POST':
        form = blogsForms(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            # import pdb
            # pdb.set_trace()
            print(type(request.user),timezone.now(),sep='-----*******------')
            blog.author = request.user
            blog.published_date = timezone.now()

            blog.save()
            return redirect('/blogs/')
    else:
        form = blogsForms()

    return render(request,'blog_form.html',{'form':form})

def home(request):
    All_blogs = blogs.objects.all()
    return render(request,'blog_home.html',{'blogs':All_blogs})
