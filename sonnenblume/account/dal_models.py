from sqlalchemy.orm import Session
from . import models, schemas


## need to import async session here instead

class UserDAL():

    def __init__(self, db_session: Session):
        self.db = db_session


    async def get_user(user_uuid: str):
        q = self.db.query(models.User).filter(models.User.uuid == user_uuid)
        return await q.first()
