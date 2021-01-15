import graphene

# Querys
from mdm_inventory.clients.graphql.query import QueryClient
from mdm_inventory.users.graphql.query import QueryUsers

#Mutations
from mdm_inventory.users.graphql.mutation import MutationUser
from mdm_inventory.clients.graphql.mutation import MutationClient

class Query(
        QueryClient,
        QueryUsers,
        graphene.ObjectType
):
    pass

class Mutation(
    MutationGenericUsers,
    MutationClient,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation ,)
