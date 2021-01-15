# django
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# graphene
import graphene
import graphql_jwt

#models
from mdm_inventory.users.models import User

# types
from mdm_inventory.users.graphql.types import UserType

#serializers
from mdm_inventory.users.serializers import (
   UserCreateSerializer,
   UserUpdateSerializer,
   UserCreateSerializer
)

# utils
from mdm_inventory.utils.graphql.generic_mutation import GenericMutationSerializer

class InputUserData(graphene.InputObjectType):
    first_name = graphene.String(description="Primer Nombre")
    last_name = graphene.String(description="Apellido")
    email = graphene.String(description="correo electronico")
    username = graphene.String(description="Nombre de usuario")
    profile_picture = graphene.String(description="Foto de perfil")
    is_manager = graphene.Boolean(description="Gerente")
    is_supervisor = graphene.Boolean(description="SuperVisor")
    is_cashier = graphene.Boolean(description="Cajero")

class CreateUser(GenericMutationSerializer):
    
    class Arguments:
        input = InputUserData(description="Input User Data")

    user = graphene.Field(ClientType)

    class Meta:
        model = Client
        description = 'CreateClient in data base'
        serializer_class = UserCreateSerializer

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Usuario Creado")
        return cls(user=user, message=str(message), status=status)

class UpdateUser(GenericMutationSerializer):
    
    class Arguments:
        input = InputUserData(description="Input User Data")

    user = graphene.Field(ClientType)

    class Meta:
        model = Client
        description = 'CreateClient in data base'
        serializer_class = UserUpdateSerializer
        update = True

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Usuario Actualizado ")
        return cls(user=user, message=str(message), status=status)


class InputDisableData(graphene.InputObjectType):
    id = graphene.Int(description="Id User ref pk")

class DeleterUser(GenericMutationSerializer):
    
    class Arguments:
        input = InputDisableData(description="Input User Data")

    class Meta:
        model = Client
        description = 'Deleter in data base'
        delete = True

    @classmethod
    def mutate(cls, root, info, **kwargs):
        message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Usuario Eliminado")
        return cls(message=str(message), status=status)

