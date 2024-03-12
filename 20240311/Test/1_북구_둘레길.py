import csv
import json
import pprint
import requests

# 1. 데이터 수집
# 서비스 키
service_key = '1wMGYoH1onj8LIYDjyTfyuVPZLQc6F31PLdZjBj6jxjEi5P5suF4F9tGV2d38RvWOUj0tpiv6/OmN0NsBd93gg=='

url = 'http://apis.data.go.kr/3450000/bukguDulleRoadService/getBukguDulleRoad'
param = f'?serviceKey={service_key}&currentPage=1&perPage=500&SN=&MNTN_NM='

response = requests.get(url, param)

json_data = response.text # HTTP 응답에서 텍스트 데이터를 추출
dict_data = json.loads(json_data) # JSON 형식의 문자열을 파이썬의 딕셔너리로 변환

# 산명으로 검색
for item in dict_data['body']:
    if item['MNTN_NM'] == '도덕산' or item['MNTN_NM'] == '함지산':
        print(item['MNTN_NM'])

# 2. 데이터 저장
item_list : list[dict] = list() # 목록을 저장할 리스트
name_list : list[str] = ['산 명', '노선', '거리', '소요시간'] # csv의 헤더 및 딕셔너리의 key값으로 사용.

for item in dict_data['body']:
    if item['MNTN_NM'] == '도덕산' or item['MNTN_NM'] == '함지산':
        new_item :dict = dict()
        new_item[name_list[0]] = item['MNTN_NM']
        new_item[name_list[1]] = item['ROUTE']
        new_item[name_list[2]] = item['DSTNC']
        new_item[name_list[3]] = item['REQRE_TIME']
        item_list.append(new_item)


with open('output/bukgu_trail.csv', 'w', newline='', encoding='UTF-8') as file:
    dict_writer = csv.DictWriter(file, name_list)
    dict_writer.writeheader()
    for data in item_list:
        dict_writer.writerow(data)