import pprint

import requests
from bs4 import BeautifulSoup as bs
#
# # beautifulsoup 실습 : find() 메소드 이용하기
#
# # 1) find 메소드
# # 지정된 태그들 중에서 가장 첫 번째 태그만 가져오는 메소드(하나의 값만 반환), 문자열 형태로 반환
# # 일반적으로 하나의 태그만 존재하는 경우에 사용. 만약 여러 태그가 있으면 첫 번째 태그만 가져옴
#
# # 위키피디아 '대구광역시' 페이지
# url = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
#
# first_img = soup.find('img') # img 태그 중에 제일 먼저 나오는 것
# print(type(first_img))
# print(first_img)
#
# target_img = soup.find(name='img', attrs = {'alt': 'Deadongyeonjido (Gyujangek) 17-02.jpg'})
# print(target_img)
#
# # 2) find_all() 메소드 이용하기
# # 지정한 태그들을 모두 가져오는 메소드. 가져온 태그들은 모두 리스트에 보관
#
# # 네이버 스포츠 페이지에서 박스 뉴스 제목 들고 옴
#
# url = 'https://sports.news.naver.com/index.nhn'
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')
#
# # today_list = soup.find('ul',{'class': 'today_list'}).find_all('strong', {'class', 'title'})
# today_list = soup.find('ul',{'class':'today_list'})
# # print(today_list)
#
# today_list_title = today_list.find_all('strong', {'class', 'title'})
# pprint.pprint(today_list_title)
#
# for title in today_list_title:
#     print(title.text.strip()) # 양쪽 공백 없애는 메서드 strip()

# 3) find_all() 메소드 이용하기

# # 다음 뉴스
# url = 'https://news.daum.net/'
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')
#
# # a 태그의 갯수 출력
# print('1. a 태그의 갯수')
# print(len(soup.find_all('a')))
# print()
#
# # a 태그 20개만 출력
# # print('2. a 태그 20개만 출력')
# # for news in soup.find_all('a')[:20]:
# #     print(news.text)
#
# # a 태그 링크 5개 출력
# print('3. a 태그 링크 5개 출력')
# for i in soup.find_all('a')[:5]:
#     print(i.attrs['href'])
#     print(i.get('href'))
# print("=" * 20)
#
# # 특정 클래스 속성을 출력하기
# # print('4. 특정 클래스 속성을 출력')
# # print(soup.find_all('div', {'class': 'item_issue'}))
# # print("=" * 20)
#
# # 4. 링크를 텍스트 파일로 저장
# print('5. 링크를 텍스트 파일로 저장')
# file = open('./output/links.txt', 'w') # 쓰기 전용 파일 생성
#
# for i in soup.find_all('div', {'class': 'item_issue'}):
#     file.write(i.find('a').get('href') + '\n')
# file.close()
#
# # 문제 : with사용. 뉴스 타이틀 추출. 파일명은 news_title.txt
# # 넘버링 붙도록 예) 1. title~
#
# # 5. 타이틀을 파일로 저장
# with open('./output/news_title.txt', 'w', encoding='utf-8') as file:
#     for i, news in enumerate(soup.find_all('div', {'class':'item_issue'})):
#         file.write(f'{i+1}.{news.find_all("a")[1].text.strip()}\n')
#         print('*' * 20)


# 6. find_all() 메소드 이용하기

# 네이버 뉴스 : IT/과학에서 오른쪽 섹션의 언론사별 가장 많이 본 뉴스 제목 들고오기

url = 'https://news.naver.com/section/105'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)

section_list = soup.find('ul', {'class': 'ranking_list'})
# print(section_list)
for section in section_list:
    news_list = section.find_all('p', {'class': 'rl_txt'})
    for i in news_list:
        print(i.text)
    print()


# news_list = section_list.find_all('p', {'class': 'rl_txt'})
# pprint.pprint(news_list)

# for news in news_list:
#     print(news.text)











