from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class TodoCreate(TodoBase):
    user_id: int

class Todo(TodoBase):
    id: int
    user_id: int
