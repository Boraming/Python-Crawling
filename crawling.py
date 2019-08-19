import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com').text


soup = BeautifulSoup(response, 'html.parser') #네이버 html코드
tags = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

for x in tags:
    print(x.text)
