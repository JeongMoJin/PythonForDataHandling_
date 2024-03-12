# 텍스트 파일 생성하기
file = open('./output/hello.txt', 'wt')

# hello.txt에 글 쓰기.
file.write('안녕하세요')
file.write('\n') # 줄 바꿈
file.write('반갑습니다.')
file.write('\n')
print('hello.txt 파일이 생성되었습니다.') # 진행 상황을 알기 위해서 화면 출력.

file.close()

# 2. 텍스트 파일에 내용 추가하기
# 기존 파일에 내용을 추가할 수 있는 모드는 a 모드
file = open('./output/hello.txt', 'at')

file.write('Hello. \n')
file.write('Nice to meet you. \n')
print('hello.txt 파일에 새로운 내용이 추가되었습니다.')
file.close()

# utf-8로 문서 작성하기 (인코딩을 ansi -> utf-8)
import codecs
file = codecs.open('./output/한글파일.txt', 'w', 'utf-8')
file.write('오늘 나는 학교에 갔습니다.')
file.close()
















