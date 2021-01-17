import graphene 

from .mutations import (
    CreateUser,
    UpdateUser,
    DeleterUser,
    Login
)

import graphql_jwt

class MutationUser(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    deleter_user = DeleterUser.Field()
    Login = Login.Field()


