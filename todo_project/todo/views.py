from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todoModel
from .forms import todoModelForm

import logging
_logger = logging.getLogger(__name__)
# Create your views here.

def home(request):
    form = todoModelForm()
    context = todoModel.objects.all().order_by('-created_date')
    return render(request,'index.html',{'to_do_list':context,'form':form})


def process_form(request):
    if request.POST:
        form = todoModelForm(request.POST)
        saved_object = form.save(commit=False)
        # saved_object.active = True
        saved_object.save()
    return redirect(home)

def delete_completed(request,flag):
        if flag == 1:
            todoModel.objects.all().delete()
        else:
            todoModel.objects.exclude(active=True).delete()
        return redirect(home)

def edit_todo(request,pk):
        record = todoModel.objects.get(pk=pk)
        
        if request.POST:
            form = todoModelForm(request.POST,instance=record)
            saved_object = form.save(commit=False)
            # saved_object.active = True
            saved_object.save()
            return redirect(home)
        else:
            form = todoModelForm(instance=record)

        return render(request,"edit_todo.html",{'form':form,'pk':pk})


