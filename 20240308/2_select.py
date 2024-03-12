import pprint

import requests
from bs4 import BeautifulSoup as bs

# 실습 1. 대구광역시 위키피디아에서 상징 > 시조 > 독수리 들고 오기
# url = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
#
# tag_symbol = soup.select_one('.mw-parser-output ul')
# print(tag_symbol)
#
# text_symbol = tag_symbol.find('a').text
# print(text_symbol) # 독수리
#
# # 실습 2. 다음 > 뉴스 > IT > 오늘의 연재 의 첫번째 글 제목과 신문사 들고오기
# url = 'https://news.daum.net/digital#1'
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
#
# tag_series = soup.select_one('.list_todayseries li')
# print(tag_series)
#
# print()
# tag_series_title = tag_series.select_one('.link_txt').text
# print(f'제목: {tag_series_title}')
#
# tag_series_press = tag_series.select_one('.txt_info').text
# print(f'신문사 : {tag_series_press}')
#
# # 실습 3. seelct_one() 메소드 이용하기
# # 할리스 커피 : 매장 검색
#
# url = 'https://www.hollys.co.kr/store/korea/korStore2.do'
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
# print(soup.prettify())
#
# # 매장 테이블 가져오기
# stores = soup.select_one('table.tb_store')
# # print(stores)
#
# first_store = stores.select_one('#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1)')
# # print(first_store)
#
# # td:nth-child(1) -> td 태그중 첫번째
# second_store_name = first_store.select_one('td:nth-child(2)')
# print(second_store_name.text)
#
# second_store_address = first_store.select_one('td:nth-child(4)')
# print(second_store_address.text)
#
# # 실습 4. select() 메소드 실습하기
#
# # select() 메소드
# # CSS selector로 지정한 태그들을 모두 가져오는 메소드. 가져온 태그들은 모두 리스트에 보관
#
# # 다음 > 뉴스 > IT > 오늘의 연재의 첫번째 글 제목과 신문사 들고오기
#
# url = 'https://news.daum.net/digital#1'
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
#
# tag_series = soup.select('.list_todayseries li')
# print(tag_series)
#
# for tag in tag_series:
#     print()
#     tag_series_title = tag.select_one('.link_txt').text
#     print(f'제목 : {tag_series_title}')
#
#     tag_series_press = tag.select_one('.txt_info').text
#     print(f'신문사 : {tag_series_press}')
#
# # 실습 5. select() 메소드 실습하기
#
# # 네이버 환률 크롤링
# # https://finance.naver.com/marketindex
#
# url = 'https://finance.naver.com/marketindex'
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')
#
# nations = soup.select('#exchangeList > li > a.head > h3 > span')
# print(nations)
#
# exchange_rates = soup.select('#exchangeList > li > a.head > div > span.value') # 환률 가져옴
# print(exchange_rates)

# 6. BeautifulSoup 실습 : select() 메소드
# 크롤링을 이용한 환률 계산기 : 다른 나라의 통화를 원으로 계산

# def get_exchange_rate(menu : int) -> float: # 원하는 환률을 가져옴
#     url = 'https://finance.naver.com/marketindex'
#     response = requests.get(url)
#     soup = bs(response.text, 'html.parser')
#     exchange_rates = soup.select('#exchangeList > li > a.head > div > span.value')
#     exchange_rate: float = float(exchange_rates[menu - 1].text.replace(',','')) # , 지우기
#     return exchange_rate
#
# print('=== 메뉴 ===')
# print('1. 미국')
# print('2. 일본')
# print('3. 유럽')
# print('4. 중국')
# print('=============')
# menu = int(input('선택 >> '))
# unit = ['달러', '엔', '유로', '위안']
# money = float(input(f'금액 입력 (단위 : {unit[menu -1]}) >> '))
#
# if menu == 2: # 일본을 선택한다면? 네이버에서는 100엔 기준 금액을 제공
#     money = money / 100
# print(get_exchange_rate(menu) * money, '원')

# 7. 실습 : select() 메소드 이용하기

# 크롤링을 이용한 환률 계산기 : 다른 나라의 통화를 원으로 계산 > 원을 다른 나라 통화로 계산으로 변경

# 함수는 그대로 사용
# def get_exchange_rate(menu : int) -> float: # 원하는 환률을 가져옴
#     url = 'https://finance.naver.com/marketindex'
#     response = requests.get(url)
#     soup = bs(response.text, 'html.parser')
#     exchange_rates = soup.select('#exchangeList > li > a.head > div > span.value')
#     exchange_rate: float = float(exchange_rates[menu - 1].text.replace(',','')) # , 지우기
#     return exchange_rate
#
# money = int(input(f'step 01) 환률 계산할 금액을 입력해주세요. (단위 :원) >> '))
# unit = ['달러', '엔', '유로', '위안']
# print('=== 메뉴 ===')
# print('1. 미국')
# print('2. 일본')
# print('3. 유럽')
# print('4. 중국')
# print('=============')
# menu = int(input('선택 >> '))
#
# if menu == 2: # 일본을 선택했다면? 네이버에서는 100엔 기준 금액을 제공
#     trans_money = money / get_exchange_rate(menu) * 100
# else:
#     trans_money = money / get_exchange_rate(menu)
# print(f'step 03) {money}원은 {unit[menu-1]}로 환전하면 {trans_money}{unit[menu-1]}입니다.')

# 8. 실습 : select() 메소드
url = 'https://finance.naver.com/marketindex'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

# select 태그에 있는 데이터를 사용

# stpe 1) 환률 데이터 들고옴. 딕셔너리(나라, 단위, 환률, 원화비율)로 저장
datas= soup.select_one('#select_to') # id 값이 select_to인 태그
# print(datas)

dict_list: list[dict] = list()
for data in datas.select('option'): # option 태그만 반복
    # print(data)
    # print(data.text)
    # print(data.get('value'))
    new_dict: dict = dict()
    nation = data.text.split(" ")[0]
    if nation == '남아프리카':
        new_dict['나라'] = ' '.join(data.text.split(" ")[0:2])
        new_dict['단위'] = ' '.join(data.text.split(" ")[2:])
    else:
        new_dict['나라'] = nation
        new_dict['단위'] = ' '.join(data.text.split(" ")[1:])
    new_dict['환률'] = data.get('value')
    new_dict['원화비율'] = data.get('label')

    dict_list.append(new_dict)

pprint.pprint(dict_list)




























