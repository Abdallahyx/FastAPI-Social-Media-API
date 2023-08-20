from ..database import get_db
from ..schemas import UserRequest, UserResponse
from .. import models, utils
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("/{id}", response_model=UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

