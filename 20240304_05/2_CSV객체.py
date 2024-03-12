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
import csv

# csv 모듈을 사용해서 csv 파일을 읽으려면 다른 텍스트 파일처럼 open() 함수로 파일을 열어야 함
example_file = open('./input/example.csv') # mode를 생략하면 rt가 기본값

# read() 대신 csv.reader() 함수에 전달. reader() 객체가 반환
example_reader = csv.reader(example_file)

# list로 변환하여 값에 접근
print(example_reader)
example_data = list(example_reader)
print(example_data)
print(example_data[0][1]) # Apples
example_file.close()

# 2. for 반복문을 이용해 reader 객체로부터 데이터 읽기
# CSV 파일이 큰 경우에는, 전체 파일을 한 번에 메모리에 로드하지 말고
# for 반복문에서 reader 객체 사용
# reader 객체는 한 번만 사용가능하기 때문에 다시 사용할려면 새로 reader 객체 생성
example_file = open('./input/example.csv')
example_reader = csv.reader(example_file)
#print(example_reader)
print('example.csv 출력')
for row in example_reader:
    # 각 행의 번호를 얻으려면 reader 객체의 line_one 변수를 사용
    print(f'Row #{str(example_reader.line_num)} {str(row)} {str(row[0])}')
example_file.close()
print('=' * 20)

# 3. writer 객체
# writer 객체를 사용하면 데이터를 csv 파일에 저장할 수 있음

output_file = open('./output/output.csv', 'w', newline='') # newline'' : 빈줄이 들어가는 것 방지
output_writer = csv.writer(output_file) # csv.writer에 전달할 객체 생성
output_writer.writerow(['spam', 'eggs', 'bacon', 'han']) # writer.writerow() : 리스트에 인자를 전달
output_writer.writerow(['hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1,2,3,3.141592,4])
output_file.close()

# 4. 키워드 인자 delimiter와 lineterminator
# 쉼표가 아닌 탭문자로 셀을 구분하고 줄 간격을 한 줄씩 띄우려는 상황을 가정
# 구분자 (delimiter)와 줄 끝 문자 (lineterminator)를 변경
# delimiter의 기본값은 쉼표이고, lineterminator의 기본값은 개행문자
# 셀들이 탭으로 구분되어 있기 때문에 탭으로 구분된 값을 의미하는 .tsv 파일 확장자 사용
csv_file = open('./output/example.tsv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
csv_writer.writerow(['apples', 'oranges', 'grapes'])
csv_writer.writerow(['eggs', 'bacon', 'ham'])
csv_writer.writerow(['spam','spam','spam','spam','spam','spam',])
csv_file.close()

# 5. CSV 객체의 DictReader와 DictWriter
# 헤더 행이 있는 csv 파일의 경우 reader나 writer 객체보다 DictReader나 DictWriter 객체를 사용하는 것이 작업하기 편함
example_file = open('./input/example_with_header.csv')
example_dict_reader = csv.DictReader(example_file)
# DictReader 객체는 1) row를 딕셔너리 객체로 설정하고, 2) 첫 번째 행에 있는 정보를 건너 뜀
# 3) 첫 번째 행에 있는 정보를 키값으로 사용
print('example_with_header.csv 출력')
for row in example_dict_reader:
    print(f'{row["Timestamp"]}, {row["Fruit"]}, {row["Quantity"]} ')
print('=' * 20)

# 헤더 정보가 없는 파일의 경우 DictReaer() 생성자의 두 번째 인자로 헤더 이름을 지어서 전달
example_file = open('./input/example_with_header.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])
print('example.csv 출력')
for row in example_dict_reader:
    print(f'{row["time"]}, {row["name"]}, {row["amount"]}')
print('=' * 20)

# DictWriter 객체는 csv 파일을 생성하기 위해 딕셔너리를 사용
output_file = open('./output/output_with_header.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
# 파일에 헤더 행을 넣고 싶으면 writeheader()를 호출
output_dict_writer.writeheader()
# writerow() 메서드를 호출하여 각 행을 쓸 수 있는데, 이 때 딕셔너리를 사용.
# 딕셔너리의 키는 헤더이고, 딕셔너리의 값은 파일에 쓰려는 데이터가 들어감
output_dict_writer.writerow({'Name' : 'Alice', 'Pet' : 'cat', 'Phone' : '555-1234'})
output_dict_writer.writerow({'Name' : 'Bob', 'Phone' : '555-9999'}) # 누란된 키는 빈 상태로 나옴
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':'dog'}) # 순서는 중요하지 않음
output_file.close()