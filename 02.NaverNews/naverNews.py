# naverNews.py

import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent" : "Seoul Gangseo Campus of Korea Polytechnics College, Dept. of Data Analysis / Python Education"
}

webpage = requests.get("https://entertain.naver.com/read?oid=009&aid=0004968578",
                       headers=header)

soup = BeautifulSoup(webpage.content, "html.parser")

naver_news = soup.select_one("#articeBody").get_text().strip()

print(naver_news)