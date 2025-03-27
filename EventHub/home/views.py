from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Events
from .serializers import EventsSerializer


# @api_view(['GET'])
# def event_list(request):
#     events = Events.objects.all()
#     serializer = EventsSerializer(events, many=True)
#     return Response(serializer.data)

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


# TODO: make web-interface for CRUD
