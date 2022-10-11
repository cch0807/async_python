import requests  # F401
import time
import aiohttp
import asyncio
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


async def main():
    urls = ["https://naver.com", "https://instagram.com"] * 50

    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        # result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # print(result)
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
