import graphene

#models
from mdm_inventory.products.models import Product

#types
from mdm_inventory.products.graphql.types import ProductType

class QueryProduct(graphene.ObjectType):
    products = graphene.List(ProductType)

    def resolve_products(root, info):
        return Product.objects.filter(is_active=True)
