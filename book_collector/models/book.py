from odmantic import Model


# class Player(Model):
#     name: str
#     game: str


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"


# db db-name-> collection books-> document
