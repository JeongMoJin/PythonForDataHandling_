import json

string_json_data :str = '{"name": "Zopgie", "isCat" : true, "miceCaught" : 0, "felineIQ" : null}'
json_data_as_python_value = json.loads(string_json_data)
print(type(json_data_as_python_value)) # <class 'dict'>
print(json_data_as_python_value)
# {'name': 'Zopgie', 'isCat': True, 'miceCaught' : 0, 'felineIQ': None}

# 온라인에서 JSON파일 열기
import urllib.request as request
json_data = request.urlopen('https://jsonplaceholder.typicode.com/todos/1').read()
print(type(json_data)) # <class 'bytes'>
python_data = json.loads(json_data)
print(type(python_data)) # <class 'dict'>
print(python_data)
# {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

# dumps() 함수를 이용하여 JSON 작성하기
python_data: dict = {'name': 'Zopgie', 'isCat':True, 'miceCaught':0, 'felineIQ':None}
json_data : str = json.dumps(python_data)
print(type(json_data)) # <class 'str'>
print(json_data)
# {"name": "Zopgie", "isCat": true, "miceCaught": 0, "felineIQ": null}

# JSON파일의 설치목적구분의 종류를 (중복없이) 출력
import json
with open('./input/cctv.json', 'r', encoding='utf-8') as jsonfile:
    json_data = jsonfile.read()
    cctv_list = json.loads(json_data)
    cctv_purpose = set()
    for place in cctv_list:
        cctv_purpose.add(place['설치목적구분'])

print(cctv_purpose)









