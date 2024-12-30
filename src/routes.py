from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models import User
from src.schemas import UserCreate, User as UserSchema


router = APIRouter(prefix="/users", tags=["users"])

"""response model è uno schema che descrive come devono apparire i dati in API , in questo caso come UserSchema
che fa riferimento a User e UserCreate come abbiamo importato sopra """

@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # cerchiamo un users:
    db_user = db.query(User).filter(User.email == user.email).first() # questo modo di scrivere lo permette SQL
    """db.query(User)=select *(all),
       filter=from user where User.email == user.email,
       first=limit 1"""
    """se esiste eccezzione"""
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    """se non esiste creiamo un users , id si mette auto da solo"""
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=user.password  # In real app, hash the password!
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# questo get si usa come slicing per estrarre solo gli users che vogliamo, skip salta il numero che vogliamo
# limit imposta quanti ne vogliamo vedere
# per esempio skip 5 limit 6 prende solo 6 users e i primi 5 li salta percio ti dara 6 users da id 6 a 11
@router.get("/{users}", response_model=List[UserSchema])
def slicing_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

"""questo get si usa per cercare un specifico ID"""
@router.get("/{user_id}", response_model=UserSchema)
def search_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

"""cambia le informazioni di qualcosa gia creato"""
@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.dict().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}