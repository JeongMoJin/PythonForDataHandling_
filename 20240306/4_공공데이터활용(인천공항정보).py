import csv
import pprint

import requests
import xmltodict

# 인증키 기입
service_key :str = 'service_key'
# URL 기입
url = 'http://apis.data.go.kr/B551177/StatusOfPassengerFlightsDSOdp/getPassengerDeparturesDSOdp'
param = f'?serviceKey={service_key}&type=xml&airline=대한항공'

# URL 정보 불러옴
response = requests.get(url+param)

# 불러온 정보의 TEXT 정보 저장
xml_data = response.text

# XML의 텍스트 정보를 파이썬의 딕셔너리로 변환
dict_data = xmltodict.parse(xml_data)
print(dict_data)

# 가독성이 좋게 출력을 해주는 pprint 출력
pprint.pprint(dict_data)

# 2. 데이터 저장
item_list : list[dict] = list() # 목록을 저장할 리스트
# csv의 헤더 및 딕셔너리의 key값
name_list : list[str] = ['항공사', '출발지공항', '스케줄타임']

# 필요한 정보를 추출하여 list에 저장 (대한항공만 추출)
for item in dict_data['response']['body']['items']['item']: # 필요데이터 위치 경로 파악
    if item.get('airline'): # item 딕셔너리 안에 'airline' key 값이 있을 경우 아래 아래 코드 실행
        if item['airline'][0:2] == '대한': # 항공사의 앞 두글자가 '대한'일 때, 아래 코드 실행
            new_item: dict = dict() # 딕셔너리 객체 생성
            new_item[name_list[0]] = item['airline'] # 딕셔너리 안에 name_list 리스트의 0번 인덱스에 airline 값들 저장
            new_item[name_list[1]] = item['airport'] # 딕셔너리 안에 name_list 리스트의 1번 인덱스에 airport 값들 저장
            new_item[name_list[2]] = item['scheduleDateTime'] # 딕셔너리 안에 name_list 리스트의 2번 인덱스에 scheduleDateTime 값들 저장
            item_list.append(new_item) # 각각의 리스트 들을 item_list라는 큰 리스트에 저장

# 가독성 좋게 pprint 출력
pprint.pprint(item_list)

# list 내용을 csv 파일로 저장
with open('./output/incheon_air_daehan_start.csv', 'w', newline='', encoding='UTF-8') as file:
    dict_writer = csv.DictWriter(file, name_list)
    dict_writer.writeheader()
    for data in item_list:
        dict_writer.writerow(data)

# 공공데이터활용(에어코리아), 공공데이터활용(근접측정소), XML, 공공데이터활용(인천공항)
