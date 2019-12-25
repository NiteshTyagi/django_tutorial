from django.shortcuts import HttpResponse,render


def index_bootstrap(request):
    return render(request,'index.html')