import requests
from bs4 import BeautifulSoup as bs

#헤더 정보 확인
url = 'https://planet-trade.kr/header_info.php'

# 1. requests를 이용해서 접속을 하면, 브라우저의 정보 (User-Agent)가 requests의 모듈 정보로 나옴
# 서버에서 해당 정보를 보고 크롤링을 판단할 수 있음
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup)
# 접속 IP : 58.149.46.252
# 접속 정보 : python-requests/2.31.0

# 2. requests에서 헤더 정보를 변경할 수 있음
request_headers = {
    'Uesr-Agent' : ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'),
    'Referer' : '',
}
resp = requests.get(url, headers=request_headers)
soup = bs(resp.text, 'html.parser')
print(soup)



