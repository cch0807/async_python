from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/hello")
def read_fastapi_hello():
    return {"hello": "Fastapi"}


@app.get("/items/{item_id}/{xyz}")
def read_item(item_id: int, xyz: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "xyz": xyz}
