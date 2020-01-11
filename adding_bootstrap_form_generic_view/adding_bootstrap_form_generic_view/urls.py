"""adding_bootstarp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from form import views as form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',form_view.render_form,name='Render Form',kwargs={'a':'nitesh','b':'tyagi'}),
    path('submit_form/',form_view.submit_form,name='Submit Form'),
    path('show_form_data/',form_view.Detailform_View.as_view(),name='Form data'),

]
