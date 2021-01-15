# Django
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# Graphene
import graphene
from graphql.error import GraphQLError
from graphql.error.located_error import GraphQLLocatedError

# Utils Grahql
from .generic_types import SerializerMessage
from .exceptions import ResponseError , PermissionDenied

class GenericMutationSerializer(graphene.Mutation):
    """
        Generic Mutation Serializer Based on the required needs of the project user_auth

        It Receives extra parameters like:
        - serializer_class
        - is_current_user
        - model
        -type_mutation

        ?reference to parameters
        *is_current_user = refers to the models that depend on the current user of the session
        *type_mutation = refers to the type of operation to be performed
    """

    message = SerializerMessage()
    status = SerializerMessage()

    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        interfaces=(),
        resolver=None,
        output=None,
        arguments=None,
        _meta=None,
        **options
    ):
        super(GenericMutationSerializer, cls).__init_subclass_with_meta__(_meta=_meta, **options)

        cls.serializer_class = options.get('serializer_class', None)
        cls.permissions = options.get('permissions', None)
        cls.update = options.get('update', False)
        cls.model = options.get('model', None)
        cls.data = options.get('data', None)
        cls.delete = options.get('delete', False)

        # ? Expect a user field name -> 'owner'
        # ? where user_field is the field that expect a user in serializer
        cls.set_logged_user_in_field = options.get('set_logged_user', False)

    @classmethod
    def get_data(cls, info, **kwargs):
        """
            Returns the union between the input, and the rest of the
            data indicated in the arguments in a single dictionary
        """
        input = {}
        if 'input' in kwargs:
            input = kwargs.pop('input')

        input.update(kwargs)

        if cls.data:
            input.update(cls.data)

        # If user field is set, the logged user is assigned to
        # the indicated field in serializer
        if cls.set_logged_user_in_field:
            input[cls.set_logged_user_in_field] = info.context.user.pk

        return input

    @classmethod
    def get_logged_user(cls, info, **kwargs):
        return info.context.user

    @classmethod
    def get_instance(cls, info, pk, **kwargs):
        try:
            return cls.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            msg = _('El modelo a actualizar no existe.')
            raise ResponseError(message=str(msg), status="400")

    @classmethod
    def check_permissions(cls, info, data, instance=None,   **kwargs):
        """
            Execute the permission functions by sending the corresponding
            parameters. It evaluates by default an OR, if any permission
            returns True, it allows to continue, if not, it raises an error.
        """
        if not cls.permissions:
            return True

        user = cls.get_logged_user(info, **kwargs)

        # Iterate for pemissions to achieve an OR
        for permission in cls.permissions:
            if permission(user, instance, data):
                return True

        raise PermissionDenied

    @classmethod
    def perform_mutation(cls, root, info, **kwargs):
        """
            Get the data from kwargs, check permissions
            and use the serializer and model to perform
            an update or create operations, returning:
            obj, msg, status
        """
        # Get input data
        data = cls.get_data(info, **kwargs)
        instance = None
        if cls.update or cls.delete:
            pk = int(data.pop('id'))
            instance = cls.get_instance(info, pk, **kwargs)

        cls.check_permissions(info, data, instance)

        if cls.update:
            serializer = cls.serializer_class(
                instance,
                data=data,
                partial=True,
                context={
                    'user': cls.get_logged_user(info, **kwargs)
                }
            )
            cls.type_message = "updated"

        # TODO CHECK AND REFACTOR
        # ! There is no serializer used
        elif cls.delete:
            id_intance = intance.id
            instance.delete()
            msg = "success"
            status = "200"
            return id_intance , msg, status
        else:
            serializer = cls.serializer_class(
                data=data,
                context={
                    'user': cls.get_logged_user(info, **kwargs)
                }
            )
        if serializer.is_valid():
            obj = serializer.save()
            msg = 'success'
            status = '200'
        else:
            msg = serializer.errors
            obj = None
            status = '400'
            raise ResponseError(message=msg, status=status)
        return obj, msg, status


