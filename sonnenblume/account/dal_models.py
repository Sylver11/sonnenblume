from sqlalchemy.orm import Session, noload
from sqlalchemy.future import select
from sqlalchemy import update
from uuid import UUID
from . import models, schemas


class UserDAL():

    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_user_by_email(self, email: str):
        stmt = select(models.User).\
                where(models.User.email == email).\
                options(noload('*'))
        q = await self.db_session.execute(stmt)
        return q.scalars().first()

    async def get_user_by_uuid(self, user_uuid: UUID):
        stmt = select(models.User).\
                where(models.User.uuid == user_uuid).\
                options(noload('*'))
        q = await self.db_session.execute(stmt)
        return q.scalars().first()

    async def create_user(self, user: schemas.UserCreate):
        new_user = models.User(
            email=user.email,
            firstname=user.firstname,
            secondname=user.secondname,
        )
        new_user.set_password(user.password)
        self.db_session.add(new_user)
        return await self.db_session.flush()
