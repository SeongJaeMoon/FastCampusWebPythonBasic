# Python 크롤러3 - 데이터 추출
키워드 : [HTTP status code](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C), [웹 크롤러](https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%81%AC%EB%A1%A4%EB%9F%AC)

[지난 내용](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Python/Course12/)에 이어서 파이썬 크롤러 개발 세 번째 내용을 정리해보도록 하겠습니다. 지난 내용을 통해 페이징을 진행하며, 웹 자원을 불러오는 것이 가능해졌습니다. 이번 장에서는 많은 웹 자원 중에서 원하는 콘텐츠만 추출하는 코드를 작성해보도록 하겠습니다.

## HTTP 상태 코드
강의에서 살펴봤던 HTTP 상태(또는 응답) 코드에 대해서 잠시 이야기하고 진행하도록 하겠습니다. 우리가 프로그램을 통해 서버에게 웹 자원을 요청하면, 서버는 우리에게 웹 자원과 함께 여러 가지 정보를 함께 제공합니다. 

예를 들어, 클라이언트의 요청에 서버가 잘 반응했는지, 반응하지 못했는지, 만약 반응하지 못했다면 왜 반응하지 못했는지 등에 대한 정보를 1xx ~ 5xx까지의 숫자로 나타내 우리에게 전송해줍니다. 이 정보가 바로 HTTP 상태 코드라고 할 수 있습니다.

한 번쯤 접해보셨을 상태 코드는 아마도, `404 Not Found`일 것입니다. 이 상태 코드는 웹과 관련해서 필수적인 지식입니다. 안타깝게도 이 상태 코드의 종류는 굉장히 여러 가지가 있습니다. 외우실 필요는 없습니다. 찾아보면 금방 나오기도 하며, 자연스럽게 응답 코드가 나타내는 의미에 익숙해지실 겁니다. 

강의에서도 말씀드렸듯이, 지금 당장은 한 가지만 기억해주시면 됩니다. 서버에 웹 자원 요청 시 돌아온 상태 코드가 `200`이라면, 정상적으로 서버가 우리의 요청을 받고, 응답한 것이라는 것을 말입니다! :)

더 자세한 HTTP 상태 코드와 관련된 내용은 [여기](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C)를 참고해주세요.
## 원하는 콘텐츠 추출
지난 내용의 코드에 이어서 크롤링 코드를 작성해보도록 하겠습니다.

```python
import requests
from bs4 import BeautifulSoup as bs
URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="

def get_link():
    for page in range(1, 11):
        req = requests.get(URL.format(str(page)))
        code = req.status_code
        if code == 200:
            soup = bs(req.text, 'html.parser')
            print(soup)
        else:
            print('HTTP Error:', code)
if __name__ == "__main__":
    get_link()
```
`get` 메서드를 이용해 웹 자원을 요청하고, `status_code`라는 속성을 통해서 응답 코드를 반환할 수 있습니다. `if`구문으로 응답 코드가 `200`이라면 코드를 계속 실행할 수 있도록 조건을 걸어줍니다. 만약, `200`이 아니라면, 어떤 코드가 돌아왔는지 출력하도록 합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/a.png" width="45%" height="100%">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/p.png" width="45%" height="100%">
</p>

이제 본격적으로 웹 상에서 원하는 콘텐츠를 추출하는 코드를 작성해보도록 하겠습니다. 그전에, 웹 사이트 분석 파트에서 개발자 도구를 이용한 선택자 문법을 다시 한번 확인하도록 하겠습니다.

>  #result_list > li:nth-child(1) > div.list_con > p.title > a

> #result_list > li:nth-child(1) > div.list_con > div:nth-child(4) > p:nth-child(2)

