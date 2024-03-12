# 오늘의 스케줄을 입력하면 그 내용이 모두 파일에 보관되는 프로그램입니다.
# 스케줄을 입력하지 않고 enter를 누르면 프로그램은 종료됩니다.
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt입니다.
# '2024-02-29.txt'와 같은 형식을 갖추고 있습니다.

import time

file = open(f'./output/{time.strftime("%Y-%m-%d")}.txt', 'at')

while True:
    schedule = input('오늘의 스케줄을 입력하세요 >>> ')
    if not schedule:
        break
    file.write(schedule + '\n')

file.close()

# 파이썬 버전이 올라가면서 open()에서도 utf-8 지원
file = open('./output.txt', 'w', encoding='utf-8')
file.write('오늘 나는 학교에 갔습니다.')
file.close()