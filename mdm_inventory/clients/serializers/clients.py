# Django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import (
    FieldDoesNotExist, ImproperlyConfigured, ValidationError,
)

# DRF
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# models

from mdm_inventory.clients.models import Client


class CreateClientSerializer(serializers.ModelSerializer):
    """Cient create serializer"""
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'dni',
            'phone_number',
            'full_name',
        )

    def validate(self, data):
        return data

    def create(self, data):
        client = Client.objects.create(**data)
        return client

class ClientUpdateSerializer(CreateClientSerializer):
    class Meta(CreateClientSerializer.Meta):
        pass

    def update(self, instance, validated_data):
        first_name = validated_data.pop("first_name", None)
        last_name = validated_data.pop("last_name", None)
        dni = validated_data.pop("dni", None)
        phone_number =validated_data.pop("phone_number", None)
        full_name =validated_data.pop("full_name", None)
        address = validated_data.pop("address", None)
        
        if first_name is not None :
            instance.first_name = first_name
        
        if last_name is not None :
            instance.last_name = last_name

        if dni is not None :
            instance.dni = dni

        if phone_number is not None :
            instance.phone_number = phone_number

        if full_name is not None :
            instance.full_name = full_name

        if address is not None :
            instance.address = address

        instance.save()
        return instance

class ClientDisableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id',)
        read_only_field = ('id',)

    def validate(self, data):
        return data

    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save()
        return instance