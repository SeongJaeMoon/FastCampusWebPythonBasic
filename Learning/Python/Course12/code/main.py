import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.fastcampus.co.kr/dev_online_introdev/#row_course"

# div.vc_toggle_content > ul > li
rq = requests.get(URL)
soup = bs(rq.content, 'html.parser')

# (class, id, ...), attrs = {key : value, ...}
li_list = soup.find_all('div', class_ = 'vc_toggle_content')
# li_list -> 4개의 모든 강의 내용, 강의 과제
for li in li_list:
    ul = li.select('ul > li')
    for l in ul:
        print(l.get_text())

