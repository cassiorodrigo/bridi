from django.shortcuts import render, redirect
from .forms import ContactForm
import os
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        message_name = request.POST['name']
        message_surname = request.POST['surname']
        message_email = request.POST['email']
        message = request.POST['enquery1']
        print(f'{message_name} {message_surname} \nenviou um email a partir do {message_email}. \nMensagem: {message}')
        try:
            send_mail(
                'Teste1',
                message,
                message_email,
                ['cassiorodrigo@gmail.com'],

            )
            messages.success(request, "Message Sent! Thank you for your query.")
            return redirect('home',)
        except Exception as e:
            messages.warning(request, f"Message not Sent. Something whet wrong. Please, try Again soon. {e}")

    return render(request, 'contact.html', {"form":form})

def galery(request):
    # caminho = os.walk('bridimain/static/img')
    caminho = os.fspath('/home/libertyforever/bridi/bridi/bridimain/static/img/')
    imagens = list((os.walk(caminho)))

    return render(request, 'galery.html', {"caminho":'/img/', "imagens":imagens[0][2]})


def videos(request):
    caminho = os.fspath('/home/libertyforever/bridi/bridi/bridimain/static/videos')
    videos = list((os.walk(caminho)))

    return render(request, "videos.html", {"caminho":"/videos/", "videos":videos[0][2]})