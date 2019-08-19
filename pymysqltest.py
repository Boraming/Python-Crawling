import pymysql
from selenium import webdriver
import time

#DB연결에 필요한 정보드레
conn = pymysql.connect(
    host = 'localhost',
    user='root',
    password='1234',
    db='test',
    charset='utf8'
)

cursor = conn.cursor() #데이터베이스에 연결된 객체

driver = webdriver.Chrome('C:/Users/User/Desktop/박보람/공부/2019_멋쟁이사자처럼/강의-멋사정규/0.크롤링/동적웹크롤링/chromedriver.exe')
home='https://comic.naver.com/webtoon/list.nhn?titleId=654774&weekday=mon'
driver.get(home)
time.sleep(2)

titles=driver.find_elements_by_css_selector('td.title a') #랭킹 30개 태그 긁어오기?

for title in titles:
    print(title.text)
    SQL = "INSERT INTO `table1`(`text1`, `text2`) VALUES ('%s', '%s')" % (title.text, title.get_attribute('href'))
                    # 테이블이름 , (`attribute이름`)
    cursor.execute(SQL)

conn.commit() #DB 연결 닫아주기

