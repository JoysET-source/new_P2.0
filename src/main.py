from fastapi import FastAPI
from src.routes import router
from src.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("main")
async def root():
    return {"message": "Welcome to User Management API"}










