#graphene
import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.products.models import Product

import django_filters

class ProductType(DjangoObjectType):
    class Meta :
        model = Product
