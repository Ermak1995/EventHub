from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Events, Registrations, Eventtickets, Eventtypes, Locations, Organizers
from .serializers import EventsSerializer, EventticketsSerializer, EventtypesSerializer, LocationsSerializer, \
    OrganizersSerializer, RegistrationsSerializer


# @api_view(['GET'])
# def event_list(request):
#     events = Events.objects.all()
#     serializer = EventsSerializer(events, many=True)
#     return Response(serializer.data)

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventticketsViewSet(viewsets.ModelViewSet):
    queryset = Eventtickets.objects.all()
    serializer_class = EventticketsSerializer


class EventtypesViewSet(viewsets.ModelViewSet):
    queryset = Eventtypes.objects.all()
    serializer_class = EventtypesSerializer


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


class OrganizersViewSet(viewsets.ModelViewSet):
    queryset = Organizers.objects.all()
    serializer_class = OrganizersSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    queryset = Registrations.objects.all()
    serializer_class = RegistrationsSerializer
