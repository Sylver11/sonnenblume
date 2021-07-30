from fastapi import APIRouter, Depends
from . import models, schemas
from .dependencies import get_user_dal
from .dal_models import UserDAL


router = APIRouter(
    prefix="/account",
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def check_health():
    return {"health_check": "ok"}


@router.get("/users/{user_uuid}", response_model=schemas.User)
async def read_user(user_uuid: str, dal_models: UserDAL = Depends(get_user_dal)):
    db_user = dal_models.get_user(user_uuid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
