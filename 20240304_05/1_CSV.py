# CSV 파일 입출력

# 1. CSV 파일이란

# 쉼표로 구분된 값 comma-separated values를 의미
# 일반 텍스트 파일처럼 저장된 간단한 스프레드 시트
# 파이썬의 csv 모듈로 CSV 파일을 쉽게 구문 분석 가능

# 각 줄은 스프레드 시트의 행을 의미하고, 쉼표는 행에서 셀을 구분하는 용도로 사용

# * 단점
# 값에 유형이 없음. 모든 것은 다 문자열
# 글꼴 크기나 색상을 지정할 수 없음
# 여러 개의 워크시르틀 가질 수 없음
# 셀의 너비나 높이를 지정할 수 없음
# 셀을 병합할 수 없음
# 그림이나 차트를 포함 할 수 없음

# * 장점
# 단순함
# 많은 프로그램에서 지원을 하고, 텍스트 편집기에서 볼 수 있으며, 스프레드 시트 데이터를 표현하는 간단한 방법

# * 주의점
# 텍스트로 구성이 되어 있어서, 각 줄에 대해 split(',')을 호출하여 쉼표로 구분된 값에서 문자열 리스트를 얻을 수 있음
# 그러나 CSV 파일의 모든 쉼표가 두 셀의 경계를 나타내지 않고, 값의 일부인 경우도 있음
# 이런 잠재적인 문제 때문에 CSV 파일을 읽거나 쓸 때 CSV 모듈을 사용하는 것이 좋음

# 1. reader 객체
# csv 모듈은 별도의 설치없이 사용가능

# Comma Separated Values 의 약자로, '쉼표로 분리한 값들'
# db나 스프레드시트 데이터를 저장하기 위해 사용하는 형식
# 내부는 실제 쉼표(,)를 사용하여 모든 항목이 구분되어 있으며 쉼표로 구성된 각 항목들이 테이블을 구성하는 각각의 데이터가 되는 방식
# 메모장에서는 텍스트로, 엑셀에서는 각 셀로 나누어서 보인다
#
# UTF - 8 형식으로 저장된 CSV 의 경우, 엑셀에서는 버전에 따라서 기본읽기로는 한글이 깨지는 경우가 있다
# 한컴 Cell 에서는 에러없이 잘 열린다.

# CSV 파일은 쉼표로 데이터가 구분되어 있어 문자열 처리 메소드를 화용하면
# 별도의 외부 모듈이 없어도 충분히 읽을 수있다:
# 1. 한줄에 한 데이터가 있으므로 readline() 메소드로 한 줄씩 읽는다
# 2. 쉼표로 분리하기 위해 split() 메소드 이용

student_list = []
with open('./input/학생명단.csv', 'rt') as file:
    file.readline()  # 학번 이름 주소 연락처
    while True:
        line = file.readline()
        if not line:  # 더 이상 읽을 내용물이 없으면 반복문을 빠져나온다.
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)

# CSV 파일을 사용할 때 큰 따옴표를 이용해서 텍스트를 묶는다.
# 큰 따옴표를 제거하기 위해 회원명에 추가로 strip() 메소드 사용.
member_list = []
with open('./input/회원명단.csv', 'rt') as file:
    file.readline()  # 학번 이름 주소 연락처
    while True:
        line = file.readline()
        if not line:  # 더 이상 읽을 내용물이 없으면 반복문을 빠져나온다.
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        # member[0].strip('"') 으로 큰 따옴표 제거
        # member[0] 에는 큰 따옴표가 포함된 회원명이 저장되어 있으므로
        # 위와 같은 형식으로 작업할 경우 아래와 같이 추가적인 따옴표 발생.
        # [['"강나라"', '필라테스', '25일\n'], ['"나유라"', '수영', '25일\n'], ['"이상기"', '헬스', '15일\n']]
        member_list.append(member)
print(member_list)

# member[0]에는 큰 따옴표가 포함된 회원명이 저장되어 있기 때문에 member[0].strip('"')으로
# 큰 따옴표를 제거

# 영어는 문제가 없는데 한글의 경우 표현하는 방식이 2가지
# cp949 : 윈도우의 기본 인코딩. 예전 방식. 한글에만 특수화된 한국에서만 사용. 모든 한글을 표현하지 못함.
# utf-8 : 파이참의 기본 인코딩. 상대적으로 새로운 방식. 한글 및 기타 외국이 문자를 하나의 인코딩으로 모두 표현하기 개발

import csv

# w모드로 열고 생성된 파일 객체를 csv, writer() 메소드에 전달
# 그러면 CSV 파일을 생성할 수 있는 객체가 생성되는데 이 객체를 이용해서
# writerow() 메소드를 호출하면 csv 파일에 데이터를 저장할 수 있슴

with open('./output/차량관리_01.csv', 'w') as file:
    # delimiter = ',':
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08라1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
print('차량관리_01.csv 파일이 생성되었습니다.')

# 불필요한 라인이 하나씩 추가되어 있는데 이를 막기 위해서 새로운 라인을
# 추가하지 못하도록 newline 옵션을 사용할 수 있음
# 줄 바꿈이 되지 않도록 newline 옵션에 빈 문자열을 지정하고 이를 코드에 반영

import csv

with open('./output/차량관리_02.csv', 'w', newline='') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08라1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
print('차량관리_02.csv 파일이 생성되었습니다.')

# csv 모듈로 CSV 파일 읽기

# CSV 파일을 읽기 위해서는 r모드로 파일을 열고 생성된 파일 객체를 csv.reader() 메소드에 전달
# csv.reader() 메소드는 CSV파일을 읽고 그 내용을 읽고 저장한 객체 iterator를 반환

with open('./output/차량관리_02.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    for line in csv_reader:
        print(line)
















