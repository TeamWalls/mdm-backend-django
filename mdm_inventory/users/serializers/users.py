# Django
from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import (
    FieldDoesNotExist, ImproperlyConfigured, ValidationError,
)

# JWT
import jwt

# rest
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# User model
from mdm_inventory.users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
        User Signup serializer
    """
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all() , message= _("El correo electrónico ya esta en uso"))
        ],
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all() , message= _("El nombre de usuario ya esta en uso"))
        ],
    )

    password = serializers.CharField(min_length=8, max_length=64,)
    password_confirmation = serializers.CharField(min_length=8, max_length=64,)

    class Meta:
        model = User
        read_only_fields = ('id',)
        exclude = ("is_verified", "is_staff","is_superuser")

    def validate(self, data):
        "Check the password and user type"
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        
        if passwd != passwd_conf:
            raise serializers.ValidationError({"password" : _("Las Contraseñas no coinciden")})
        try :
            password_validation.validate_password(passwd)
        except ValidationError:
            raise serializers.ValidationError({"password" : _("Contraseña muy simple o es totalmente numerica")})
        return data

    def create(self, data):
        """Handle user and email verification"""
        data.pop('password_confirmation')
        user = User.objects.create_user(is_verified=True, **data)
        return user

class UserUpdateSerializer(UserCreateSerializer):
    """
        serialzer for updating user fields 
    """
    class Meta(UserCreateSerializer.Meta):
        pass
        
    def validate(self , data):
        data.pop('password_confirmation' , None)
        data.pop('password' , None)
        email = data.pop("email" , None)
        
        """ 
            Provisional evaluation
        """

        if email is not None:
            raise serializers.ValidationError({"email" : _("No puedes Cambiar de Email")})

        return data

    def update(self, instance, validated_data):
        username = validated_data.pop("username" , None)
        first_name = validated_data.pop("first_name" , None)
        last_name = validated_data.pop("last_name",None)
        is_manager = validated_data.pop("is_manager", None)
        is_supervisor = validated_data.pop("is_supervisor", None)
        is_cashier = validated_data.pop("is_cashier", None)
        profile_picture = validated_data.pop("profile_picture", None)

        if username is not None:
            instance.username = username
        
        if first_name is not None :
            instance.first_name  = first_name

        if is_manager is not None :
            instance.is_manager = is_manager
        
        if is_supervisor is not None :
            instance.is_supervisor = is_supervisor
         
        if is_cashier is not None :
            instance.is_cashier = is_cashier       

        if profile_picture is not None:    
            instance.profile_picture = profile_picture

        instance.save()    
        return instance

class UserDisableSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
        read_only_field = ('id',)

    def validate(self, data):
        return data

    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save()
        return instance

