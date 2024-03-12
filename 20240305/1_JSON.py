import json
from typing import List

dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]
    },
    {
        'name': 'alice',
        'age':21,
        'spec': [
            168.5,
            60.5
        ]
    }
]

json_string: str = json.dumps(dict_list)
print(json_string)

with open('./output/dict_list_01.json', 'w') as file:
    file.write(json_string)

print('dict_list_01.json 파일이 생성되었습니다.')

json_stirng = json.dumps(dict_list, indent=4) # indent 옵션 사용

with open('./output/dict_list_02.json', 'w') as file:
    file.write(json_string)

print('dict_list_02.json 파일이 생성되었습니다.')

with open('./output/dict_list_02.json', 'r') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)
    print(dict_list)
    print(type(dict_list)) # <class 'list'>

for dic in dict_list:
    print('이름: {}'.format(dic['name']))
    print('나이: {}'.format(dic['age']))
    print('키: {}'.format(dic['spec'][0]))
    print('몸무게: {}'.format(dic['spec'][1]))
    print()






















