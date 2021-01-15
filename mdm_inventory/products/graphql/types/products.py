#graphene
import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.products.models import Product

class ProductType(DjangoObjectType):
    class Meta :
        model = Product
        # filter_fields = {
        #     'name': ['exact', 'icontains'],
        #     'created': ['exact', 'icontains'],
        #     'username': ['exact', 'icontains'],
        #     'email': ['exact', 'icontains'],
        #     'is_active': ['exact'],
        #     'is_verified': ['exact'],
        #     'is_superuser': ['exact'],
        # }
