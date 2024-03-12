import json
import csv
import requests

# 1. 데이터 수집
# 서비스 키
service_key :str = 'service_key'

url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'
param_str : str = f'?addr=대구&pageNo=1&numOfRows=30&serviceKey={service_key}&returnType=json'

response = requests.get(url + param_str)

json_data = response.text # HTTP 응답에서 텍스트 데이터를 추출
dict_data = json.loads(json_data) # JSON 형식의 문자열을 파이썬의 딕셔너리로 변환
print(dict_data)

for item in dict_data['response']['body']['items']:
    if item['addr'][0] in '대구':
        print(item['addr'])

# 2. 데이터 저장
item_list : list[dict] = list() # 목록을 저장할 리스트
name_list : list[str] = ['측정소 명', '측정소 주소', '위도', '경도', '설치년도'] # csv의 헤더 및 딕셔너리의 key값으로 사용.

for item in dict_data['response']['body']['items']:
    if item['addr'][0:2] == '대구':
        new_item: dict = dict()
        new_item[name_list[0]] = item['stationName']
        new_item[name_list[1]] = item['addr']
        new_item[name_list[2]] = item['dmX']
        new_item[name_list[3]] = item['dmY']
        new_item[name_list[4]] = item['year']
        item_list.append(new_item)

print(item_list)
with open('./output/daegu_air_list.csv', 'w', newline='', encoding='UTF-8') as file:
    dict_writer = csv.DictWriter(file, name_list)
    dict_writer.writeheader()
    for data in item_list:
        dict_writer.writerow(data)