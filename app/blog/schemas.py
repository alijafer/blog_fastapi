from pydantic import BaseModel
from sqlalchemy import orm
from typing import List, Optional

class BlogBase(BaseModel):
    title:str
    body:str


class Blog(BlogBase):
    class Config():
        orm_mode = True
class ShowUser(BaseModel):
    username:str
    email:str
    blogs: List[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):

    title:str
    body:str
    creator: ShowUser
    class Config():
        orm_mode = True

class User(BaseModel):
    username:str
    email:str
    password:str


class Login(BaseModel):
    username:str
    password:str
    class Config():
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

