from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Events, Registrations, TicketTypes, EventTickets, EventTypes, Locations, Organizers
from .serializers import EventsSerializer, EventTicketsSerializer, EventTypesSerializer, LocationsSerializer, \
    OrganizersSerializer, RegistrationsSerializer


# @api_view(['GET'])
# def event_list(request):
#     events = Events.objects.all()
#     serializer = EventsSerializer(events, many=True)
#     return Response(serializer.data)

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]


class EventTicketsViewSet(viewsets.ModelViewSet):
    queryset = EventTickets.objects.all()
    serializer_class = EventTicketsSerializer


class EventTypesViewSet(viewsets.ModelViewSet):
    queryset = EventTypes.objects.all()
    serializer_class = EventTypesSerializer


class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


class OrganizersViewSet(viewsets.ModelViewSet):
    queryset = Organizers.objects.all()
    serializer_class = OrganizersSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    queryset = Registrations.objects.all()
    serializer_class = RegistrationsSerializer
