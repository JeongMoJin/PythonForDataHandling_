import csv
import json
import pprint
import requests

# 1. 데이터 수집
# 서비스 키
service_key = ''

#골목 검색 URL
url_1 = 'https://www.daegufood.go.kr/kor/api/Alley.html?mode=json'

response = requests.get(url_1)
json_data_1 = response.text # HTTP 응답에서 텍스트 데이터를 추출
dict_data_1 = json.loads(json_data_1) # JSON 형식의 문자열을 파이썬의 딕셔너리로 변환
open_data = 'open_data'

# 음식점 검색 URL
url_2 = f'https://www.daegufood.go.kr/kor/api/Alley_food.html?mode=json&OPENDATA_ID={open_data}'

response = requests.get(url_2)
json_data_2 = response.text # HTTP 응답에서 텍스트 데이터를 추출
dict_data_2 = json.loads(json_data_2) # JSON 형식의 문자열을 파이썬의 딕셔너리로 변환

# 동구 명칭 OPENDATA_ID 검색
opendata_list : list[str] = list() # opendata_id를 저장할 리스트
for item in dict_data_1['data']:
    if item['FD_CS'][0:4] == '(동구)':
        opendata_list.append(item['OPENDATA_ID'])

# 2. 데이터 저장
item_list : list[dict] = list() # 목록을 저장할 리스트
name_list : list[str] = ['음식골목명', '음식점 상호', '음식점 주소']


for item in opendata_list:
    open_data = item
    # 음식점 검색 URL
    url_2 = f'https://www.daegufood.go.kr/kor/api/Alley_food.html?mode=json&OPENDATA_ID={open_data}'
    response = requests.get(url_2)
    json_data_2 = response.text  # HTTP 응답에서 텍스트 데이터를 추출
    dict_data_2 = json.loads(json_data_2)  # JSON 형식의 문자열을 파이썬의 딕셔너리로 변환
    for item_food in dict_data_2["data"]:
        new_item: dict = dict()
        new_item[name_list[0]] = item_food["FD_CS"]
        new_item[name_list[1]] = item_food["BZ_NM"]
        new_item[name_list[2]] = item_food["GNG_CS"]
        item_list.append(new_item)

pprint.pprint(item_list)
with open('output/daegufood_street.csv', 'w', newline='', encoding='UTF-8') as file:
    dict_writer = csv.DictWriter(file, name_list)
    dict_writer.writeheader()
    for data in item_list:
        dict_writer.writerow(data)