import graphene 

from .mutations import (
    CreateUser
)

class MutationUser(graphene.ObjectType):
    create_user = graphene.Field(CreateUser)
