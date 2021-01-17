# django
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# graphene
import graphene
import graphql_jwt

# Auth
from graphql_jwt.decorators import login_required

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
from  mdm_inventory.utils.graphql.exceptions import ResponseError

class InputUserData(graphene.InputObjectType):
    first_name = graphene.String(description="Primer Nombre")
    last_name = graphene.String(description="Apellido")
    email = graphene.String(description="correo electronico")
    username = graphene.String(description="Nombre de usuario")
    profile_picture = graphene.String(description="Foto de perfil")
    is_manager = graphene.Boolean(description="Gerente")
    is_supervisor = graphene.Boolean(description="SuperVisor")
    is_cashier = graphene.Boolean(description="Cajero")
    password = graphene.String(description="password")
    password_confirmation = graphene.String(description="password confirmation")

class CreateUser(GenericMutationSerializer):
    
    class Arguments:
        input = InputUserData(description="Input User Data")

    user = graphene.Field(UserType)

    class Meta:
        model = User
        description = 'CreateUser in data base'
        serializer_class = UserCreateSerializer

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Usuario Creado")
        return cls(user=user, message=str(message), status=status)

class UpdateUser(GenericMutationSerializer):
    
    class Arguments:
        id = graphene.ID(description="Id User")
        input = InputUserData(description="Input User Data")

    user = graphene.Field(UserType)

    class Meta:
        model = User
        description = 'CreateUser in data base'
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
        model = User
        description = 'Deleter in data base'
        delete = True

    @classmethod
    def mutate(cls, root, info, **kwargs):
        message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Usuario Eliminado")
        return cls(message=str(message), status=status)

#Login Person
class CustomObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        user_login = info.context.user
        return cls(user=user_login)

class UserLoginInput(graphene.InputObjectType):
    email = graphene.String(description="Email user")
    password = graphene.String(description="password")

class Login(graphene.Mutation):
    """
        Mutacion for verification , password recovery and user verification
    """
    class Arguments:
        input = UserLoginInput(description=_("Input user data"))

    user = graphene.Field(UserType)
    token = graphene.String()
    exp_token = graphene.Int()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        email = kwargs["input"]["email"].lower()
        kwargs["input"]["email"] = email
        password = kwargs["input"]["password"] 
        try :
            #?send user data to be purchased
            data = kwargs.pop("input")
            data_mutation = CustomObtainJSONWebToken.mutate(root,info,**data)
            user = data_mutation.user
            token = data_mutation.token
            exp = data_mutation.payload["exp"]
            if user.is_verified is True :
                pass
            else:
                msg = _("Debes verificar tu usuario antes de empezar a usar mdm_inventory")
                raise ResponseError(message=str(msg), code="400", params={"is_verified": "False"})
        except ObjectDoesNotExist :
            msg = _("Datos invalidos")
            raise ResponseError(message=str(msg), code="400")  
        return cls(user=user , token=token , exp_token=exp)

from graphql_jwt.shortcuts import get_token
