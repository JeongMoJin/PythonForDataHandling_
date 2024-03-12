from bs4 import BeautifulSoup as bs

# beautifulsoup : 구문을 분석해서 필요한 내용만 추출 할 수 있는 기능을 가지고 있는 외부 패키지

with open('./7_HTML.html','r', encoding='UTF-8') as file:
    html = file.read()

soup = bs(html, 'html.parser') # html.parser : html 코드를 사용하기 쉽게 beautifulsoup의 객체로 파싱

print(type(soup)) # <class 'bs4.BeautifulSoup'>
print(soup) # html 출력

print(soup.find('title').text) # 문서의 제목
print(soup.find('div').text) # div 태그의 텍스트
print(soup.find('h1').text.strip())