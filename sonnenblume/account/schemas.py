from pydantic import BaseModel, ValidationError, validator, EmailStr
from typing import List
from uuid import UUID

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
    email: EmailStr

#    @validator('confirm_password')
#    def passwords_match(cls, v, values, **kwargs):
#        if 'password' in values and v != values['password']:
#            raise ValueError('passwords do not match')
#        return v


class UserCreate(UserBase):
    firstname: str
    secondname: str
    password: str
#    confirm_password: str


class UserLogin(UserBase):
    password: str
    current_login_at: str
    current_login_ip: str


class User(UserBase):
    uuid: UUID
    firstname: str
    secondname: str
    roles: List[Role] = []
    groups: List[Group] = []

    class Config:
        orm_mode = True



