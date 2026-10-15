from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.user import User


async def get_current_user(
    db: AsyncSession = Depends(get_db),
) -> User:
    user = await db.get(User, 1)

    if user is None:
        raise HTTPException(
            status_code=500,
            detail="Test user not initialized",
        )

    return user