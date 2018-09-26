# Python 패키지 설치
키워드 : [pip](https://ko.wikipedia.org/wiki/Pip_(패키지_관리자)), [requests](http://docs.python-requests.org/en/master/), [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [openpyxl](https://openpyxl.readthedocs.io/en/stable/), [konlpy](http://konlpy.org/en/latest/)

아직 파이썬 설치와 가상 환경 설정이 이루어지지 않으신 분은 [여기](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Python/Course01/)에 접속하셔서, 참고 자료를 보며 파이썬 설치 및 가상 환경 설정을 먼저 진행해주세요! 아울러, 강의에서 다루지 않는 [Python 기본 문법](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Python/Course01/#python-기본-문법) 부분도 확인부탁드립니다!

## Windows 운영체제
윈도우 운영체제를 사용하시는 분은 아래 패키지를 설치하기 전에 `java`와 `JPype`를 설치해주셔야 합니다. 맥 운영체제를 사용하시는 분은 이 부분은 건너뛰고 바로 [패키지 설치](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Python/Course01/task/#패키지-설치)를 진행하시면 됩니다.

### 자바 설치

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/java1.JPG" width="100%" height="70%">
</p>

구글 검색 창에 `java`를 입력합니다. 가장 상단에 나오는 "무료 소프트웨어 다운로드"를 선택합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/java2.JPG" width="100%" height="70%">
</p>

경우에 따라서, 쿠키 설정 동의 요청 창이 나올 수가 있습니다. 모두 `예`를 클릭하고, `기본 설정 제출`을 클릭합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/java3.JPG" width="100%" height="70%">
</p>

`동의 및 무료 다운로드 시작`을 클릭해줍니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/java4.JPG" width="100%" height="70%">
</p>

설치 마법사가 나오면 `설치`를 클릭하여 설치를 시작합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/java6.JPG" width="100%" height="70%">
</p>

잠시 기다리면, 설치가 진행됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/java7.JPG" width="100%" height="70%">
</p>

만약, 기존의 구 버전 자바가 설치되었다면, 위와 같은 화면이 나오게 됩니다. `설치 해제`를 클릭해줍니다. (일정 시간 이상 소요될 수 있습니다.) 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/java10.JPG" width="100%" height="70%">
</p>

잠시 기다리면 자바 설치가 완료됩니다.

## JDK 설치

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/jdk1.png" width="100%" height="70%">
</p>

다음으로, JDK를 설치해야 합니다. [여기](https://www.oracle.com/technetwork/java/javase/downloads/index-jsp-138363.html)에 접속합니다. `Oracle JDK`부분을 클릭합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/jdk2.png" width="100%" height="70%">
</p>

페이지 하단에 `Accept License Agreement`를 체크하고, `windows-x64_bin.exe` 파일을 다운로드 받고 설치합니다.

## JAVA_HOME 설정

자바 설치가 완료되면, JAVA_HOME 설정을 진행해야 합니다. 우선, java 설치 파일의 경로를 확인합니다.

보통, 자바를 처음 설치하면 자동으로 C 드라이브에 ProgramFiles 폴더 밑에 java 파일이 설치됩니다. 해당 경로에 접속하면, "jdk_버전", "jre_버전" 형태로 폴더가 존재합니다. jdk_버전 폴더에 접속하여 `bin` 폴더를 찾습니다. 해당 폴더의 경로를 클립보드에 복사합니다. (`e.g., C:\Program Files\Java\jdk1.8.0_181\bin`) 다음으로, 윈도 탐색기에 `시스템 환경 변수`를 입력하면 환경 변수를 설정할 수 있는 선택 메뉴가 나타납니다. 클릭해줍니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/sp1.JPG" width="100%" height="70%">
</p>

시스템 속성 창이 나타나면, "환경 변수"를 클릭해줍니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/sp2.JPG" width="100%" height="70%">
</p>

하단의 시스템 변수 설정 부분에서 "새로 만들기"를 클릭합니다. 


<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/jdk3.jpeg" width="100%" height="70%">
</p>

새 시스템 변수 창이 나타나면, 변수 이름을 `JAVA_HOME`이라고 작성하고, 변수 값을 앞서 복사한 `java/jdk버전/bin` 폴더 경로를 붙여 넣기 합니다. 입력이 완료되면, 모두 확인을 누르고 빠져나옵니다. 

### Jpype 설치
우선, [여기](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)에 가셔서 `Jpype`를 로컬 저장소에 다운로드하여야 합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/jpype1.JPG" width="100%" height="70%">
</p>

여러 가지 버전이 존재하는데요, 그중에서 32비트 파이썬을 설치한 경우에는, `JPype1‑0.6.3‑cp37‑cp37m‑win32.whl`를 선택하고 다운로드해줍니다. 64비트 파이썬을 설치한 경우에는, `JPype1‑0.6.3‑cp37‑cp37m‑win_amd64.whl`를 선택하고 다운로드해줍니다.

저장 경로는 따로 특정 지을 필요는 없지만, 원활한 진행을 위해서 파이썬 개발을 위해 만들어둔 프로젝트 폴더를 지정하여 저장해줍니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/jpype2.JPG" width="100%" height="70%">
</p>

VS Code 실행하고, 가상 환경을 실행합니다. (`. .venv/Scripts/activate`) 가상 한경이 실행되면, 아래 명령어를 입력합니다. 잠시 기다리면, 설치가 완료됩니다!
- 32비트 파이썬의 경우
> pip install JPype1‑0.6.3‑cp37‑cp37m‑win32.whl
- 64비트 파이썬의 경우
> pip install JPype1‑0.6.3‑cp37‑cp37m‑win_amd64.whl

## 패키지 설치
우리 강의에 최종 목표인 파이썬 크롤러 개발을 위해서, 우리는 기존에 잘 만들어진 여러 패키지를 활용합니다. 같은 기능을 할 수 있는 많은 패키지가 있지만, 원활한 진행을 위해 아래 패키지를 설치해주세요! (가상 환경이 실행되어 있지 않다면, 패키지를 설치하기 전에, 가상 환경을 실행해주세요.)

### requests
`requests` 패키지는 웹 자원 요청을 위한 다양한 기능을 제공하는 패키지입니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/vscode7.JPG" width="100%" height="70%">
</p>

아래 명령어를 입력해주세요.

> pip3 install requests

### bs4
`bs4` 패키지는 다양한 형식으로 웹 자원을 파싱(Parsing)하고, 분석할 수 있게 해주는 패키지입니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/vscode6.JPG" width="100%" height="70%">
</p>

아래 명령어를 입력해주세요.

> pip3 install bs4

### openpyxl
`openpyxl` 패키지는 엑셀 처리를 할 수 있는 패키지입니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/vscode8.JPG" width="100%" height="70%">
</p>

아래 명령어를 입력해주세요.

> pip3 install openpyxl

### numpy
`numpy` 패키지는 다양한 수학 관련 처리를 할 수 있는 패키지입니다. 강의에서 사용되는 패키지는 아니지만, `konlpy` 패키지 사용을 위해 필요합니다. (파이썬에서 자주 사용되는 패키지이므로, 설치해두면 두루두루 사용하는 경우가 생길 겁니다! :)

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/numpy.JPG" width="100%" height="70%">
</p>

아래 명령어를 입력해주세요.

> pip3 install numpy


### konlpy
`konlpy` 패키지는 한글 분석 및 처리를 할 수 있는 패키지입니다. 위의 `numpy` 패키지가 설치되지 않았다면, 에러가 발생할 수 있습니다. 설치 전에 `numpy` 패키지를 먼저 설치해주세요!

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/vscode9.JPG" width="100%" height="70%">
</p>

아래 명령어를 입력해주세요.

> pip3 install konlpy

이제 정상적으로 파이썬 코드를 실행할 준비가 되었는지 확인하기 위해서, 아래 코드를 입력합니다. 파이썬 파일을 아직 만들지 않으셨다면, `main.py` 파일을 만들어줍니다. 

```python
from bs4 import BeautifulSoup
from opnepyxl import load_workbook
from konlpy.tag import Okt
import requests

print("안녕하세요.")
```

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course01/static/import.JPG" width="100%" height="70%">
</p>

위 코드를 입력하고, 파일이 있는 경로에 들어갑니다. (`cd 경로`) 터미널에 `python main.py` 명령어를 입력합니다. 터미널에 에러 없이 "안녕하세요."가 잘 나오면 성공입니다!

지금은 위 코드가 어떤 의미인지 몰라도 괜찮습니다. 모듈과 패키지 강의 부분에서 자세하게 다루게 될 내용입니다. :) 지금은, 아무런 에러 없이 외부 패키지를 잘 불러왔고, 이를 활용해서 코드를 작성할 준비가 되었다는 점만 기억해주시면 됩니다! 
