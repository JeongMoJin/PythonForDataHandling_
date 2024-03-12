import urllib.request as request
import json
import datetime

# API 이용하기
# openweathermap

api_key: str = '7bcfe93058cb697de719461d5eac0e1c'

# 대구 위치 정보
city:str = 'Taegu'
url: str = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}'
# print(url)

json_data = request.urlopen(url).read()
dict_data = json.loads(json_data)
lat = dict_data[0]['lat']
lon = dict_data[0]['lon']
print(f'{lat}/{lon}')

# 현재 날씨
# https://openweathermap.org/current
# &lang=kr: 한국어 사용
# &units=metric : 섭씨 사용

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang=kr&units=metric'
print(url)
json_data = request.urlopen(url).read()
dict_data = json.loads(json_data)
json_data = json.dumps(dict_data, indent=4)
print(json_data)

print(f'도시 : {dict_data["name"]}')
print(f'현재날씨 : {dict_data["weather"][0]["description"]}')
print(f'최저기온 : {dict_data["main"]["temp_min"]}')
print(f'최고기온 : {dict_data["main"]["temp_max"]}')
print(f'일출시간 : {datetime.datetime.fromtimestamp(dict_data["sys"]["sunrise"])}')
print(f'일몰시간 : {datetime.datetime.fromtimestamp(dict_data["sys"]["sunset"])}')

# 날씨 예보 : 5 day / 3 Hour
# https://openweathermap.org/forecast5
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&lang=kr&units=metric'
json_data = request.urlopen(url).read()
dict_data = json.loads(json_data)
json_data = json.dumps(dict_data, indent=4)
print(json_data)

weather_list = dict_data['list'] # json 데이터 중에서 list key에 해당하는 목록 가져오기
print(weather_list)

for item in weather_list:
    print(f'시간: {datetime.datetime.fromtimestamp(item["dt"])}', end=',')
    print(f'최고기온: {item["main"]["temp_max"]}', end=',')
    print(f'날씨 : {item["weather"][0]["main"]}', end=', ')
    print(f'날씨 : {item["weather"][0]["description"]}')
    print()