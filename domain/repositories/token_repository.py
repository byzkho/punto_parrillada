from abc import ABC, abstractmethod


class TokenRepository(ABC):
    @abstractmethod
    def save(self, payload: dict) -> str:
        pass
    
    @abstractmethod
    def get_one(self, token: str) -> dict:
        pass