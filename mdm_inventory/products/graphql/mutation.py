import graphene 

from .mutations import (
    CreateProduct,
    UpdateProduct,
    DeleterProduct
)

class MutationProduct(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    deleter_product = DeleterProduct.Field()
  


