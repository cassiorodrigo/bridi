from django.shortcuts import render
from .forms import ContactForm
import os
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        print(request.POST)
        message_name = request.POST['name']
        message_surname = request.POST['surname']
        message_email = request.POST['email']
        message = request.POST['enquery1']
        print(f'{message_name} {message_surname} enviou um email a partir do {message_email}. \nMensagem: {message}')

        send_mail(
            'Teste1',
            message,
            message_email,
            ['cassiorodrigo@gmail.com'],

        )
    return render(request, 'contact.html', {"form":form})

def galery(request):
    # caminho = os.walk('bridimain/static/img')
    caminho = os.fspath('bridimain/static/img')
    imagens = list((os.walk(caminho)))
    novalistaimagens = []


    return render(request, 'galery.html', {"caminho":'static/img', "imagens":imagens[0][2]})


def videos(request):
    caminho = os.fspath('bridimain/static/videos')
    videos = list((os.walk(caminho)))
    novalistaimagens = []
    return render(request, "videos.html", {"caminho":"static/videos", "videos":videos[0][2]})