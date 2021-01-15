import graphene 

from .mutations import (
    CreateUser,
    UpdateUser,
    DeleterUser
)

class MutationUser(graphene.ObjectType):
    create_user = graphene.Field(CreateUser)
    update_user = graphene.Field(UpdateUser)
    deleter_user = graphene.Field(DeleterUser)

