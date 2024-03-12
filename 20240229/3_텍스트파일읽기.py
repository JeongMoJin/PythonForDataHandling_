# 텍스트 파일 읽기

# 1) read() 메소드
# file.read(size)
# 파일로부터 데이터를 읽어 들이는 메소드
# 텍스트 모드의 바이너리 모드에서 다른 방식으로 동작

# 반환값 : 텍스트 모드 | 읽어 들인 문자열, 바이너리 모드 | 읽어 들인 바이트열
# 매개변수 size : 텍스트 모드 | 읽어 들일 최대 문자의 개수, 바이너리 모드 | 읽어 들일 최대 바이트 수
# 매개변수 size 생략 : 파일 전체 읽음
# 파일의 끝에 도달 : 빈 문자열 ('') 반환
file = open('./input/hello.txt', 'rt')

str = file.read() # 파일 전체를 한 번에 읽어 들임
print(str, end='')

file.close()

# 2) readline() 메소드
# 텍스트 파일을 한 줄씩 읽어서 처리하는 메소드
# 파일이 종료되어 더 이상 읽어 들일 글자가 없으면 빈 문자열('')을 읽어 들임
# 반복문을 이용해서 여러 번 읽어 들어야 파일 전체를 읽어 들일 수 있음
print()
file = open('./input/hello.txt', 'rt')

while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')

file.close()

# 3) readlines() 메소드
# 라인 line 하나가 아니라 전체 라인 lines을 모두 읽어 각 라인 line 단위로 리스트에 저장하는 메소드
print()
file = open('input/hello.txt', 'rt')

line_list = file.readlines()
print(line_list) # ['안녕하세요.\n', '반갑습니다.\n', 'Hello.\n', 'Nice to meet you.\n']
for line in line_list:
    print(line, end='')

file.close()

# enumrate() 함수를 이용하면 라인 번호 line number 도 함께 출력할 수 있슴
print()
file = open('input/hello.txt', 'rt')

line_list = file.readlines()
for no, line in enumerate(line_list):
    print('{} {}'.format(no + 1, line), end='')

file.close()

# sys 모듈을 이용하면 보다 쉽게 파일을 읽을 수 있슴
# sys 모듈에는 표준 입출력을 위한 stdin과 stdout 객체가 포함
# stdout은 출력을 위한 객체이며 화면 출력 메소드인 write()와 writelines() 메소드를 사용할 수 있슴
# writelines() 메소드를 사용하면 리스트와 같은 반복 가능한 객체의 각 요소를 한 줄씩 자동으로 출력
print()
import sys

file = open('input/hello.txt', 'rt')

line_list = file.readlines()
sys.stdout.writelines(line_list)

file.close()