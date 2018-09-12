# Python 크롤러4 - 데이터 분석 및 저장
키워드 : [웹 크롤러](https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%81%AC%EB%A1%A4%EB%9F%AC)

[지난 내용](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Python/Course13/)에 이어서 파이썬 크롤러 개발 네 번째 내용이자, 우리 강의의 마지막 내용을 정리하도록 하겠습니다. (거의 다 왔습니다!) 지난 내용에서까지의 내용을 종합하면,

1. HTML을 분석
2. 요소를 추출
3. 요소의 콘텐츠만 추출

위 세 단계까지 진행했다고 할 수 있습니다. 이번 장에서는, 불러온 웹 자원을 엑셀 파일에 저장하는 코드와 말뭉치를 분석하는 코드 등의 추가 내용을 작성해보도록 하겠습니다. (거의 다 이미 해본 내용이기 때문에 어려울 것이 없습니다. ^^)
```python
import requests
from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook as load

URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="

def save_excel(a_links, b_links, title = 'test'):
    wb = load('test.xlsx')
    ws = wb.create_sheet(title)
    try:
        for i in range(len(a_links)):
            ws['A' + str(i + 1)] = a_links[i]
        for j in range(len(b_links)):
            ws['B' + str(j + 1)] = b_links[j]
        wb.save('test.xlsx')
    except Exception as e:
        print(e)
    finally:
        wb.close()

def get_link():
    a_links = []
    b_links = [] 
    for page in range(1, 11):
        req = requests.get(URL.format(str(page)))
        code = req.status_code
        print(code)
        if code == 200:
            soup = bs(req.text, 'html.parser')
            div = soup.find_all('div', attrs= {'class':'list_con'})
            for data in div:
                a_tag = data.find('a', attrs={'title': '상세화면'})
                a_tag = a_tag.get_text()        
                a_tag = a_tag.replace('\n', '').replace('\t', '')
                box_st1 = data.find('div', attrs = {'class':'box_st1'})
                box_st1 = box_st1.get_text()
                a_links.append(a_tag)
                b_links.append(box_st1)
        else:
            print('HTTP Error:', code)
    return a_links, b_links

if __name__ == "__main__":
    a_links, b_links = get_link()
    save_excel(a_links, b_links, title='content')
```
우선 기존의 `get_link` 함수에서 크롤링한 데이터를 `save_excel` 함수에 인자로 반환하기 위해서 `a_links`, `b_links` 이름으로 각각 제목, 초록을 저장하도록 합니다. (하나의 리스트에 중복 리스트, 딕셔너리 등을 이용해도 무방합니다.) `test.xlsx` 엑셀 파일을 만들고, 해당 엑셀 파일에 `A`열에는 제목을, `B`열에는 초록을 저장합니다.

위 코드를 실행하면, 아래와 같이 엑셀 파일이 잘 저장됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course14/static/excel.png" width="100%" height="100%">
</p>

추가로, 말뭉치 분석 내용 때 다뤘던 워드 클라우드를 만드는 코드를 가져와보겠습니다.
```python
from konlpy.tag import Okt
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook as load
# import 구문이 추가로 필요하다는 점에 주의하세요!

URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="
PATH = '/Library/Fonts/NanumGothic.ttf'

def get_wc(content, title):
    ok = Okt()
    result = {}
    for c in content:
        temp = ok.pos(c)
        for t in temp:
            if t[1] == 'Noun' and len(t[0]) > 1:
                if not (t[0] in result):
                    result[t[0]] = 0
                result[t[0]] += 1
    result = sorted(result.items(), key = lambda x:x[1], reverse = True)
    print(dict(result))
    wc = WordCloud(font_path = PATH, background_color = 'white', width = 800, height = 600)
    plt.axis('off')
    plt.imshow(wc.generate_from_frequencies(dict(result)))
    plt.savefig(title + '.jpg')


def save_excel(a_links, b_links, title = 'test'):
    wb = load('test.xlsx')
    ws = wb.create_sheet(title)
    try:
        for i in range(len(a_links)):
            ws['A' + str(i + 1)] = a_links[i]
        for j in range(len(b_links)):
            ws['B' + str(j + 1)] = b_links[j]
        wb.save('test.xlsx')
    except Exception as e:
        print(e)
    finally:
        wb.close()

def get_link():
    a_links = []
    b_links = [] 
    for page in range(1, 11):
        req = requests.get(URL.format(str(page)))
        code = req.status_code
        print(code)
        if code == 200:
            soup = bs(req.text, 'html.parser')
            div = soup.find_all('div', attrs= {'class':'list_con'})
            for data in div:
                a_tag = data.find('a', attrs={'title': '상세화면'})
                a_tag = a_tag.get_text()        
                a_tag = a_tag.replace('\n', '').replace('\t', '')
                box_st1 = data.find('div', attrs = {'class':'box_st1'})
                box_st1 = box_st1.get_text()
                a_links.append(a_tag)
                b_links.append(box_st1)
        else:
            print('HTTP Error:', code)
    return a_links, b_links

if __name__ == "__main__":
    a_links, b_links = get_link()
    save_excel(a_links, b_links, title='content')
    get_wc(a_links, 'python제목')
    get_wc(b_links, 'python초록')
```
말뭉치 분석 때 정의한 `get_wc` 함수를 선언하고, 사진 제목을 두 번째 입력 값으로 받을 수 있도록 수정했습니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course14/static/w1.jpg" width="45%" height="100%">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course14/static/w2.jpg" width="45%" height="100%">
</p>

위 사진은 각각 NDSL 사이트에서 파이썬 검색 키워드에 해당하는 논문 99건의 제목과 초록에 단어 출현 빈도를 나타내는 사진입니다. 

