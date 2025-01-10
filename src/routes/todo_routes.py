from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models import Todo
from src.schemas.todo_schemas import TodoCreate, Todo as TodoSchema, TodoBase

router = APIRouter(prefix="/todo", tags=["todos"])

@router.post("/create", response_model=TodoSchema)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.title == todo.title).first()
    if db_todo:
        raise HTTPException(status_code=400, detail="todo already created")

    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        user_id=todo.user_id
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/user_id", response_model=List[TodoSchema])
def list_todos(user_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.user_id == user_id).all()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# cercare una specifica attivita per titolo e user id
@router.get("/user_id/title", response_model=List[TodoSchema])
def search_todo(user_id: int, title: str, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.user_id == user_id).filter(Todo.title == title).all()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# modifica un attivita (titolo, descrizione, stato)
@router.put("/id", response_model=TodoSchema)
def change_todo(id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo.dict().items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo

# modifica lo stato di una attivita esistente
@router.put("/status", response_model=TodoSchema)
def change_status_todo(title: str, user_id: int, id: int, todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.title == title).filter(Todo.user_id == user_id).filter(Todo.id == id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    if todo.completed is not None:
        db_todo.completed = todo.completed

    db.commit()
    db.refresh(db_todo)
    return db_todo


# cancella una attivita che sta su stato True(1, done)
@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ID not found")

    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}


















