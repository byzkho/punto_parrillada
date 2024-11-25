class InvalidCredentialsException(Exception):
    def __init__(self, message="Invalid username or password"):
        self.detail = [{
            "type": "value_error",
            "loc": ["username", "password"],
            "msg": message
        }]

class ResourceNotFoundException(Exception):
    def __init__(self, resource, identifier):
        self.detail = [{
            "type": "value_error",
            "loc": ["id"],
            "msg": f"{resource} with ID {identifier} was not found"
        }]
        
class InvalidFileTypeException(Exception):
    def __init__(self, message="Invalid file type"):
        self.detail = [{
            "type": "value_error",
            "loc": ["file"],
            "msg": message
        }]
        
class InvalidPhoneNumberException(Exception):
    def __init__(self, message="Invalid phone number"):
        self.detail = [{
            "type": "value_error",
            "loc": ["phone_number"],
            "msg": message
        }]