import json
import requests

service_key : str = 'service_key'

url_tm = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getTMStdrCrdnt'
# params_tm ={'serviceKey' : service_key, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'umdName' : '대명동' }
params_tm2 =f'?umdName=대명동&pageNo=1&numOfRows=10&returnType=json&serviceKey={service_key}'
print(url_tm + params_tm2)

response = requests.get(url_tm + params_tm2)

json_data = response.text # HTTP 응답에서 텍스트 데이터를 추출
dict_data = json.loads(json_data) # JSON 형식의 문자열을 파이썬의 딕셔너리로 변환
print(dict_data)

tmX: str = ''
tmY: str = ''
for item in dict_data['response']['body']['items']:
    if item['sidoName'].find('대구') ==0:
        print(item)
        tmX = item['tmX']
        tmY = item['tmY']

# tmX = dict_data['response']['body']['items'][0]['tmX']
# tmY= dict_data['response']['body']['items'][0]['tmY']

print(tmX, tmY)

url_air = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'
# params_air ={'serviceKey' : service_key, 'returnType' : 'json', 'tmX' : '244148.546388', 'tmY' : '412423.75772', 'ver' : '1.1' }
params_air2 = f'?tmX={tmX}&tmY={tmY}&returnType=json&serviceKey={service_key}'
print(url_air + params_air2)

response = requests.get(url_air + params_air2)

json_data = response.text # HTTP 응답에서 텍스트 데이터를 추출
dict_data = json.loads(json_data) # JSON 형식의 문자열을 파이썬의 딕셔너리로 변환

print(dict_data)
for item in dict_data['response']['body']['items']:
    print(item['stationName'])

# 2. 데이터 저장
item_list : list[dict] = list() # 목록을 저장할 리스트
name_list : list[str] = ['측정소 위치']

























