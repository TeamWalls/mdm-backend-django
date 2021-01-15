# django
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# graphene
import graphene
import graphql_jwt

# Auth
from graphql_jwt.decorators import login_required

# models
from mdm_inventory.clients.models import Client

# serializers
from mdm_inventory.clients.serializers import (
    CreateClientSerializer,
    ClientUpdateSerializer,
    ClientDisableSerializer
)

# types
from mdm_inventory.clients.graphql.types import ClientType

# utils
from mdm_inventory.utils.graphql.generic_mutation import GenericMutationSerializer


class InputClientData(graphene.InputObjectType):
    first_name = graphene.String(description="first name")
    last_name = graphene.String(description="last name")
    dni = graphene.String(description="DNI")
    phone_number = graphene.String(description="phone number")
    full_name = graphene.String(description="full name")
    address = graphene.Int(description="ID address relate", required=False)


class CreateClient(GenericMutationSerializer):

    class Arguments:
        input = InputClientData(description="Input user data")

    client = graphene.Field(ClientType)

    class Meta:
        model = Client
        description = 'CreateClient in data base'
        serializer_class = CreateClientSerializer

    @classmethod
    def mutate(cls, root, info, **kwargs):
        client, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Cliente Agregado")
        return cls(client=client, message=str(message), status=status)


class UpdateClient(GenericMutationSerializer):

    class Arguments:
        id = graphene.ID(required=True, description=_("ID Client object"))
        input = InputClientData(description="Input user data")

    client = graphene.Field(ClientType)

    class Meta:
        model = Client
        description = 'CreateClient in data base'
        serializer_class = ClientUpdateSerializer
        update = True

    @classmethod
    def mutate(cls, root, info, **kwargs):
        client, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Cliente Actualizado")
        return cls(client=client, message=str(message), status=status)

class InputDisableClient(graphene.InputObjectType):
    id = graphene.ID(required=True, description=_("ID Client object"))

class DisableClient(GenericMutationSerializer):
    class Arguments:
        input = InputDisableClient(description="Input user data")

    client = graphene.Field(ClientType)

    class Meta:
        model= Client
        description = 'CreateClient in data base'
        serializer_class = CreateClientSerializer
        update = True

    @classmethod
    def mutate(cls, root, info, **kwargs):
        client, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Cliente Desactivado")
        return cls(message=str(message), status=status)
