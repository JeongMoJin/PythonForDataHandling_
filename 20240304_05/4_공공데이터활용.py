import csv
from typing import List

# example_file = open('./input/아파트(매매)_실거래가_20240304154554.csv')
# example_reader = csv.DictReader(example_file)
# print('출력')
# for row in example_reader:
#     print(f'{row}')
# print('=' * 20)

# 조건 : 래미안 단지만 검색
# 출력조건: 지역, 단지명, 크기, 층수, 거래금액
# 저장 파일명 : apt_2403_조건1.csv
# with로 파일 처리

new_datas: List[dict] = list()
with open('./input/아파트(매매)_실거래가_20240304154554.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row: dict
        if row['단지명'].find('래미안') != -1:
            print(f'{row["단지명"]}')
            new_data: dict = dict()
            new_data['시군구'] = row['시군구']
            new_data['단지명'] = row['단지명']
            new_data['전용면적(㎡)'] = row['전용면적(㎡)']
            new_data['층'] = row['층']
            new_data['거래금액(만원)'] = row['거래금액(만원)']
            new_datas.append(new_data)
print(new_datas)
header: list = list(new_datas[0].keys())

file_name = 'apt_2403_조건1.csv'
with open(f'./output/{file_name}', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)
print(f'{file_name}파일이 생성 되었습니다.')


# 조건 : 롯데캐슬 거래건만 검색
# 출력조건 : 구(구만 나오도록 할 것), 단지명, 전용면적, 층, 거래금액
# 저장 파일명 : apt_2403_조건3.csv
# with로 파일 처리
# 예) 달서구, 롯데캐슬레이크, 84, 91, 3, "32.109"

new_datas: List[dict] = list()
with open('./input/아파트(매매)_실거래가_20240304154554.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row: dict
        if row['단지명'].find('롯데캐슬') >= 0:
            print(f'{row["시군구"].split(" ")[1]} / {row["단지명"]}')
            new_data: dict = dict()
            new_data['구'] = row['시군구'].split(" ")[1]
            new_data['시군구'] = row['시군구']
            new_data['단지명'] = row['단지명']
            new_data['전용면적(㎡)'] = row['전용면적(㎡)']
            new_data['층'] = row['층']
            new_data['거래금액(만원)'] = row['거래금액(만원)']
            new_datas.append(new_data)
print(new_datas)
header: list = list(new_datas[0].keys())

file_name = 'apt_2403_조건2.csv'
with open(f'./output/{file_name}', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)
print(f'{file_name}파일이 생성 되었습니다.')

# 조건 : 각 구별 롯데캐슬 거래건수 검색
# 출력조건 : 구(구만 나오도록 할 것), 거래건수
# 저장 파일명 : apt_2403_조건3.csv
# with로 파일처리

import csv
from typing import List, Dict

# 중구 : 110 형태의 데이터가 필요하기때문에 dict데이터를 사용. key는 문자열, value는 정수.
new_datas: Dict[str, int] = dict()

with open('./input/아파트(매매)_실거래가_20240304154554.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row: dict
        if row['단지명'].find('롯데캐슬') >= 0:
            new_key: str = row['시군구'].split(" ")[1] # 구를 추출
            if new_key in new_datas: # 구이름의 키가 있는 경우, 기존 값 1을 더함
                new_datas[new_key] = new_datas[new_key] + 1
            else: # 구이름의 키가 없는 경우, 새로 생성 후 1을 입력
                new_datas[new_key] = 1
print(new_datas)

header: list = ['구', '거래건수']

file_name = 'apt_2404_조건3.csv'
with open(f'./output/{file_name}', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for key, value in new_datas.items():
        writer.writerow({header[0]: key, header[1]: value})
        # print([key, value])
print(f'{file_name}파일이 생성 되었습니다.')