from django.shortcuts import render, HttpResponse

from .models import Contactus

# Create your views here.

def contactus(request):

    if request.method == 'POST':
        form = Contactus(request.POST)

        print('---------------------222222--------',form.errors)

        if form.is_valid():
            print(dir(request),form.cleaned_data,sep='----------11111111111-------------')
            return HttpResponse('Thank you')
    else:
        form = Contactus({'first_name':'nitesh',
                           'last_name':'Tyagi',
                           'email_address':'a@gmail.com',
                           'address':'dsfdsfd',
        })

    return render(request,'form.html',{'form':form})
