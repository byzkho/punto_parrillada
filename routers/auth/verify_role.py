from fastapi import Depends, HTTPException, status
from app.config.fastapi_users.session_fastapi_users import fastapi_users

def get_user_with_role(required_role: str):
    def dependency(
        user=Depends(fastapi_users.current_user),
    ):
        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return user

    return dependency