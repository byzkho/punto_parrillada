from injector import inject
from passlib.context import CryptContext
from domain.exceptions.exceptions import InvalidCredentialsException
from domain.repositories.token_repository import TokenRepository
from domain.repositories.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @inject
    def __init__(self, user_repository: UserRepository, token_repository: TokenRepository):
        self.user_repository = user_repository
        self.token_repository = token_repository

    def verify_user(self, username: str, password: str):
        user = self.user_repository.find_by_username(username)
        if not user or not pwd_context.verify(password, user.password):
            raise InvalidCredentialsException()
        return user

    def login_user(self, username: str, password: str):
        user = self.verify_user(username, password)
        if not user:
            raise InvalidCredentialsException(message="Invalid username or password")
        return user
        
    def find_by_token(self, token: str):
        token = self.token_repository.get_one(token)
        user = self.user_repository.get_one(token.user_id)
        if user:
            return user
        return None