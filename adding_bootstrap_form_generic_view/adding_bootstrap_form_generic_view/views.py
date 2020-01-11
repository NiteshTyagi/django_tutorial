from django.shortcuts import HttpResponse,render


def index_bootstrap(request):
    return render(request,'index.html')

def basic_template(request):
    return render(request,'base.html')


