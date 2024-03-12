import csv

import requests
import pprint
import xmltodict
import xml
import pprint

with open('./input/data.xml', 'r', encoding='utf-8') as xml_file:
    dict_data = xmltodict.parse(xml_file.read(), xml_attribs=True) # xml 데이터를 딕셔너리로 변경
    print(dict_data)
    datas = dict_data['response']['body']['items']
    pprint.pprint(datas)

# 1. 대구 오페라 공연 일정 XML 파일 읽은 후 CSV로 저장

# URL 기입
url :str = 'https://www.daeguoperahouse.org/rss.php'
print(url)

# URL 정보 불러옴
response = requests.get(url)

# 불러온 정보의 TEXT 정보 저장
xml_data = response.text

# XML의 텍스트 정보를 파이썬의 딕셔너리로 변환
dict_data = xmltodict.parse(xml_data)
print(dict_data)

# 가독성이 좋게 출력을 해주는 pprint 출력
pprint.pprint(dict_data)


# 2. 데이터 저장
item_list : list[dict] = list() # 목록을 저장할 리스트
name_list : list[str] = ['제목', '링크'] # csv의 헤더 및 딕셔너리의 key값

# 필요한 정보를 추출하여 list에 저장
for item in dict_data['rss']['channel']['item']:
    new_item: dict = dict()
    new_item[name_list[0]] = item['title']
    new_item[name_list[1]] = item['link']
    item_list.append(new_item)

pprint.pprint(item_list)

# list 내용을 csv 파일로 저장
with open('./output/daegu_opera_240306.csv', 'w', newline='', encoding='UTF-8') as file:
    dict_writer = csv.DictWriter(file, name_list)
    dict_writer.writeheader()
    for data in item_list:
        dict_writer.writerow(data)