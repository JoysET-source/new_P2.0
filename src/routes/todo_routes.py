from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models import Todo
from src.schemas.todo_schemas import TodoCreate, Todo as TodoSchema


router = APIRouter(prefix="/todo", tags=["todo"])

@router.post("/", response_model=TodoSchema)
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

@router.get("/{ToDo}", response_model=List[TodoSchema])
def slicing_todo():
    pass

@router.get("/{ToDo}", response_model=TodoSchema)
def search_todo():
    pass


















