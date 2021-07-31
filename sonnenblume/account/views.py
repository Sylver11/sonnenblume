from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from . import models, schemas
from .dependencies import get_user_dal
from .dal_models import UserDAL


router = APIRouter(
    prefix="/account",
    responses={404: {"description": "Not found"}},
)


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate,
                      dal_models: UserDAL = Depends(get_user_dal)):
    db_user = dal_models.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Email already exists")
    return await dal_models.create_user(user = user)


@router.get("/users/get-user-by-uuid/{user_uuid}",
            response_model=schemas.User)
async def read_user_by_uuid(user_uuid: UUID,
                    dal_models: UserDAL = Depends(get_user_dal)):
    db_user = await dal_models.get_user_by_uuid(user_uuid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/get-user-by-email/{email}",
            response_model=schemas.User)
async def read_user_by_email(email: str,
                    dal_models: UserDAL = Depends(get_user_dal)):
    db_user = await dal_models.get_user_by_email(email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("")
async def check_health():
    return {"health_check": "ok"}
