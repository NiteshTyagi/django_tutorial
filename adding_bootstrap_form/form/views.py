from django.shortcuts import render,HttpResponse,redirect
from .models import Form_data

# Create your views here.

def render_form(request):
    return render(request,"index.html")

def submit_form(request):    
    if request.GET.get('name') and request.GET.get('address'):
        Form_data(name=request.GET.get('name'),address=request.GET.get('address')).save()

    return redirect('/show_form_data')

def form_data(request):
    record_set = Form_data.objects.all()
    return render(request,"form_data.html",{'record_set':record_set})