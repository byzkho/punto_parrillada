# token_service.py
from datetime import datetime, timedelta, timezone
import jwt
from domain.entities.user import User
from domain.repositories.token_repository import TokenRepository
from injector import inject
from domain.exceptions.exceptions import InvalidCredentialsException, InvalidTokenException

ACCESS_SECRET_KEY = "your_secret_key"
REFRESH_SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRATION = 15  # minutos
REFRESH_TOKEN_EXPIRATION = 30  # días

class TokenService:
    @inject
    def __init__(self, token_repository: TokenRepository):
        self.token_repository = token_repository

    def create_access_token(self, user: User):
        expiration = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRATION)
        token = jwt.encode({"id": user.id, "username": user.username, "exp": expiration}, ACCESS_SECRET_KEY, algorithm=ALGORITHM)
        return token

    def create_refresh_token(self, data: dict):
        expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRATION)
        data.update({"exp": expire})
        encoded_jwt = jwt.encode(data, REFRESH_SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def is_token_in_db(self, token: str) -> bool:
        return self.token_repository.get_one(token)
    
    def save_token(self, token: str):
        return self.token_repository.save(token)
    
    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, ACCESS_SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("username")
            id: int = payload.get("id")
            if username is None:
                raise InvalidCredentialsException("Could not validate credentials")
            return {"username": username, "id": id}
        except jwt.PyJWTError as e:
            raise InvalidTokenException(e)