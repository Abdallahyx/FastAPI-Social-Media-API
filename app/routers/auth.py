from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_db
from ..schemas import UserRequest, UserResponse
from .. import models, utils, oauth2
from ..schemas import Token
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends

router = APIRouter(
    tags=['Authentication']
)


@router.post("/register", status_code = status.HTTP_201_CREATED, response_model=UserResponse)
async def register(user: UserRequest, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}
