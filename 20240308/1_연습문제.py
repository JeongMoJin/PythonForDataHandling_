import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : find_all() 메소드 이용하기

# 다음 뉴스에서 제목, 링크, 뉴스 본문 추출하기

# 다음 뉴스에서 제목, 링크, 뉴스 본문 추출해서 파일로 저장하기
# 1) 이전 예제를 활용할 것
# 2) 링크를 추출한 for 안에서 제목을 추출
# 3) 뉴스 본문은 링크를 이용
# 4) 링크를 타고 뉴스 본문을 들고 와야 되니
# for문 안에서 requests, BeautifulSoup가 실행이 되어야 함
# 5) 제목, 링크, 뉴스 순으로 csv 저장

# 기사 모으기
url = 'https://news.daum.net/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.prettify())

tags = soup.find_all('div', {'class' : 'item_issue'})
# print(len(tags)) # 20

for tag in tags:
    title : str = tag.find_all('a')[1].text.strip()
    link: str = tag.find_all('a')[1].get('href')

    print(f'title: {title}, link : {link}')

    response = requests.get(link)
    soup = bs(response.text, 'html.parser')
    print(soup.find('div',{'class' : 'article_view'}).text.strip())

    print('-' * 20)


















