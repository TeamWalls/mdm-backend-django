import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.address.models import Address

#types
from mdm_inventory.address.graphql.types import AddressType

class QueryAddress(graphene.ObjectType):
    Address = graphene.List(AddressType)

    def resolve_address(root, info):
        return Address.objects.filter(is_active=True)
