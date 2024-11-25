from injector import singleton
from domain.repositories.token_repository import TokenRepository
from infrastructure.database.models import TokenTable

@singleton
class TokenRepositoryImpl(TokenRepository):
    def __init__(self, session):
        self.session = session

    def get_one(self, token):
        return self.session.query(TokenTable).filter(TokenTable.token == token).first()
        
    def save(self, payload: dict) -> str:
        token = TokenTable(**payload)
        self.session.add(token)
        self.session.commit()
        return token.token