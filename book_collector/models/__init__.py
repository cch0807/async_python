from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from book_collector.app.config import MONGO_URL, MONGO_DB_NAME


# client = AsyncIOMotorClient(MONGO_URL)
# engine = AIOEngine(motor_client=client, database=MONGO_DB_NAME)


class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.engine = AIOEngine(self.client, database=MONGO_DB_NAME)
        print("DB 연결 성공")

    def close(self):
        self.client.close()
        print("DB 연결 해제")


mongodb = MongoDB()
