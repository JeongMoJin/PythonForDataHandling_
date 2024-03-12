import pprint
import requests
from bs4 import BeautifulSoup as bs
from requests import Response


# 멜론차트 가져오기
# user-agent를 확인해서 bot의 접근을 막음.
# 1) user-agent를 변경해서 결과 값을 가지고 올 것
# 2) 구현 후에 이 부분을 함수화 할 것

def requests_get(url: str) -> Response:
    request_headers: dict = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/122.0.0.0 Safari/537.36'),

        'Referer': '',
    }
    return requests.get(url, headers=request_headers)


url = 'https://www.melon.com/chart/'
response = requests_get(url)
soup = bs(response.text, 'html.parser')
# print(soup)
# html 문서에 table 태그가 하나만 있음
pprint.pprint(soup.select('table tbody tr')[0])

# 순위, 곡제목, 가수를 csv로 저장
# 파일명 melon_chart.csv

print(f'제목 / 아티스트 / 앨범')
dict_list = list()
for idx, item in enumerate(soup.select('table tbody tr')):
    print(f'{idx + 1}')
    print(f'곡제목: {item.select_one(".rank01").text.strip()}')
    print(f'가수: {item.select_one(".rank02 a").text.strip()}')
    print(f'앨범: {item.select_one(".rank03").text.strip()}')
    print(f'앨범이미지: {item.select_one("td:nth-child(4) img").get("src")}')

    new_data = dict()
    new_data['순위'] = idx + 1
    new_data['곡제목'] = item.select_one('div.rank01').text.strip()
    new_data['가수'] = item.select_one('div.rank02 a').text.strip()
    new_data['앨범'] = item.select_one('div.rank03').text.strip()
    dict_list.append(new_data)

    response = requests_get(item.select_one("td:nth-child(4) img").get("src"))
    with open(f"./output_image/melon/{new_data['순위']}_{new_data['곡제목']}_{new_data['가수']}.jpg", 'wb') as image_file:
        image_file.write(response.content)






























