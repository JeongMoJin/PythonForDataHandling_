import requests

# requests 사용법

url = 'https://www.naver.com/'
response = requests.get(url) # get() 또는 post() 메서드를 이용해서 html 정보를 받아옴

html = response.text # response 객체의 text 속성을 지정하면 html 정보 반환
print(html) # html 소스가 출력

headers = response.headers # response 객체의 headers 속성 지정하면 헤더 정보 반환
print(headers)










