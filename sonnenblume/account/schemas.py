from pydantic import BaseModel
from typing import List



class Role(BaseModel):
    uuid: str
    name: str
    description: str

    class Config:
        orm_mode = True


class Group(BaseModel):
    uuid: str
    name: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    firstname: str
    secondname: str
    password: str
    confirm_password: str
    thirdparty_authenticated: bool
    thirdparty_name = str
    active = bool


class UserLogin(UserBase):
    password: str
    current_login_at: str
    current_login_ip: str


class User(UserBase):
    uuid: str
    firsname: str
    secondname: str
    roles: List[Role] = []
    groups: List[Group] = []

    class Config:
        orm_mode = True



