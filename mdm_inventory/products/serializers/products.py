# Django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import (
    FieldDoesNotExist, ImproperlyConfigured, ValidationError,
)

# DRF
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# models

from mdm_inventory.products.models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    """Product create serializer"""
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'code',
            'brand',
            'product_type',
            'gross_price',
            'price_neto'
        )

    def validate(self, data):
        return data

    def create(self, data):
        product = Product.objects.create(**data)
        return product

class ProductUpdateSerializer(CreateProductSerializer):
    class Meta(CreateProductSerializer.Meta):
        pass

    def update(self, instance, validated_data):
        name = validated_data.pop("name", None)
        description = validated_data.pop("description", None)
        code = validated_data.pop("code", None)
        brand =validated_data.pop("brand", None)
        product_type =validated_data.pop("product_type", None)
        gross_price = validated_data.pop("gross_price", None)
        price_neto  = validated_data.pop("price_neto", None)
        
        if name is not None :
            instance.name = name
        
        if description is not None :
            instance.description = description
            
        if code is not None :
            instance.code = code

        if brand is not None :
            instance.brand = brand

        if product_type is not None :
            instance.product_type = product_type
        
        if gross_price is not None :
            instance.gross_price = gross_price

        if price_neto is not None :
            instance.price_neto = price_neto

        instance.save()
        return instance

# class ProductDisableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id',)
#         read_only_field = ('id',)

#     def validate(self, data):
#         return data

#     def update(self, instance, validated_data):
#         instance.is_active = False
#         instance.save()
#         return instance