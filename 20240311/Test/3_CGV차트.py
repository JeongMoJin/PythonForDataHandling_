import pprint
import requests
from bs4 import BeautifulSoup as bs
from requests import Response

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
response = requests.get(url)
soup = bs(response.text, 'html.parser')


# 순위, 제목, 개봉일, 예매율, 이미지 저장

# 데이터베이스 생성 쿼리

# CREATE DATABASE `movie_chart`
#
# CREATE TABLE `movie_chart` (
# 	`movie_name` VARCHAR(50) NULL',
# 	`movie_start_day` VARCHAR(20) NULL',
# 	`movie_percent` VARCHAR(20) NULL'
# )


print(f'순위 / 제목 / 개봉일 / 예매율 / 포스터')
dict_list = list()
for idx, item in enumerate(soup.select('body ol li')):
    if idx == 19:
        break
    print(f'순위: {item.select_one(".rank").text.strip()}')
    print(f'제목: {item.select_one(".title").text.strip()}')
    print(f'개봉일: {item.select_one(".txt-info strong").text.replace(" ", "").strip()}')
    print(f'예매율: {item.select_one(".percent span").text.strip()}')
    print(f'포스터: {item.select_one(".thumb-image").get("src")}')


    new_data = dict()
    new_data['순위'] = item.select_one(".rank").text.strip()
    new_data['제목'] = item.select_one(".title").text.strip()
    new_data['개봉일'] = item.select_one(".txt-info strong").text.replace(" ", "").strip()
    new_data['포스터'] = item.select_one(".thumb-image").get("src")

    # INSERT 쿼리
    print(f'INSERT INTO `movie_chart`.`movie_chart` (`movie_name`, `movie_start_day`, `movie_percent`) VALUES '
          f'({item.select_one(".title").text.strip()},{item.select_one(".txt-info strong").text.replace(" ", "").strip()},{item.select_one(".percent span").text.strip()});')
