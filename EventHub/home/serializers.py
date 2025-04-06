from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Events, EventTickets, EventTypes, Locations, Organizers, Registrations


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class EventTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTickets
        fields = '__all__'


class EventTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTypes
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class OrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizers
        fields = '__all__'


class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = '__all__'


