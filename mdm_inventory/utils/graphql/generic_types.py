""""
    Type and global data of the application, and connections
"""

from graphene.types.scalars import Scalar
from graphene import Connection, Int


class SerializerMessage(Scalar):
    @staticmethod
    def serialize(dt):
        return dt


class TotalCountConnection(Connection):
    """ class to obtain the total and current element number of a page """
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length

    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)


class FileUpload(Scalar):
    class Meta:
        description = (
            "Variables of this type must be set to null in mutations. They will be "
            "replaced with a filename from a following multipart part containing "
            "a binary file. "
            "See: https://github.com/jaydenseric/graphql-multipart-request-spec."
        )

    @staticmethod
    def serialize(value):
        return value

    @staticmethod
    def parse_literal(node):
        return node

    @staticmethod
    def parse_value(value):
        return value