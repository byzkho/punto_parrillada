from domain.exceptions.exceptions import ResourceNotFoundException
from functools import wraps


def check_none_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            raise ResourceNotFoundException(
                resource=args[0].__class__.__name__, 
                identifier=args[1])
        return result
    return wrapper