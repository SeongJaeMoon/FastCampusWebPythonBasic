# Python 말뭉치 처리
키워드 : [말뭉치](https://ko.wikipedia.org/wiki/%EB%A7%90%EB%AD%89%EC%B9%98), [konlpy](http://konlpy.org/ko/latest/), [wordcloud](https://github.com/amueller/word_cloud)    

강의에서도 언급했듯이, 우리가 사용하는 자연어(Natural language)를 분석하기 위해서는, 굉장히 다양한 기술들이 필요합니다. 그중에서도 굉장히 중요한 역할을 하는 것이 있습니다. 바로, 이번 장에서 살펴볼 말뭉치라는 것입니다. 말뭉치는 우리가 사용하는 한글뿐만 아니라, 전 세계 어떤 언어이든지 간에 자연어를 분석하고, 처리하기 위해서 가장 기본이 되는 언어의 표본 집합입니다. 

한글의 말뭉치는 국립국어원에서 실행한 세종 프로젝트를 통해서 만들어진 [세종 말뭉치](https://ithub.korean.go.kr/user/guide/corpus/guide1.do)라는 것이 가장 대표적으로 활용되는 말뭉치입니다. 세종 말뭉치는 형태소 단위로 한글을 분리하여, 분석할 수 있도록 미리 작성된 표본 집합입니다. 참고로, 한국어의 감성 분석을 위해 [KOSAC](http://word.snu.ac.kr/kosac/)과 같은 언어 표본 집합 등도 많이 존재합니다. 

이러한 한글 말뭉치를 통해 한글을 분석할 수 있는 파이썬 패키지가 많이 존재합니다. 그중에서, 주요 다섯 개의 한글 말뭉치 처리 파이썬 패키지를 하나로 모아 사용자가 쉽게 사용할 수 있도록 만든 파이썬 패키지가 바로, 우리가 강의에서 알아본 [konlpy("코엔엘파이")](http://konlpy.org/ko/latest/)입니다. 아직 `konlpy` 패키지 설치가 완료되지 않으셨다면, [여기](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Python/Course01/task)에 접속하셔서, 파이썬 패키지 설치를 먼저 진행해주세요!

포함되어 있는 여러 가지의 파이썬 한글 말뭉치 분석 패키지 중에서 우리는, [Okt(Open Korean Text)](https://github.com/open-korean-text/open-korean-text)라는 트위터에서 개발하고, 오픈 소스로 공개되어 있는 패키지를 이용합니다. 이번 장에서는 해당 패키지를 이용해 간단한 **문자열 집합 안에서 문자의 출현 빈도를 계산**하는 예시를 코드와 함께 알아보도록 하겠습니다.
```python
# tag 모듈 안의 Okt class 불러오기
from konlpy.tag import Okt
# 임의의 문자열 리스트를 선언합니다.
NOUNS = ['한글', '한글날', '세종', '세종대왕', '패스트', '캠퍼스']
# Okt 객체를 선언합니다.
ok = Okt()
```
우선, `Okt` 클래스를 사용하기 위해서, 모듈을 불러옵니다. 우리는 분석할 문자 집합이 없기 때문에, 임의로 분석할 문자 집합을 만들어 내기 위해서, `NOUNS`라는 리스트를 선언합니다. `'한글', '한글날', '세종', '세종대왕', '패스트캠퍼스'`가 요소로 초기화 되어 있는 것을 확인할 수 있습니다. (임의로 초기화한 것이기 때문에, 원하는 글자를 사용해도 무방합니다.) 
```python
from konlpy.tag import Okt
from random import randint # random 표준 모듈의 randint 불러오기

NOUNS = ['한글', '한글날', '세종', '세종대왕', '패스트', '캠퍼스']

ok = Okt()
# 임의의 문자열 집합을 만들어내기 위한 함수를 선언합니다.
def get_rand():
    content = [] # 임의의 문자열 리스트를 담을 빈 리스트를 선언합니다.
    for i in range(5): # 0 ~ 4 까지 반복
        temp = "" # 랜덤한 문자열을 만들 변수를 선언합니다.
        j = 0 # 반복 중지 조건을 만들기 위한 변수를 선언합니다.
        while j < 100: # j의 값이 100이 될 때 까지 반복합니다.
            temp += NOUNS[randint(0, 5)] # 문자열 리스트의 값을 무작위로 가져와 문자열 결합합니다.
            j += 1 # 반복 중지 조건을 위해 인덱스를 증가시킵니다.
        content.append(temp) # 만들어진 문자열을 할당합니다.
```
다음은, 임의의 문자열 집합을 만들어내기 위한 `get_rand`라는 함수를 정의합니다. 무작위로 문자열을 만들어내기 위해서, 파이썬 표준 모듈 중에 `random`이라는 모듈을 사용할 수 있습니다. `random` 모듈 안에 `randint` 함수를 이용하면, 지정한 범위의 값을 랜덤 하게 반환해줍니다.(`첫 번째 인자 <= x <= 두 번째 인자`) 

반복문(`while 구문`)을 통해 `NOUNS`의 요소를 임의대로 100번 문자열 결합하고, 다시 그 반복을 다섯 번 반복(`for 구문`)하여 `content` 리스트에 할당합니다. `content` 리스트의 값을 출력해보면, 아래와 같이 무작위로 문자열 결합이 되어 있습니다.

> 패스트캠퍼스세종대왕한글한글한글날세종한글날세종대왕한글한글...

```python
from konlpy.tag import Okt
from random import randint 

NOUNS = ['한글', '한글날', '세종', '세종대왕', '패스트', '캠퍼스']
# 문자의 출현 빈도를 계산하기 위한 함수를 정의합니다.
def get_wc(content):
    ok = Okt() # Okt 객체를 함수 안에 선언했습니다.
    result = {} # 출현 빈도 계산을 위해 빈 딕셔너리를 선언합니다.
    for c in content: # 무작위로 문자열 결합된 값들을 하나씩 받아옵니다.
        temp = ok.pos(c) # Okt 객체의 메서드 중에서 pos 메서드를 이용해 (문자, 품사) 형태의 값을 리스트로 반환하여 temp 임시변수에 할당합니다.
        for t in temp: # 반환 받은 품사 리스트의 크기 만큼 반복합니다.
            if t[1] == 'Noun': # 품사가 명사인지 확인합니다.
                if not (t[0] in result): # 출현 빈도를 계산하기 위해 선언한 딕셔너리에 단어가 들어있는지 확인합니다.
                    result[t[0]] = 0 # 단어가 최초로 나왔다면, 0으로 초기화합니다.
                result[t[0]] += 1 # 찾은 단어의 값을 1 증가합니다.
    result = sorted(result.items(), key = lambda x:x[1], reverse = True) # sorted 내장 함수를 이용해 딕셔너리를 내림 차순 정렬하고, 리스트로 반환합니다.
    print(result) # 출현 빈도를 출력합니다.

def get_rand():
    content = [] 
    for i in range(5): 
        temp = "" 
        j = 0 
        while j < 100: 
            temp += NOUNS[randint(0, 5)] 
            j += 1 
        content.append(temp) 
    return content

# 단독 스크립트 실행인지 확인합니다.
if __name__ == "__main__":
    get_wc(get_rand()) # 단독 스크립트 실행이라면, 출현 빈도를 계산하는 함수를 실행합니다.
```
코드가 조금 길어졌는데요, 강의를 통해서도 이미 알고 있는 내용이 많기 때문에, 어렵지 않게 이해하실 수 있을겁니다. 코드에서 사용한 `Okt` 클래스의 `pos` 메서드는 문자열 안의 단어를 모두 쪼개고, `('단어', '품사')` 형태로 만들어 리스트로 반환합니다. `Okt` 클래스의 메서드와 관련된 더 자세한 내용은 [여기](http://konlpy.org/en/latest/api/konlpy.tag/#okt-class)와 [여기](https://github.com/open-korean-text/open-korean-text)에서 확인할 수 있습니다.

위 코드를 VS code에서 터미널로 실행하면, 아래와 같은 결과가 터미널에 출력됩니다. 출현 빈도는 무작위이기 때문에, 코드를 실행할 때 마다 달리집니다.

> [('한글날', 89), ('세종대왕', 87), ('캠퍼스', 87), ('세종', 84), ('패스트', 82), ('한글', 71)]

여기서 끝내면 뭔가 아쉬우니, 위 내용을 가지고 계속해서 약간의 심화 내용을 더 살펴보도록 하겠습니다. 

우리가 무언가에 빈도를 나타내기 위해서 보통 그래프를 많이 이용합니다. 위 코드에 약간의 추가를 하여 단어의 출현 빈도를 그래프로 표현해보도록 하겠습니다. 단, 일반적인 바(Bar) 형태의 그래프가 아닌, 워드 클라우드라는 것을 만들어 보도록 하겠습니다. 

우선, 코드를 작성하기 전에, 몇 가지 패키지를 `pip`로 다운로드해야 합니다. 우리는 이미 `pip`를 통해 다양한 패키지를 다운로드했기 때문에, 같은 방법으로 진행해주시면 됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course10/static/wordcloud.png" width="100%" height="70%">
</p>

먼저, VS code 터미널에서 가상 환경을 실행합니다. 아래 명령어를 터미널에 입력합니다. `wordcloud` 패키지를 이용해서 워드 클라우드를 만들 수 있습니다.

> pip3 install wordcloud

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course10/static/matplotlib.png" width="100%" height="50%">
</p>

`wordcloud` 패키지 설치가 잘 되었다면, 이번엔 아래 명령어를 터미널에 입력하여 `matplotlib` 패키지를 다운로드합니다. 

> pip3 install matplotlib

참고로, `matplotlib` 패키지는 워드 클라우드뿐만 아니라, 다양한 분야에서 파이썬으로 그래프를 표현하기 위해 사용되는 인기 있는 패키지입니다. (파이썬 패키지를 이야기할 때 거의 빠지지 않고 등장하는 패키지입니다. ^^)

위 패키지 설치가 잘 이루어졌다면, 이제 워드 클라우드를 만드는 코드를 추가해보도록 하겠습니다.
```python
from konlpy.tag import Okt
from random import randint
# wordcloud 모듈의 WordCloud 클래스 불러오기
from wordcloud import WordCloud
# matplotlib 모듈 불러오기
import matplotlib as mpl
mpl.use('TkAgg') # 맥 OS에서 가상 환경 에러 해결을 위해 사용합니다.
from matplotlib import pyplot as plt # 그래프를 그리기 위해 pyplot 모듈을 불러옵니다.

NOUNS = ['한글', '한글날', '세종', '세종대왕', '패스트', '캠퍼스']
# ttf 형식의 한글 폰트 경로입니다. (e.g., Nanum, NanumGothic, etc.)
PATH = '/Library/Fonts/NanumGothic.ttf' # 윈도의 경우 C:\Windows\Fonts\NanumGothic.ttf
 
def get_wc(content):
    ok = Okt()
    result = {}
    for c in content:
        temp = ok.pos(c)
        for t in temp:
            if t[1] == 'Noun':
                if not (t[0] in result):
                    result[t[0]] = 0
                result[t[0]] += 1
    result = sorted(result.items(), key = lambda x:x[1], reverse = True)
    
    # WordColud 객체를 선언합니다.
    wc = WordCloud(font_path = PATH, background_color = 'white', width = 800, height = 600)
    # 그래프의 x, y 축이 나타나지 않도록 합니다.
    plt.axis('off')
    # 출현 빈도에 따라 워드 클라우드를 그리기 위해서 워드 클라우드 객체의 메서드를 이용합니다. 
    plt.imshow(wc.generate_from_frequencies(dict(result)))
    # 워드 클라우드를 이미지로 저장합니다.
    plt.savefig("test.jpg")  

def get_rand():
    content = [] 
    for i in range(5): 
        temp = "" 
        j = 0 
        while j < 100: 
            temp += NOUNS[randint(0, 5)] 
            j += 1 
        content.append(temp) 
    return content

if __name__ == "__main__":        
    get_wc(get_rand())
```
코드가 몇 줄 더 추가되었는데요, 사실 10줄 정도의 코드만 더 추가되었습니다. 그래도 처음 보는 코드 구문이 많이 늘어났으므로, 하나하나 살펴보도록 하겠습니다. 

우선, 워드 클라우드를 그릴때, 한글의 경우 깨지는 현상이 발생할 수 있습니다. 이를 해결하기 위해 한글을 나타낼 수 있는 폰트를 정해주어야 합니다. 윈도의 경우 `C:\Windows\Fonts`, 맥의 경우엔 `/Library/Fonts/`에 컴퓨터에서 사용할 수 있는 폰트가 저장되어 있습니다. 위 코드 예시의 경우 나눔고딕 폰트를 사용하였습니다.

컴퓨터에 나눔고딕 폰트가 설치되어 있지 않으시다면, [여기](https://hangeul.naver.com/download.nhn)에 접속하셔서, 한글 폰트를  위 경로에 저장해주시면 됩니다.

> wc = WordCloud(font_path = PATH, background_color = 'white', width = 800, height = 600)

워드 클라우드 객체 선언을 할 때, `font_path` 인자로 경로를 작성해줍니다. `background_color` 인자의 경우엔 보통 `white`로 많이 작성하고, 원하면 다른 색상을 사용할 수 있습니다. `widht`, `height` 인자는 각각 워드 클라우드의 너비와 높이를 설정할 수 있는 인자입니다.

> plt.imshow(wc.generate_from_frequencies(dict(result)))

워드 클라우드 객체의 `generate_from_frequencies` 메서드를 이용하면, 간단하게 워드 클라우드를 그릴 수 있습니다. 단, 인자로 넘겨줄 값은 키와 값 형태로 이루어진 딕셔너리여야 합니다. 앞서, 미리 작성한 코드의 경우 리스트로 정렬된 값을 반환하고 있기 때문에, `dict` 키워드를 이용해 리스트를 딕셔너리로 변환합니다. 

딕셔너리로 변환하면, 아래와 같은 형태로 변환됩니다.

> {'세종대왕': 113, '한글': 110, '패스트': 101, '캠퍼스': 101, '한글날': 94, '세종': 87}

이제 메모리 상에서만 만들어진 그래프를 이미지 파일로 저장하기 위해서, 파일 이름과 확장자까지 작성해줍니다.

> plt.savefig("test.jpg")

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course10/static/test.jpg" width="100%" height="100%">
</p>

파이썬 파일이 있는 폴더를 확인해보면, 위와 같이 워드 클라우드가 이미지 파일로 생성된 것을 확인할 수 있습니다! :)

이번 장에서는 간단한 한글 말뭉치 처리에 대해서 알아보았습니다. 보통, 자연어 처리를 위해선 수학적 기법이 적용된 [word2vec](https://en.wikipedia.org/wiki/Word2vec), [베이지안 필터링](https://ko.wikipedia.org/wiki/%EB%82%98%EC%9D%B4%EB%B8%8C_%EB%B2%A0%EC%9D%B4%EC%A6%88_%EB%B6%84%EB%A5%98), [SVM](https://ko.wikipedia.org/wiki/%EC%84%9C%ED%8F%AC%ED%8A%B8_%EB%B2%A1%ED%84%B0_%EB%A8%B8%EC%8B%A0) 등의 굉장히 많은 기술들이 서로 유기적으로 활용됩니다. 또한, 이러한 기술들이 접목되어 텍스트 마이닝, 검색 추천, 챗봇, 문자 자동 완성 등에 사용될 수 있습니다. 데이터 분석과 관련된 내용에 관심이 있으시다면, 이러한 부분들에 대해 깊은 공부를 해보시는 것을 추천드리고 싶습니다! :) (학습 난이도가 상당합니다..^^)