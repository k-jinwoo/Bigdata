"""
날짜 : 2021/06/08
이름 : 김진우
내용 : 가상브라우저를 활용한 크롤링 실습하기
"""

from selenium import webdriver

# 크롬 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('http://naver.com')

# 로그인 버튼 클릭
btn_login = browser.find_element_by_css_selector('#account > a')
btn_login.click()

# 아이디, 비밀번호 입력
input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_css_selector('#pw')
input_id.send_keys('asdf')
input_pw.send_keys('1234')

# 로그인 버튼 클릭
btn_login2 = browser.find_element_by_css_selector('#log\.login')
btn_login2.click()

# 가상 브라우저 종료
browser.close()