from pydantic import BaseModel, Field, field_validator

from domain.enum.user_role import UserRole


class CreateUserDTO(BaseModel):
    full_name: str
    email: str
    password: str
    username: str
    role: UserRole

    @field_validator("role", mode="before")
    def validate_role(cls, v):
        if isinstance(v, str):
            try:
                return UserRole(v.lower())
            except ValueError:
                raise ValueError(
                    f"Role '{v}' no es válido. Debe ser uno de: {[role.value for role in UserRole]}"
                )
        return v