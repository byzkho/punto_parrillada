from fastapi import Depends, HTTPException, status
from app.config.fastapi_users.session_fastapi_users import fastapi_users


async def get_current_active_user(
    user=Depends(fastapi_users.current_user),
):
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return user