"""
웹 크롤링 : 검색 엔진의 구축 등을 위하여 특정한 방법으로 웹 페이지를 수집하는 프로그램
웹 스크래핑 : 웹에서 데이터를 수집하는 프로그램
"""

from bs4 import BeautifulSoup
import aiohttp
import asyncio

# soup = BeautifulSoup("www.naver.com", "html.parser")

# print(soup.prettify())

# print(soup.title)

# print(soup.p)

# print(soup.find("p", "story").text)


async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        # print(html)
        cont_thumb = soup.find_all("div", "cont_thumb")
        print(cont_thumb)
        for cont in cont_thumb:
            title = cont.find("p", "txt_thumb")
            if title is not None:
                print(title.text)


async def main():
    BASE_URL = "https://bjpublic.tistory.com/category/"
    urls = [f"{BASE_URL}?page={i}" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())
