import requests
from bs4 import BeautifulSoup

#response = requests.get('https://www.acmicpc.net/problem/tags')
#response = requests.get('https://www.acmicpc.net/problem/tags').ok
#response = requests.get('https://www.acmicpc.net/problem/tags').status_code
response = requests.get('https://www.naver.com').text

#print(response)

soup = BeautifulSoup(response, 'html.parser')

#print(soup)
# print(soup)

soup = BeautifulSoup(response, 'html.parser')
# 원하는 부분을 겨냥한다
tags = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

for x in tags:
    print(x.text)

# 200 성공
# 300 리다이렉션
# 400 뭔가 문제가 있다