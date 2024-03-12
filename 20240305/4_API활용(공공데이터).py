import urllib.request as request
import json
import datetime

# 대구광역시_맛집
# 공공데이터 포탈에서 '대구광역시_맛집' 검색 (키사용이 없음)
# https://www.data.go.kr/data/15057236/openapi.do
# 중구의 맛집 목록을 json 타입으로 받아서 처리

# 1. 음식카테고리 출력
# {'한식', '일식', '세계요리', '중식', '전통차/커피전문점', '특별한 술집', '디저트/베이커리', '양식'}

# 2. 일식의 음식점명, 연락처, 메뉴 출력
# --------------------
# 음식점명: 종로초밥
# 연락처: 053-252-0321
# 메뉴: 광어회 50,000원 <br />모둠회 40,000원 <br />무침회 20,000원<br />
# --------------------
# 음식점명: 삼삼구이초밥
# 연락처: 053-425-3392
# 메뉴: 회덮밥 9,000원 <br />미주구리 30,000원 <br />점심특선 6,000원<br />
# --------------------

url : str = 'https://www.daegufood.go.kr/kor/api/tasty.html?mode=json&addr=%EC%A4%91%EA%B5%AC'
json_data = request.urlopen(url).read()
dict_data = json.loads(json_data)
print(json_data)

# csv 파일로 저장
# 파일명 : daegu_food_joongu_list.csv
# 인코딩 : utf-8
# 헤더 : '음식카테고리', '음식점명', '연락처', '메뉴'

food_list : list[dict] = list() # 일식 목록을 저장할 리스트
name_list : list[str] = ['음식카테고리', '음식점명', '연락처', '메뉴'] # csv의 헤더 및 딕셔너리의 key값으로 사용.

for data in dict_data['data']:
    if data['FD_CS'] == '일식':
        new_data: dict = dict()
        new_data[name_list[0]] = data['FD_CS']
        new_data[name_list[1]] = data['BZ_NM']
        new_data[name_list[2]] = data['TLND']
        new_data[name_list[3]] = data['MNU']
        food_list.append(new_data)

import csv
with open('./output/daegu_food_joongu_list.csv', 'w', newline='', encoding='UTF-8') as file:
    dict_writer = csv.DictWriter(file, name_list)
    dict_writer.writeheader()
    for data in food_list:
        data: dict
        dict_writer.writerow(data)







