#graphql
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
import graphql_jwt

#mutations
from mdm_inventory.clients.graphql.mutations import (
    CreateClient,
    UpdateClient,
    DisableClient
)

class MutationClient(graphene.ObjectType):
    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    disable_client = DisableClient.Field()
