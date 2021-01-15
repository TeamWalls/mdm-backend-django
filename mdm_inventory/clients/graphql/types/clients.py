#graphene
import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.clients.models import Client

class ClientType(DjangoObjectType):
    class Meta :
        model = Client
        # filter_fields = {
        #     'name': ['exact', 'icontains'],
        #     'created': ['exact', 'icontains'],
        #     'username': ['exact', 'icontains'],
        #     'email': ['exact', 'icontains'],
        #     'is_active': ['exact'],
        #     'is_verified': ['exact'],
        #     'is_superuser': ['exact'],
        # }
