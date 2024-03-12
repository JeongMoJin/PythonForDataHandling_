import pprint
import requests
import os.path
from bs4 import BeautifulSoup as bs

# 파이썬 공식 홈페이지에서 이미지 링크 가져옴

url = 'https://www.python.org/static/img/python-logo.png'
response = requests.get(url)

# 실습 1
# 1) 파일 이름 가지고 오기
image_file_name = os.path.basename(url) # 파일 이름 가져오기
print(image_file_name) # pyhton-logo@2x.png

# 2) 파일 저장 response.content 사용
with open(f'./output_image/{image_file_name}', 'wb') as image_file:
    image_file.write(response.content)
    print('이미지 파일로 저장하였습니다.')

# 실습 2 : 할리스커피에서 태그를 이용해서 이미지 저장
url = 'https://www.hollys.co.kr/menu/espresso.do'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.prettify())

# 1) 커피이미지 태그 가져오기
image_tag = soup.select_one('#menuView1_877 > img')
print('HTML 요소: ',image_tag)
print()

# 2) 이미지 경로 가져오기
# img_source = image_tag.get('src')
img_source = image_tag.attrs['src']
print('이미지 파일 경로: ', img_source)
print()

response = requests.get('https:' + img_source)
with open('./output_image/download_image.png', 'wb') as image_file:
    image_file.write(response.content)
    print('이미지 파일로 저장하였습니다.')

# 실습 3. 야후 이미지 검색 이용
# https://www.yahoo.com/ 에서 이미지 검색을 한 후 url을 들고 올 것

# 1) 이미지 태그 가져오기
url = 'https://images.search.yahoo.com/search/images;_ylt=Awr9.uRQpOpl_XMJ.WeJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRmcgN5ZnAtdARmcjIDcDpzLHY6aSxtOnNiLXRvcARncHJpZANmcFBiY3FWRFRtLnhMQ0Izcmo4S2RBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzgEcXVlcnkDdW5pdmVyc2UEdF9zdG1wAzE3MDk4NzYzMTY-?p=universe&fr=yfp-t&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&ei=UTF-8&x=wrt'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

tag_images = soup.select('li.ld a > img')
pprint.pprint(tag_images)

# 2) 이미지 저장
dir_save = './output_image/yahoo' # 저장 경로

for idx,  tag in enumerate(tag_images):
    response = requests.get(tag.get('data-src'))
    with open(f'{dir_save}{idx + 1}.png', 'wb') as image_file:
        image_file.write(response.content)
        print(f'{idx+1}/{len(tag_images)}')

