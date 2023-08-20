from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from .. import oauth2
from ..database import get_db
from .. import models
from ..schemas import UserResponse, Vote

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(vote: Vote, db: Session= Depends(get_db), current_user: UserResponse = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    
    query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = query.first()
    
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Voted"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Unvoted"}
        