import graphene
from graphene_django import DjangoObjectType

#models
from mdm_inventory.users.models import (
    Client,
    User,
    Employee
)

#types
from mdm_inventory.users.graphql.types import (
    ClientType,
    UserType,
    EmployeeType
)

class QueryUserGeneric(graphene.ObjectType):
    class Meta:
        description = 'Query of Model Users'
    clients = graphene.List(ClientType)
    users = graphene.List(UserType)
    employees = graphene.List(EmployeeType)

    def resolve_clients(root, info):
        return Client.objects.filter(is_active=True)
    
    def resolve_users(root, info):
        return User.objects.filter(is_active=True)
    
    def resolve_employees(root, info):
        return Employee.objects.filter(is_active=True)

