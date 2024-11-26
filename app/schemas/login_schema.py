from pydantic import BaseModel, ConfigDict

from app.schemas.user_schema import UserSchema

class LoginSchema(BaseModel):
    access_token: str
    refresh_token: str
    user: UserSchema
    
    model_config = ConfigDict(
        str_strip_whitespace=True,
        str_min_length=1
    )