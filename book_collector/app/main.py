from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path


from ..models import mongodb
from ..models.book import BookModel
from .book_scraper import NaverBookScraper


BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # book = BookModel(keyword="파이썬", publisher="BJPulbic", price=1200, image="me.png")
    # print(await mongodb.engine.save(book))  # DB에 저장
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "Collector"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    keyword = q
    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword, 10)

    # for book in books:
    #     book_model = BookModel(
    #         keyword=keyword,
    #         price=book["price"],
    #         publisher=book["publisher"],
    #         image=book["image"],
    #     )
    # print(book_model)
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "Collector", "keyword": q}
    )


@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    mongodb.close()