웹 사이트 분석 파트에서도 말씀드렸듯이, `div.listcon`이 공통된 부모 요소로 들어있는 것을 확인할 수 있습니다. 이걸 활용하여, 두 내용을 하나로 가져올 수 있습니다.
```python
import requests
from bs4 import BeautifulSoup as bs
URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="

def get_link():
    for page in range(1, 11):
        req = requests.get(URL.format(str(page)))
        code = req.status_code
        if code == 200:
            soup = bs(req.text, 'html.parser')
            div = soup.find_all('div', attrs= {'class':'list_con'}) # find_all 메서드를 이용하여 클래스 속성이 list_con인 div 요소를 리스트로 반환합니다.
            print(div) 
        else:
            print('HTTP Error:', code)
if __name__ == "__main__":
    get_link()
```
위 코드에서 추가된 `div` 요소를 찾는 코드를 통해서, 하나의 페이지 안의 모든 제목과 초록을 받아옵니다. 하지만, 여전히 받아온 웹 자원 안에는, 원치 않는 자원들이 많이 있습니다. 개발자 도구를 한 번 더 살펴보겠습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course13/static/a.png" width="100%" height="100%">
</p>

우선 제목을 나타내는 태그를 확대한 사진입니다. `title` 속성 값이 `상세화면`인 `a` 태그의 콘텐츠인 것을 확인할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course13/static/p.png" width="100%" height="100%">
</p>

다음으로, 초록을 나타내는 태그를 확대한 사진입니다. `class` 속성 값이 `box_st1`인 `div` 태그의 자식인 `p` 태그 안에 콘텐츠인 것을 확인할 수 있습니다.

위 정보를 통해 코드를 추가하면, 아래와 같이 작성할 수 있습니다.

```python
import requests
from bs4 import BeautifulSoup as bs
URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="

def get_link():
    for page in range(1, 11):
        req = requests.get(URL.format(str(page)))
        code = req.status_code
        if code == 200:
            soup = bs(req.text, 'html.parser')
            div = soup.find_all('div', attrs= {'class':'list_con'}) 
            # 하나의 페이지에서 찾은 제목과 초록의 리스트 만큼 반복합니다.
            for data in div:
                # title 속성이 상세화면인 a 태그를 찾습니다.
                a_tag = data.find('a', attrs={'title': '상세화면'}) 
                a_tag = a_tag.get_text() # 가져온 태그의 정보 중에 콘텐츠만 추출하여 문자열로합니다.    
                # class 속성이 box_st1인 div 태그를 찾습니다.    
                box_st1 = data.find('div', attrs = {'class':'box_st1'}) 
                box_st1 = box_st1.get_text() # 가져온 태그의 정보 중에 콘텐츠만 추출하여 문자열로 반환합니다.       
                print(a_tag.replace('\n', '').replace('\t', ''))
                print(box_st1)
                print('------------------------------------------------------')
        else:
            print('HTTP Error:', code)
if __name__ == "__main__":
    get_link()
```
위 코드에서 두 가지 의문점이 생기실 수 있습니다. 하나는 `box_st1`의 값을 클래스 속성이 `title`인 `p` 태그가 아닌 `div` 태그로 찾아온 이유입니다. 직접 개발자 도구로 보시면 아시겠지만, 우리가 원하는 제목 정보가 아님에도 클래스 속성이 `title`로 적용되어 있는 요소가 있습니다. 그렇기 때문에, 하나 위 부모 요소인 `div` 태그로 찾은 것입니다. 

다른 하나는, `a_tag`의 값을 출력할 때 문자열 메서드인 `replace` 메서드의 사용 이유입니다. 위 코드를 `replace` 메서드 없이 실행할 경우에 엔터와 탭 등이 포함된 형태로 나타나게 됩니다. 그렇기 때문에, 줄 바꿈과 탭에 해당하는 이스케이프 문자를 공백 처리하는 코드를 추가한 것입니다.

위 코드를 실행하면, 아래와 같이 크롤링이 진행되며, 동시에 원하는 콘텐츠만 추출해서 출력됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course13/static/content.gif" width="100%" height="100%">
</p>

이번 장에서는 불러온 웹 자원 중에 원하는 콘텐츠만 추출하는 코드를 작성해보았습니다. 사실, 다른 사람이 작성한 HTML, CSS 구조로 되어 있는 웹 사이트를 분석하여 내가 원하는 콘텐츠만 추출하는 작업은 쉬운 작업은 아닙니다. 

하지만, 내용이 어렵다기보다는 아직 익숙하지 않기 때문에 그런 부분이 더 클 것입니다. HTML과 CSS 구조에 대해서는 이미 웹 개발 기초 시간에 공부를 했기 때문에, 조금만 연습하다 보면 원하는 콘텐츠를 추출하기 위한 코드를 작성하실 수 있을 겁니다! :)
