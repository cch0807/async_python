from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path


from ..models import mongodb
from ..models.book import BookModel
from .book_scraper import NaverBookScraper


BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)

app = FastAPI(title="데이터 수집용", version="0.0.1")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # book = BookModel(keyword="파이썬", publisher="BJPulbic", price=1200, image="me.png")
    # print(await mongodb.engine.save(book))  # DB에 저장
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "Collector"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    keyword = request.query_params.get("q")
    if not keyword:
        return templates.TemplateResponse(
            "./index.html",
            {"request": request, "title": "collector"},
        )

    if await mongodb.engine.find_one(BookModel, BookModel.keyword == keyword):
        books = await mongodb.engine.find(BookModel, BookModel.keyword == keyword)
        return templates.TemplateResponse(
            "./index.html",
            {"request": request, "title": "collector", "books": books},
        )
    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword, 10)
    book_models = []
    for book in books:
        book_model = BookModel(
            keyword=keyword,
            discount=book["discount"],
            publisher=book["publisher"],
            image=book["image"],
        )
        book_models.append(book_model)
    await mongodb.engine.save_all(book_models)

    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "Collector", "books": books}
    )


@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    """after app shutdown"""
    mongodb.close()
