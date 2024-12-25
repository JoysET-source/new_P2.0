from os.path import defpath

from fastapi import FastAPI

app = FastAPI()

@app.get("primo script")
async def root():
    return {"message": "hello world"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"hello {name}"}






