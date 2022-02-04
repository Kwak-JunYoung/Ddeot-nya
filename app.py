import requests
from bs4 import BeautifulSoup
import time
import winsound

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.

updated = False

duration = 1000
freq = 400

while not updated:
    data = requests.get('https://admission.skku.edu/connect/dataroom.htm?ctg_cd=pyunip',headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    articles = (soup.select_one('#contents > article > div.tableW > table > tbody > tr.bg > td.disNo'))

    for article in articles:
        x = int(article)
        if x > 17:
            winsound.Beep(freq, duration)
            updated = True
            print("Updated!")
    time.sleep(60)