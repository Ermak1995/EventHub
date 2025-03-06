from django.http import HttpResponse
from django.shortcuts import render
from .models import Events


def index(request):
    return HttpResponse("Hello, World")


def get_all_events(request):
    events = Events.objects.all()
    return HttpResponse(events)
