import csv
import pprint

import requests
import xmltodict

# 인증키 저장
service_key : str = 'service_key'

# URL 기입
url = 'http://apis.data.go.kr/B551177/BusInformation/getBusInfo'
param = f'?serviceKey={service_key}&type=xml&area=6&numOfRows=30'

# URL 정보 불러옴
response = requests.get(url+param)

# 불러온 정보의 TEXT 정보 저장
xml_data = response.text

# XML의 텍스트 정보를 파이썬의 딕셔너리로 변환
dict_data = xmltodict.parse(xml_data)
print(dict_data)

# 가독성이 좋게 출력 해주는 pprint 출력
pprint.pprint(dict_data)

# 2. 데이터 저장

# 목록을 저장할 리스트
item_list : list[dict] = list()
# csv의 헤더 및 딕셔너리의 key값
name_list : list[str] = ['버스번호', '버스등급', '성인요금', '평일시간표', '주말시간표']

# 시간표 합치는 함수
def sort_str(string1 : str, string2 : str) -> str:
    # 기본 데이터는 문자열. 2개의 문자열을 결합하고, 공백제거 후, 리스트로 변환
    temp_list : list[str] = (string1 + ', ' + string2).replace(' ','').split(",")
    temp_list = list(set(temp_list)) # 중복 제거
    temp_list.sort() # 정렬
    return str(temp_list)[1:-1].replace("'",'')

# 출력물을 파일로 저장하는 함수
def output_csv(filename : str):
    with open(f'./output/{filename}', 'w', newline='', encoding='UTF-8') as file:
        dict_writer = csv.DictWriter(file, name_list)
        dict_writer.writeheader()
        for data in item_list:
            dict_writer.writerow(data)

# 필요한 정보를 추출하여 list에 저장 (대한항공만 추출)
# 필요 데이터 경로 파악 후 기입
for item in dict_data['response']['body']['items']['item']:
    if item['busnumber'].find('대구') != -1: # 버스번호(경유지)안에 대구가 포함되어 있을 때, 리스트에 추가 코드 실행
        new_item: dict = dict() # 딕셔너리 객체 생성
        new_item[name_list[0]] = item['busnumber']
        new_item[name_list[1]] = item['busclass']
        new_item[name_list[2]] = item['adultfare']

        # 기본 데이터는 문자열, 2개의 문자열을 결합하고, 공백제거 후, 리스트로 변환
        temp_list: list[str] = (item['t1wdayt'] + ', ' + item['t2wdayt']).replace(' ','').split(",")
        temp_list = list(set(temp_list)) # 중복 제거
        temp_list.sort() # 정렬
        new_item[name_list[3]] = str(temp_list)[1:-1].replace("'",'')

        temp_list: list[str] = (item['t1wt'] + ', ' + item['t2wt']).replace(' ','').split(",")
        temp_list = list(set(temp_list)) # 중복 제거
        temp_list.sort() # 정렬
        new_item[name_list[4]] = str(temp_list).replace("'",'').replace('[','').replace(']','')

        item_list.append(new_item)

# 가독성 좋게 pprint 출력
pprint.pprint(item_list)
print('run OK')

# 2. csv파일로 데이터 저장
output_csv('air_bus_daegu.csv')