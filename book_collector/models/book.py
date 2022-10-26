from odmantic import Model


# class Player(Model):
#     name: str
#     game: str


class BookModel(Model):
    keyword: str
    price: int
    publisher: str
    image: str

    class Config:
        collection = "books"


# db db-name-> collection books-> document
