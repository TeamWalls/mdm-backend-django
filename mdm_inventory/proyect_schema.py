import graphene

# Querys
from mdm_inventory.clients.graphql.query import QueryClient
from mdm_inventory.users.graphql.query import QueryUsers
from mdm_inventory.products.graphql.query import QueryProduct
from mdm_inventory.address.graphql.query import QueryAddress

#Mutations
from mdm_inventory.users.graphql.mutation import MutationUser
from mdm_inventory.clients.graphql.mutation import MutationClient
from mdm_inventory.products.graphql.mutation import MutationProduct

class Query(
        QueryClient,
        QueryUsers,
        QueryProduct,
        QueryAddress,
        graphene.ObjectType
):
    pass

class Mutation(
    MutationUser,
    MutationClient,
    MutationProduct,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation ,)
