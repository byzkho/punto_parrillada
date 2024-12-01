# convert_mapper.py
from functools import wraps

def dto_to_dict_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Asumimos que el primer argumento después de `self` es el DTO
        dto = args[1]
        dto_dict = dto.dict()
        # Reemplazamos el DTO con el diccionario
        new_args = (args[0], dto_dict) + args[2:]
        return func(*new_args, **kwargs)
    return wrapper

def dict_to_model_decorator(model_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Asumimos que el primer argumento después de `self` es el diccionario
            dto_dict = args[1]
            model_instance = model_class(**dto_dict)
            # Reemplazamos el diccionario con la instancia del modelo
            new_args = (args[0], model_instance) + args[2:]
            return func(*new_args, **kwargs)
        return wrapper
    return decorator