import graphene

#Models
from mdm_inventory.users.models import User

#types
from mdm_inventory.users.graphql.types import UserType

class QueryUsers(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(root, info):
        return User.objects.filter(is_active=True)