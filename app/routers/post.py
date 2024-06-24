from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, dependencies

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.create_post(db, post, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    posts = dependencies.get_user_posts_cached(user_id=current_user.id, db=db)
    return posts

@router.delete("/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(dependencies.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    post = crud.delete_post(db, post_id, user_id=current_user.id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post