from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Events, Eventtickets, Eventtypes, Locations, Organizers, Registrations


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class EventticketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventtickets
        fields = '__all__'


class EventtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventtypes
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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
