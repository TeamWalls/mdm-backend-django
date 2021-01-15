# Graphene Django Optimizer
import graphene_django_optimizer as gql_optimizer

DEFAULT_FILTER = {
    'is_active': True
}


def optimized_model_resolver(root, info, model, filters=DEFAULT_FILTER, **kwargs):
    return gql_optimizer.query(
        model.objects.filter(**filters), info, **kwargs
    )


def optimized_model_resolver_decorator(model, filters=DEFAULT_FILTER):
    def decorator(resolver_func):
        def wrapper_resolver(root, info, **kwargs):
            return gql_optimizer.query(
                model.objects.filter(**filters), info, **kwargs
            )
        return wrapper_resolver
    return decorator