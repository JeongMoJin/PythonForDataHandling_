# 다음 지시사항에 따라 서울특별시 마포구에 설치된 CCTV의 개수를 구하는 프로그램을 구현하세요.
#
# 지시사항
# 1. cctv.csv 파일을 읽습니다.
# 2. 모든 라인에 존재하는 카메라 개수를 합한 결과를 출력합니다.
# 5번째 데이터가 카메라 대수 입니다.
#
# 실행 예 :
# 서울특별시 마포구에 설치된 CCTV는 총 2167대입니다.


# DictReader 이용할 것

import csv

with open('./input/cctv.csv', 'r') as file:
    datas = csv.DictReader(file) # dict로 읽음
    total_cctv = 0 # 카메라 대수를 저장하기 위한 변수
    for data in datas:
        total_cctv += int(data['카메라대수']) # value가 문자열이여서 형변환을 해야함

print(f'서울특별시 마포구에 설치된 CCTV는 총 {format(total_cctv, ",")}대입니다.')


# 개발절차
# 1. pop_seoul.csv 파일을 읽어서 딕셔너리로 출력
# 2. 반복문을 돌려서 한 행씩 출력
# 3. 한 행씩 출력하는 코드에서 외국인 비율을 구해서 출력
# 4. 조건애 해당하는 데잍

import csv

# 1. pop_seoul.csv 파일을 읽어서 딕셔너리로 출력
example_file = open('./input/pop_seoul.csv')
example_dict_reader = csv.DictReader(example_file) # dict 형식으로 파일을 읽기
print(list(example_dict_reader))
example_file.close()

# 2. 반복문을 돌려서 한 행씩 출력
example_file = open('./input/pop_seoul.csv')
example_dict_reader = csv.DictReader(example_file) # dict 형식으로 파일을 읽기
# print(list(example_dict_reeader))
for row in example_dict_reader:
    print(row)
example_file.close()

# 3. 한 행씩 출력하는 코드에서 외국인 비율을 구해서 출력
# 외국인 비율 : 외국인 / 총 인구수(한국인 + 외국인) * 100

import csv
new_datas: list = []
with open('./input/pop_seoul.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # 외국인 비율 : 외국인 / 총 인구수(한국인 + 외국인) * 100
        # 구별 총 인구수 출력 : 데이터가 문자열이라서 콤마(,)를 제거해야 정수로 형변환 가능
        total_population = int(row['Korean'].replace(',','')) + int(row['Foreigner'].replace(',',''))
        print(f'{row["Gu"]}의 총 인구수 : {total_population}')

        # 외국인 비율
        rate_foreigner: float = int(row['Foreigner'].replace(',','')) / total_population * 100
        print(f'{row["Gu"]}의 외국인 비율: {rate_foreigner}')

        if rate_foreigner >= 3.0:
            new_data: dict = dict()
            new_data['Gu'] = row['Gu']
            new_data['Korean'] = row['Korean']
            new_data['Foreigner'] = row['Foreigner']
            new_data['Rate'] = round(rate_foreigner, 1)
            new_datas.append(new_data)

print(new_datas)

with open('./output/pop_seoul.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Gu', 'Korean', 'Foreigner', 'Rate'])
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)


















