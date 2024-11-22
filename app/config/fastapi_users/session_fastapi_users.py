from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database.models import User
from app.config.fastapi_users.user_manager import UserManager
from app.config.database.database import get_db
from fastapi_users.authentication.transport.bearer import BearerTransport

SECRET_KEY = "secret-key"
transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)

jwt_authentication = AuthenticationBackend(
    name="jwt",  # Nombre único para este backend
    transport=transport,  # Puedes configurar un transport si lo necesitas
    get_strategy=get_jwt_strategy,
)

async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(User, session)

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
    

fastapi_users = FastAPIUsers(
    get_user_manager=get_user_manager,
    auth_backends=[jwt_authentication],
)