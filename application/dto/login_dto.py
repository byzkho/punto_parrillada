from pydantic import BaseModel, ConfigDict

class LoginDto(BaseModel):
    username: str
    password: str
    
    model_config = ConfigDict(from_attributes=True)