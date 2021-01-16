# django
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# graphene
import graphene

# Auth
from graphql_jwt.decorators import login_required

# models
from mdm_inventory.products.models import Product

# serializers
from mdm_inventory.products.serializers import (
    CreateProductSerializer,
    ProductUpdateSerializer,
    # ProductDisableSerializer
)

# types
from mdm_inventory.products.graphql.types import ProductType

# utils
from mdm_inventory.utils.graphql.generic_mutation import GenericMutationSerializer


class InputProductData(graphene.InputObjectType):
    name = graphene.String(description="name of product")
    description = graphene.String(description="description of product")
    code = graphene.String(description="code of product")
    brand  = graphene.String(description="brand of product")
    product_type  = graphene.String(description="product type")
    gross_price =  graphene.Float(description="gross price")
    price_neto = graphene.Float(description="price neto")


class CreateProduct(GenericMutationSerializer):

    class Arguments:
        input = InputProductData(description="Input product data")

    product = graphene.Field(ProductType)

    class Meta:
        model = Product
        description = 'CreateProduct in data base'
        serializer_class = CreateProductSerializer

    @classmethod
    @login_required
    def mutate(cls, root, info, **kwargs):
        product, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Producto Agregado")
        return cls(product=product, message=str(message), status=status)


class UpdateProduct(GenericMutationSerializer):

    class Arguments:
        id = graphene.ID(required=True, description=_("ID Product object"))
        input = InputProductData(description="Input product data")

    product = graphene.Field(ProductType)

    class Meta:
        model = Product
        description = 'UpdateProduct in data base'
        serializer_class = ProductUpdateSerializer
        update = True

    @classmethod
    @login_required
    def mutate(cls, root, info, **kwargs):
        product, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Producto Actualizado")
        return cls(product=product, message=str(message), status=status)

class InputDeleterProduct(graphene.InputObjectType):
    id = graphene.ID(required=True, description=_("ID Product object"))

class DeleterProduct(GenericMutationSerializer):
    class Arguments:
        input = InputDeleterProduct(description="Input product data")

    product = graphene.Field(ProductType)

    class Meta:
        model= Product
        description = 'DeleterProduct in data base'
        delete = True

    @classmethod
    def mutate(cls, root, info, **kwargs):
        message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Producto Eliminado")
        return cls(message=str(message), status=status)
