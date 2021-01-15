import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.clients.models import Client

#types
from mdm_inventory.clients.graphql.types import ClientType

class QueryClient(graphene.ObjectType):
    clients = graphene.List(ClientType)

    def resolve_clients(root, info):
        return Client.objects.filter(is_active=True)
