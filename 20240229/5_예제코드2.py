# 동요 '엄마돼지 아기돼지'의 가사가 저장되어 있는 '엄마돼지아기돼지.txt' 파일을 읽어서
# '꿀'이라는 글자가 몇 번 나오는지 찾는 프로그램입니다.

file = open('./input/엄마돼지아기돼지.txt', 'rt')

line_list = file.readlines() # 줄 단위로 읽어서 리스트로 반환
print(line_list)
count = 0
for line in line_list: # 줄단위 문자열 추출
    for ch in line: # 개별 문자 추출
        # print(ch)
        if ch == '꿀':
            count += 1

print(f'꿀은 전체 {count}번 나타납니다.')
