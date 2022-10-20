from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from ..models import mongodb


BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "Collector"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    print(q)
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "Collector", "keyword": q}
    )


@app.on_event("startup")
def on_app_start():
    print("start server")
    """before app starts"""
    mongodb.connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    # await mongodb.close()
    print("end server")
