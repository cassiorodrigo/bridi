from django.shortcuts import render
from .forms import ContactForm
import os

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {"form":form})

def galery(request):
    # caminho = os.walk('bridimain/static/img')
    caminho = os.fspath('bridimain/static/img')
    imagens = list((os.walk(caminho)))
    novalistaimagens = []
    for i in imagens[0][2]:
        print(i)

    return render(request, 'galery.html', {"caminho":'static/img', "imagens":imagens[0][2]})
# Create your views here.
