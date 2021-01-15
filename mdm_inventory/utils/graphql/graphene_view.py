"""
    graphqlview class overwriting for custom error response
"""

import traceback
# django
from django.conf import settings
# graphene
from graphene_django.views import GraphQLView
from graphql.error import GraphQLSyntaxError, GraphQLError
from graphql.error.located_error import GraphQLLocatedError
from graphql.error import format_error as format_graphql_error

# Utils
from mdm_inventory.utils.graphql import ResponseError , PermissionDenied , GraphqlWsResponseError
from mdm_inventory.utils.functions import *


def encode_code(code):
    if code is None:
        return None
    return to_kebab_case(code)


def encode_params(params):
    if params is None:
        return None
    return dict_key_to_camel_case(params)


def format_response_error(error: GraphqlWsResponseError):
    return {
        'message': error.message,
    }


def format_response_error(error: ResponseError):
    return {
        'message': error.message,
        'code': encode_code(error.code),
        'params': error.params,
    }


def format_response_error(error: PermissionDenied):
    return {
        'message': error.message,
        'code': "403",
    }


def format_internal_error(error: Exception):
    """
        overwriting function to customize internal error message sending formatr
    """
    message = 'An error has occurred'
    code = 400
    if settings.DEBUG:
        return {
            'code': code,
            'message': str(error),
        }
    return {
        'code': code,
        'message': message,
    }


def format_located_error(error):
    #import os
    # os.system('clear')
    """
        overwriting function to customize local error message sending formatr
    """
    if isinstance(error.original_error, GraphQLLocatedError):
        return format_located_error(error.original_error)
    if isinstance(error.original_error, ResponseError):
        return format_response_error(error.original_error)
    if isinstance(error.original_error, PermissionDenied):
        return format_response_error(error.original_error)
    if isinstance(error.original_error, GraphqlWsResponseError):
        return format_response_error(error.original_error)
    return format_internal_error(error.original_error)


class SafeGraphQLView(GraphQLView):
    @staticmethod
    def format_error(error):
        try:
            if isinstance(error, GraphQLLocatedError):
                return format_located_error(error)
            if isinstance(error, GraphQLSyntaxError):
                return format_graphql_error(error)
            if isinstance(error, GraphQLError):
                return format_graphql_error(error)
        except Exception as e:
            return format_internal_error(e)
