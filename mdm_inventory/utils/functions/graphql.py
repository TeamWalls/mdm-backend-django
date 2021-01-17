""" 
    generic functions
"""


# graphene
from graphene.utils.str_converters import to_snake_case, to_camel_case

def to_kebab_case(s):
    return to_snake_case(s).replace('_', '-')


def encode_key(k):
    return to_camel_case(k)


def dict_key_to_camel_case(d: dict):
    return dict((encode_key(k), v) for k, v in d.items())


def code_and_message_response(self, type_mutation, serializer):
    pass


def encode_key_suscripction(instance, message):
    pass
