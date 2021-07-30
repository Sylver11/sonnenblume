from sqlalchemy.orm import Session
from . import models, schemas


class UserDAL():

    def __init__(self, db_session: Session):
        self.db = db_session

    async def get_user(self, user_uuid: str):
        q = await self.db.query(models.User).filter(models.User.uuid == user_uuid)
        return q.first()
