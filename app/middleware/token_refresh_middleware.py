# FILE: token_refresh_middleware.py
from datetime import datetime, timedelta, timezone
from fastapi import Request
from app.manager.cookie_manager import CookieManager
from application.services.token_service import TokenService
from starlette.middleware.base import BaseHTTPMiddleware
import logging

class TokenRefreshMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, token_service: TokenService, cookie_manager: CookieManager):
        super().__init__(app)
        self.token_service = token_service
        self.cookie_manager = cookie_manager

    async def dispatch(self, request: Request, call_next):
        print("TokenRefreshMiddleware: dispatch called")
        response = await call_next(request)
        
        access_token = request.cookies.get("access_token")
        refresh_token = request.cookies.get("refresh_token")
        logging.info(f"Access Token: {access_token}, Refresh Token: {refresh_token}")

        if access_token and refresh_token:
            try:
                logging.info("Verifying access token")
                user_data = self.token_service.verify_token(access_token)
                exp = datetime.fromtimestamp(user_data["exp"], timezone.utc)
                now = datetime.now(timezone.utc)
                logging.info(f"Token Expiration: {exp}, Current Time: {now}")

                # Check if the access token is about to expire in the next 5 minutes
                if exp - now < timedelta(minutes=5):
                    logging.info("Access token is about to expire, renewing token")
                    user_data = self.token_service.verify_token(refresh_token)
                    new_access_token = self.token_service.create_access_token(user_data)
                    expires = datetime.now(timezone.utc) + timedelta(minutes=15)
                    self.cookie_manager.set_access_token_cookie(response, new_access_token, expires)
            except Exception as e:
                logging.error(f"Error in TokenRefreshMiddleware: {e}")

        return response