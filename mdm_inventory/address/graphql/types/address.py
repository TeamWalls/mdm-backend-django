#graphene
import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.address.models import Address

class AddressType(DjangoObjectType):
    class Meta :
        model = Address
        # filter_fields = {
        #     'name': ['exact', 'icontains'],
        #     'created': ['exact', 'icontains'],
        #     'username': ['exact', 'icontains'],
        #     'email': ['exact', 'icontains'],
        #     'is_active': ['exact'],
        #     'is_verified': ['exact'],
        #     'is_superuser': ['exact'],
        # }
