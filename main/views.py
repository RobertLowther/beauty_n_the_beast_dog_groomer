import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from django.conf import settings


def homepage(request):
    return render(request, "main/index.html")

def contact(request):
    return render(request, "main/contact.html")

def gallery(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/gallery')
    context = {'images' : img_list}
    return render(request, "main/gallery.html", context)

def services(request):
    return render(request, "main/services.html")