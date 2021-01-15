# django
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# graphene
import graphene
import graphql_jwt


# types
from mdm_inventory.users.graphql.types import UserType

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
        serializer_class = CreateClientSerializer

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Usuario Creado")
        return cls(user=user, message=str(message), status=status)

# class UpdateUser(GenericMutationSerializer):

#     class Arguments:
#         id = graphene.ID(required=True, description=_("ID Client object"))
#         input = InputClientData(description="Input user data")

#     client = graphene.Field(ClientType)

#     class Meta:
#         model = Client
#         description = 'CreateClient in data base'
#         serializer_class = ClientUpdateSerializer
#         update = True

#     @classmethod
#     def mutate(cls, root, info, **kwargs):
#         client, message, status = cls.perform_mutation(root, info, **kwargs)
#         message = _("Cliente Actualizado")
#         return cls(client=client, message=str(message), status=status)

# class InputDisableClient(graphene.InputObjectType):
#     id = graphene.ID(required=True, description=_("ID Client object"))

# class DisableClient(GenericMutationSerializer):
#     class Arguments:
#         input = InputDisableClient(description="Input user data")

#     client = graphene.Field(ClientType)

#     class Meta:
#         model= Client
#         description = 'CreateClient in data base'
#         serializer_class = CreateClientSerializer
#         update = True

#     @classmethod
#     def mutate(cls, root, info, **kwargs):
#         client, message, status = cls.perform_mutation(root, info, **kwargs)
#         message = _("Cliente Desactivado")
#         return cls(message=str(message), status=status)
