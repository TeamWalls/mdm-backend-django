import graphene

# Querys
from mdm_inventory.users.graphql.query import QueryUserGeneric

#Mutations
from mdm_inventory.users.graphql.mutation import MutationUser
from mdm_inventory.clients.graphql.mutation import MutationClient

class Query(
        QueryUserGeneric,
        graphene.ObjectType
):
    pass

class Mutation(
    MutationGenericUsers,
    MutationClient,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query , mutation=Mutation )
