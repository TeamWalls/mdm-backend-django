#graphene
import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.users.models import User

class UserType(DjangoObjectType):
    class Meta :
        model = User
        # filter_fields = {
        #     'name': ['exact', 'icontains'],
        #     'created': ['exact', 'icontains'],
        #     'username': ['exact', 'icontains'],
        #     'email': ['exact', 'icontains'],
        #     'is_active': ['exact'],
        #     'is_verified': ['exact'],
        #     'is_superuser': ['exact'],
        # }