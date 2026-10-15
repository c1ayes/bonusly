import asyncio

from app.core.database import async_session_maker
from app.models.user import User


async def create_test_user():  
    async with async_session_maker() as db:
        user = await db.get(User, 1)

        if user is not None:
            print(f"Тестовый пользователь уже существует: id={user.id}")
            return

        user = User(
            name="Test User",
            hashed_password="temporary",
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        print(f"Тестовый пользователь создан: id={user.id}")


if __name__ == "__main__":
    asyncio.run(create_test_user())
