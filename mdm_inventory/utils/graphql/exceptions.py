from django.utils.translation import gettext_lazy as _

class PermissionDenied(Exception):
    def __init__(self, message=None , status="403"):
        super().__init__(message)
        self.message = str(_("No tienes permisos para realizar esta acción."))
        self.status = status

class ResponseError(Exception):
    def __init__(self, message, status=None, params=None ):
        super().__init__(message)
        self.message = message
        self.status = status
        self.params = params

class GraphqlWsResponseError(Exception):
    """Errors data from the GraphQL response."""

    def __init__(self, response, message=None):
        """Exception constructor."""
        super().__init__(self)
        self.message = message
        self.response = response

    def __str__(self):
        """Nice string representation."""
        return f"{self.message or 'Error in GraphQL response'}: {self.response}!"