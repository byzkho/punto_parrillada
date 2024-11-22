from fastapi_users import BaseUserManager, UUIDIDMixin
from app.config.database.models import User

SECRET_KEY = "secret-key"

class UserManager(UUIDIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request=None):
        print(f"Usuario registrado: {user.email}")
