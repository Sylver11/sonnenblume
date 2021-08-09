from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from uuid import UUID
from . import models, schemas
from .dependencies import get_user_dal
from .dal_models import UserDAL


router = APIRouter(
    prefix="/account",
    responses={404: {"description": "Not found"}},
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/testing-token/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}



@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                dal_models: UserDAL = Depends(get_user_dal):
    db_user = await dal_models.get_user_by_email(form_data.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    if not db_user.check_password(form_data.password)
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    #need to return correct access token here 
    return {"access_token": user.username, "token_type": "bearer"}




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
