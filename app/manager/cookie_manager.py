# FILE: cookie_manager.py
from fastapi import Response
from datetime import datetime

class CookieManager:
    def set_access_token_cookie(self, response: Response, access_token: str, expires: datetime):
        response.set_cookie(
            "access_token",
            access_token,
            expires=expires,
            httponly=True,
            samesite="Strict"
        )

    def set_refresh_token_cookie(self, response: Response, refresh_token: str, expires: datetime):
        response.set_cookie(
            "refresh_token",
            refresh_token,
            expires=expires,
            httponly=True,
            samesite="Strict"
        )

    def delete_access_token_cookie(self, response: Response):
        response.delete_cookie("access_token")

    def delete_refresh_token_cookie(self, response: Response):
        response.delete_cookie("refresh_token")