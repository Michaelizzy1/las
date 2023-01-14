from django.shortcuts import render
from .models import Event, Ad

# Create your views here.


def index(response):
    pics = Ad.objects.all()
    context = {'pics':pics}
    return render(response, 'goodnews/index.html', context)


def about(response):
    return render(response, 'goodnews/about.html')


def event(response):
    events = Event.objects.all()
    context = {'events':events}
    return render(response, 'goodnews/event.html', context)


def support(response):
    return render(response, 'goodnews/support.html')


def contact(response):
    return render(response, "goodnews/contact.html")