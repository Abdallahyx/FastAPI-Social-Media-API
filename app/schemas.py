from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class UserRequest(BaseModel):
    email: EmailStr
    password: str
    
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at : datetime

    class Config:
        from_attributes = True    
        
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostRequest(PostBase):
    pass
    
class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserResponse
    
    class Config:
        from_attributes = True
        

class PostResponse(BaseModel):
    Post : Post
    Votes : int = 0
    
    class Config:
        from_attributes = True
    
        
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] 
        
        
class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)