from app.config import get_secret


class NaverBookScraper:
    NAVER_API_BOOK = "https://openapi.naver.com/v1/search/book"
    NAVER_API_ID = get_secret("NAVER_API_ID")
    NAVER_API_SECRET = get_secret("NAVER_API_SECRET")

    @staticmethod
    def fetch(session, url, headers):
        pass

    def unit_rul(self, keyword, start):
        return {
            "url": f"{self.NAVER_API_BOOK}?query={keyword}$display=10&start={start}",
            "headers": {"X-Naver-Client-Id": self.N},
        }

    def search(self, keyword, total_page):
        apis = []
