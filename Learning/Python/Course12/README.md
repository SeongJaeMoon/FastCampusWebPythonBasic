# Python 크롤러2 - BeautifulSoup, requests
키워드 : [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [requests](http://docs.python-requests.org/en/master/), [웹 크롤러](https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%81%AC%EB%A1%A4%EB%9F%AC)

[지난 내용](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Python/Course11/)에 이어서 파이썬 크롤러 개발 두 번째 내용을 정리해보도록 하겠습니다. 크롤링을 위해 사용할 수 있는 패키지는 굉장히 다양하지만, 우리는 `BeautifulSoup`, `requests` 두 가지 패키지를 중심으로 다룰 것이기 때문에, 위 두 패키지를 기준으로 계속 진행하도록 하겠습니다.

## requests
웹 자원을 요청하기 위해서 사용하는 패키지로 `requests`를 소개했습니다. `requests` 패키지는 굉장히 다양한 기능들이 제공합니다. `requests` 패키지의 몇 가지 주요 내용에 대해서 살펴보도록 하겠습니다.
```python
import requests

params = {'key1':1, 'key2':2}
r = requests.get('https://www.fastcampus.co.kr/dev_online_introdev/', params=params) # HTTP GET 요청

print(r.encoding) # UTF-8
print(r.url) # https://www.fastcampus.co.kr/dev_online_introdev?key1=1&key2=2
print(r.text) # 응답 받은 콘텐츠를 해석할 수 있는 인코딩 형태로 만들어줍니다.
```
우선, 우리는 강의에서 `requests` 모듈의 `get` 메서드를 이용해서, 웹 사이트의 정보를 자원을 검색하고, 파이썬 코드로 핸들링 할 수 있다고 말씀드렸습니다. 웹 자원을 요청할 때, `params`라는 이름 있는 인자에 `키:값` 형태의 딕셔너리로 쿼리 문자열을 만들어 요청할 수 있습니다. 또한, `requests` 모듈의 경우 가져온 웹 자원의 인코딩 설정 등도 확인할 수 있습니다.
```python
import requests

data = {'key1':1, 'key2':2}
r = requests.post('https://www.fastcampus.co.kr/dev_online_introdev/', data=data)
```
우리가 웹 자원을 요청할 때는 `get` 방식 뿐만 아니라, `post` 방식으로도 요청할 수 있습니다. `post` 메서드는 `data`라는 이름있는 인자에 `get` 메서드와 마찬가지로 `키:값` 형태의 딕셔너리로 `name, value`를 만들어 웹 자원을 요청할 수 있습니다.
```python
import requests
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get('https://www.fastcampus.co.kr/dev_online_introdev/', headers=headers)
```
웹 자원을 요청할 때, 헤더 정보도 함께 담아서 요청할 수 있는데요, `HTTP`에 대해서 이야기할 때, 헤더에 대해서 잠시 언급한 적이 있습니다. 우선, 개발자 도구를 통해 구글 사이트의 요청 헤더 정보를 확인해보도록 하겠습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course12/static/header.png" width="100%" height="100%">
</p>

`Network` 탭의 가장 상단부 URL을 클릭합니다. 우리는 요청하는 측이기 때문에, `Request Headers` 부분을 봐주시면 됩니다. 이 헤더 정보에는 `User-Agent`라는 기기 정보와 브라우저 정보를 담는 부분이 있습니다.

우리가 크롤링을 통해 웹 자원을 요청하면, 기존의 브라우저가 아닌 프로그램 코드를 통해서 요청하는 것이 됩니다. 몇몇 웹 사이트는 이 부분을 해석하여 정상적인 브라우저가 아니라 크롤링을 위한 독립적인 프로그램인 것을 확인하고, 걸러내는 경우가 있습니다. 이러한 경우에 `headers`라는 이름 있는 인자에 `User-Agent` 값을 마찬가지로 딕셔너리 형태로 만들어 전송해줘야 합니다.

## BeautifulSoup
요청한 웹 자원이 정상적으로 잘 돌아오면, 불러온 웹 자원을 우리가 분석하기 용이한 HTML 문서로 파싱(Parsing)하는 작업이 필요합니다. HTML 문서를 파싱하고 분석하기 위한 `BeautifulSoup` 패키지의 몇 가지 주요 내용에 대해서 살펴보도록 하겠습니다.
```python
import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.fastcampus.co.kr/dev_online_introdev/')
soup = bs(r.text, 'html.parser')
```
웹 자원을 불러온 후, 불러온 웹 자원을 `BeautifulSoup` 객체의 첫 번째 인자로 `r.text`, 두 번째 인자로 `html.parser`를 입력 값으로 넘겨줍니다. 참고로, `html`뿐만 아니라, 우리가 공부하진 않았지만, `xml, lxml` 등 다양한 형식의 파일 구조를 파싱 할 수 있습니다.
```python
import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.fastcampus.co.kr/dev_online_introdev/')
soup = bs(r.text, 'html.parser')

print(soup) 

# 찾은 태그를 하나만 반환합니다.
soup.find('div')
soup.find(id = 'id')
soup.find('div', id ='id')
soup.find('div', class_ ='class')
# 찾은 태그를 리스트로 반환합니다.
soup.find_all('div', attrs={'id':'id'})
soup.find_all('div', attrs={'class':'class'})
soup.select('css  selector') 
# 속성에 해당하는 값을 반환합니다.
href = soup['href']
name = soup['name']
value = soup['value']
# 태그가 담고 있는 콘텐츠를 가져옵니다.
print(soup.get_text())
```
`soup` 객체를 `print` 함수로 터미널에 출력하면, 우리가 잘 아는 형태의 `html` 구조로 만들어진 것을 확인할 수 있습니다. 이제 이 `html` 형식의 `soup` 객체의 다양한 메서드를 통해서 특정 태그의 정보만 추출해서 가져올 수 있습니다. 주의해야 할 점은, `find` 메서드의 경우 하나의 `BeautifulSoup` 객체를 반환하고, `find_all`과 `select` 메서드의 경우엔 리스트로 `BeautifulSoup` 객체를 반환합니다.

## 사이트 웹 자원 불러오기
이제 본격적으로 파이썬 크롤링 코드를 작성해보도록 하겠습니다. 첫 번째로, 앞서 크롤링을 위해 선정했던 사이트인, 'NDSL'의 웹 자원을 위 패키지를 통해 가져오도록 하겠습니다.
```python
import requests
from bs4 import BeautifulSoup as bs
URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="
```
우선, 파이썬 검색어를 입력했을 때 나오는 url 주소를 복사하여 `URL`이라는 이름으로 초기화합니다. 단, 우리는 문자열 포맷팅을 통해 페이징 작업을 자동으로 이루어지게 할 것이기 때문에, `page={}` 형태로 포맷을 설정해둡니다.
```python
import requests
from bs4 import BeautifulSoup as bs
URL = "http://www.ndsl.kr/ndsl/search/list/article/articleSearchResultList.do?page={}&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&prefixQuery=&collectionQuery=&showQuery=%ED%8C%8C%EC%9D%B4%EC%8D%AC&resultCount=10&sortName=RANK&sortOrder=DESC&colType=scholar&colTypeByUser=&filterValue="

def get_link():
    for page in range(1, 11):
        req = requests.get(URL.format(str(page)))
        soup = bs(req.text, 'html.parser')
        print(soup)

if __name__ == "__main__":
    get_link()
```
웹 페이지가 1부터 시작하기 때문에, 반복문의 시작을 1부터 시작하여 10 페이지까지 반복하도록 합니다. 위 코드를 실행하면, 아래와 같이 자동으로 페이징을 하며, 웹 자원이 잘 불러와지는 것을 확인할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course12/static/get.gif" width="100%" height="100%">
</p>

위 코드에서 한 가지 주의할 점이 있습니다. 위 `URL`은 현재 `http`로 시작하고 있습니다. 만약, `requests` 모듈을 이용하여 `https` 프로토콜의 웹 자원을 요청할 시에는 `SSLError`라는 에러가 발생할 수 있습니다. 이런 경우 `get` 메서드의 인자로 `verify=False`라는 것을 추가로 입력해야 합니다. (`e.g., requests.get(URL.format(str(page)), verify=False)`)

위에서 모두 다루지 못한 `requests` 패키지에 대한 더 자세한 설명은 [여기](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)를 참고해주시고, `BeautifulSoup`와 관련된 더 자세한 설명은 [여기](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)를 참고 부탁드립니다. 

이번 장에서는 웹 자원 요청에 대해서 알아보았습니다. 세상에는 수많은 웹 사이트가 있습니다. 각각의 웹 사이트마다 서로 다른 특징을 가지고 있으며, 한 가지 방법으로 모든 웹 사이트의 자원과 정보를 가지고 올 순 없습니다. 하지만, 코드를 구성하는 기본적인 로직 자체는 큰 변화가 없습니다. 전체적인 틀에 대한 이해가 있다면, 약간의 검색과 몇 번의 시도로 금세 해결할 수 있습니다. :)