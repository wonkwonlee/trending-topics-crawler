"""
멋쟁이 사자처럼 "[심화] 같이 푸는 PYTHON" 강좌를 기반으로 만든 웹 크롤러
2021.03.10

request.RESPONSE: https://requests.readthedocs.io/en/master/api/#requests.Response
"""
import requests  # requests: put, get, post, delete
from bs4 import BeautifulSoup  # BeautifulSoup(데이터, 파싱방법)
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# url = "http://www.daum.net"       # Daum
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"        # Naver Datalab

# response = requests.get(url)      # Daum
response = requests.get(url,headers=headers)        # Naver Datalab
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

# print(soup.title)               # Title tag
# print(soup.title.string)        # String data of title tag
# print(soup.span)                # First span tag
# print(soup.findAll('span'))     # All span tags in HTML

# results = soup.findAll("a", "link_favorsch")      # Daum
results = soup.findAll("span", "item_title")        # Naver Datalab

search_rank_file = open("rankresult2.txt", "a")  # r: 읽기 전용, w: 쓰기 전용, a: 덧붙이기 전
search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n\n"))

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank) + "위 " + result.get_text() + "\n")
    print(rank, "위 ", result.get_text(), "\n")
    rank += 1

search_rank_file.close()
