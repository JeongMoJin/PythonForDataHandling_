import urllib.request as request

import requests

# 정상 접속
url = "https://www.python.org/"
code = request.urlopen(url)
print(code)

# 비정상 접속. 비정상일 경우 에러 발생
# url = "https://www.python.org/1"
# code = request.urlopen(url)
# print(code)

url = "https://www.python.org/"
response = requests.get(url)
print(response) # <Response [200]>. 정상적인 통신이 이루어짐

# 페이지가 없는 경우에도 에러가 발생하지 않고, Response [404]를 리턴
url = "https://www.python.org/1"
response = requests.get(url)
print(response) # <Response [404]>. 해당 페이지를 찾을 수 없음

# 응답 코드 : 서버에서 클라이언트로 보내는 코드
# 1XX : 요청을 받았고, 작업 진행 중
# 2XX : 사용자의 요청이 성공적으로 수행 됨
# 3XX : 요청은 완료 되었으나, 리다이렉션이 필요
# 4XX : 사용자의 요청이 잘못됨
# 5XX : 서버에 오류가 발생함















