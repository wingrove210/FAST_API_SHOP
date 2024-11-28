import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import db_helper, User, Profile, Post
from sqlalchemy.engine import Result
from typing import Union
from sqlalchemy.orm import joinedload


async def create_user(session: AsyncSession, username: str) -> User:
    new_user = User(username=username)  # Corrected variable name
    session.add(new_user)
    await session.commit()
    print("user", new_user)
    return new_user

async def get_user_by_username(session: AsyncSession, username: str) -> Union[User, None]:
    stmt = select(User).where(User.username == username)
    user: Union[User, None] = await session.scalar(stmt)
    print("found user", username, user)
    return user

async def create_user_profile(session: AsyncSession, user_id: str, first_name: Union[str, None], last_name: Union[str, None], bio: Union[str, None]) -> Profile:
    profile = Profile(user_id=user_id, first_name=first_name, last_name=last_name, bio=bio)
    session.add(profile)
    await session.commit()
    return profile
  
async def show_users_with_profiles(session: AsyncSession) -> list[User]:
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    # result: Result = await session.execute(stmt)
    # users = result.scalars()
    users = await session.scalars(stmt)
    for user in users:
        print("User", user.username)
        if user.profile:
            print("Profile", user.profile.first_name)
        else:
            print("No profile found for this user.")
      
async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username="pricer")
        # await create_user(session=session, username="dicer")
        # user_alice = await get_user_by_username(session=session, username="pricer")
        # user_alex = await get_user_by_username(session=session, username="dicer")

        # await create_user_profile(
        #     session=session,
        #     user_id=user_alice.id,
        #     first_name="grown",
        #     last_name="Smith",
        #     bio="Progger"
        # )
        # await create_user_profile(
        #     session=session,
        #     user_id=user_alex.id,
        #     first_name="grower",
        #     last_name="Johnson",
        #     bio="Progger"
        # )
        await show_users_with_profiles(session=session)
        
if __name__ == "__main__":
    asyncio.run(main())