"""
날짜 : 2021/06/08
이름 : 김진우
내용 : 파이썬 실시간 검색어 실습하기
"""
import os
import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime

# 페이지 요청하기
response = req.get('https://issue.zum.com/')

# 페이지 출력
dom = bs(response.text, 'html.parser')
divs = dom.select('#issueKeywordList > li > div')

# 디렉터리 생성
dir = './keyword/{:%Y-%m-%d}'.format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

# 파일 생성
fname = "{:%Y-%m-%d-%H-%M.txt}".format(datetime.now())
file = open(dir+'/'+fname, mode='w', encoding='utf-8')

# 파일 저장
for issue in divs :
    iss1 = issue.find(class_='num').text
    iss2 = issue.find(class_='word').text
    file.write('%s, %s\n' %(iss1[:-1],iss2))

file.close()

print('검색어 수집 완료...')