여기서 끝내면 뭔가 아쉬우니, 위 코드에 마지막으로 한 가지만 더 추가하도록 하겠습니다. 위 코드 상에서는 우리가 정의한 함수의 인자 값을 변경하기 위해서 코드를 직접 수정해야 합니다. 

코드를 변경하는 것이 아닌, 터미널에서 사용자의 입력 값을 받고 그에 따라 코드가 수정되도록 코드를 추가하겠습니다.
```python
from konlpy.tag import Okt
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook as load

URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query={}&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="
PATH = '/Library/Fonts/NanumGothic.ttf'

def get_wc(content, title):
    ok = Okt()
    result = {}
    for c in content:
        temp = ok.pos(c)
        for t in temp:
            if t[1] == 'Noun' and len(t[0]) > 1:
                if not (t[0] in result):
                    result[t[0]] = 0
                result[t[0]] += 1
    result = sorted(result.items(), key = lambda x:x[1], reverse = True)
    print(dict(result))
    wc = WordCloud(font_path = PATH, background_color = 'white', width = 800, height = 600)
    plt.axis('off')
    plt.imshow(wc.generate_from_frequencies(dict(result)))
    plt.savefig(title + '.jpg')


def save_excel(a_links, b_links, title = 'test'):
    wb = load('test.xlsx')
    ws = wb.create_sheet(title)
    try:
        for i in range(len(a_links)):
            ws['A' + str(i + 1)] = a_links[i]
        for j in range(len(b_links)):
            ws['B' + str(j + 1)] = b_links[j]
        wb.save('test.xlsx')
    except Exception as e:
        print(e)
    finally:
        wb.close()

def get_link(keyword):
    a_links = []
    b_links = [] 
    for page in range(1, 11):
        req = requests.get(URL.format(str(page), keyword))
        code = req.status_code
        print(code)
        if code == 200:
            soup = bs(req.text, 'html.parser')
            div = soup.find_all('div', attrs= {'class':'list_con'})
            for data in div:
                a_tag = data.find('a', attrs={'title': '상세화면'})
                a_tag = a_tag.get_text()        
                a_tag = a_tag.replace('\n', '').replace('\t', '')
                box_st1 = data.find('div', attrs = {'class':'box_st1'})
                box_st1 = box_st1.get_text()
                a_links.append(a_tag)
                b_links.append(box_st1)
        else:
            print('HTTP Error:', code)
    return a_links, b_links

if __name__ == "__main__":
    try:
        while True:
            keyword = input('검색어를 입력해주세요.')
            if keyword == 'exit':
                print('종료되었습니다.')
                break
            a_links, b_links = get_link(str(keyword))
            title = input('엑셀 시트명을 입력해주세요')
            save_excel(a_links, b_links, title=title)
            a, b = input('이미지 이름을 입력해주세요. (1: 제목, 2: 초록)').split()
            get_wc(a_links, a)
            get_wc(b_links, b)
    except Exception as e:
        print(e)
 
```
우선 가장 첫 번째로, 키워드를 동적으로 변화시킬 수 있도록 하기 위해서 `URL` 문자열의 포맷팅이 `query={}`로 추가된 것을 확인할 수 있습니다. 또 한 가지 중요한 것은, `input`이라는 새로운 키워드가 나왔습니다. `input` 함수는 터미널에서 사용자의 입력을 받을 수 있도록 하는 함수입니다. 함수의 인자는 터미널의 질문(입력 요청)을 나타낼 내용을 작성합니다. 

또한, `input` 함수에 
`split()`을 입력하면, 공백(Space bar)을 기준으로 동시에 두 개의 입력 값을 작성할 수 있습니다. 기존의 코드에서 함수의 인자를 입력 값으로 넘겨줄 수 있도록 수정한 것 말고는 변한 게 없습니다. :) 코드를 실행해보시면, 어렵지 않게 이해하실 수 있을 거라 생각합니다! 


이번 장을 끝으로 파이썬 크롤러 개발까지 모두 끝내셨습니다! 정말 정말 고생하셨습니다!! :) 아마 많은 분들이, 소셜 미디어와 같은 동적 페이지 크롤링을 원하실 거라 생각합니다. 아쉽게도, 그러한 동적 웹 페이지는 `Selenium`과 같은 또 다른 패키지를 통해 파이썬 코드로 브라우저를 직접 조작하는 코딩을 작성해야 합니다. 

혹은, 해당 서비스를 제공하는 측에서 자체적으로 제공하는 `API`라는 것을 이용해서 크롤링을 할 수 있습니다.(이 내용은 다소 코드가 제한적이고, 많은 양의 데이터를 크롤링해야 하는 경우엔 금액을 지불해야 합니다 ^^) 

이번 장에서는 제가 의도적으로 주석을 많이 달지 않았습니다. 위 코드의 내용이 아직 모두 다 이해가 가지 않더라도 괜찮습니다. 직접 위 코드를 손으로 하나하나 작성도 해보시고, 더 좋은 방법이 없는지 등도 많이 찾아보는 시간을 가져보셨으면 좋겠습니다. 

처음부터 수십수백 줄의 코드를 막힘 없이 짜낼 수 없습니다. 항상 단계 별로 조금씩 코드를 작성해보시고, 공부한 내용을 정리하고 글로 작성해두는 습관을 들이면 공부하는 데 도움이 될 거라 생각합니다. 틈틈이 알고리즘 공부도 하시는 거 잊지 마세요! 마지막으로, 파이썬 코드 작성을 위해서 [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/), [tensorflow](https://github.com/tensorflow/tensorflow)와 같은 여러 가지 기술들이 있습니다. 파이썬 코드 작성에 어느 정도 익숙해지셨다면, 위 내용도 함께 살펴보시는 걸 추천드립니다. :)

정말 고생 많으셨습니다. 감사합니다. :)