from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from .models import Form_data
from django.views import generic

# Create your views here.

def render_form(request,**kwargs):

    return render(request,"index.html")

def submit_form(request):    
    if request.GET.get('name') and request.GET.get('address'):
        Form_data(name=request.GET.get('name'),address=request.GET.get('address')).save()

    return HttpResponseRedirect('/show_form_data')

class Detailform_View(generic.ListView):
    template_name = 'form_data.html'
    context_object_name = 'record_set'

    def get_queryset(self):
        return Form_data.objects.all()