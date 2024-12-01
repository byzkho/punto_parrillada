class InvalidCredentialsException(Exception):
    def __init__(self, message="Invalid username or password"):
        self.detail = [{
            "type": "value_error",
            "loc": ["username", "password"],
            "msg": message
        }]

class ResourceNotFoundException(Exception):
    def __init__(self, resource, identifier):
        self.detail = {
            "type": "value_error",
            "loc": ["id"],
            "msg": f"{resource} with ID {identifier} was not found"
        }
        
class InvalidFileTypeException(Exception):
    def __init__(self, message="Invalid file type"):
        self.detail = [{
            "type": "value_error",
            "loc": ["file"],
            "msg": message
        }]
        
class InvalidTokenException(Exception):
    def __init__(self, message="Invalid token", status_code=401):
        self.detail = [{
            "status": status_code,
            "type": "value_error",
            "loc": ["token"],
            "msg": message
        }]
        self.status_code = status_code
        
class ExpiredTokenException(Exception):
    def __init__(self, message="Expired token"):
        self.detail = [{
            "status": 401,
            "type": "value_error",
            "loc": ["token"],
            "msg": message
        }]
        
        self.status_code = 401