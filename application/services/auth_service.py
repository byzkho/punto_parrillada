from datetime import datetime, timedelta, timezone
from injector import inject
from passlib.context import CryptContext
from application.services.token_service import TokenService
from domain.exceptions.exceptions import InvalidCredentialsException
from domain.repositories.token_repository import TokenRepository
from domain.repositories.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @inject
    def __init__(self, user_repository: UserRepository, token_repository: TokenRepository, token_service: TokenService):
        self.user_repository = user_repository
        self.token_repository = token_repository
        self.token_service = token_service

    def verify_user(self, username: str, password: str):
        user = self.user_repository.find_by_username(username)
        if not user or not pwd_context.verify(password, user.password):
            raise InvalidCredentialsException()
        return user

    def login_user(self, username: str, password: str):
        user = self.verify_user(username, password)
        if not user:
            raise InvalidCredentialsException(message="Invalid username or password")
        refresh_token = self.token_service.create_refresh_token({"username": user.username, "id": user.id})
        access_token = self.token_service.create_access_token(user)
        expires = datetime.now(timezone.utc) + timedelta(days=2)
        self.token_service.save_token({
            "token": refresh_token,
            "user_id": user.id
        })
        return {"access_token": access_token, "refresh_token": refresh_token, "user": user, "expires": expires}
        
    def find_by_token(self, token: str):
        token = self.token_repository.get_one(token)
        user = self.user_repository.get_one(token.user_id)
        if user:
            return user
        return None
    
    def find_by_id(self, user_id: int):
        return self.user_repository.get_one(user_id)