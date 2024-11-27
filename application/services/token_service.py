# token_service.py
from datetime import datetime, timedelta, timezone
import jwt
from domain.entities.user import User
from domain.exceptions.exceptions import InvalidCredentialsException
from domain.repositories.token_repository import TokenRepository
from injector import inject

ACCESS_SECRET_KEY = "your_secret_key"
REFRESH_SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRATION = 60  # minutos
REFRESH_TOKEN_EXPIRATION = 30  # días

class TokenService:
    @inject
    def __init__(self, token_repository: TokenRepository):
        self.token_repository = token_repository

    def create_access_token(self, user: User):
        expiration = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRATION)
        token = jwt.encode(
            {
                "id": user.id, 
                "exp": expiration
            }, 
            ACCESS_SECRET_KEY, algorithm=ALGORITHM
        )
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
            return payload
        except jwt.ExpiredSignatureError:
            raise InvalidCredentialsException("Access token has expired")
        except jwt.InvalidTokenError:
            raise InvalidCredentialsException("Invalid access token")
        
    def verify_refresh_token(self, token: str):
        try:
            payload = jwt.decode(token, REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise InvalidCredentialsException("Refresh token has expired")
        except jwt.InvalidTokenError:
            raise InvalidCredentialsException("Invalid refresh token")