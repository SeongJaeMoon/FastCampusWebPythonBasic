# GET 방식 URL 분석하기

GET 방식은 검색을 위한 방식이고, 쿼리 문자열을 구성하여 해당 페이지의 정보를 나타냅니다. 반대로 말하면 GET 방식은 URL에 어떤 정보가 나타나게 되고, 그 정보는 보통 규칙성을 갖고 있을 수 있습니다. 왜냐하면, 해당 페이지의 개발자 입장에서도 어떤 규칙 없이 정보를 표현하면 본인조차도 정보를 관리하기가 너무 복잡해지기 때문입니다.

이 점을 통해서 특정 사이트의 URL을 분석해볼 수 있습니다. 이 규칙을 찾는 것은 우리가 파이썬 언어로 웹 크롤러를 개발할 때 필수적인 작업이기도 합니다. 

저는 예제 사이트로 [팟빵 사이트](http://www.podbbang.com/)의 URL을 간단히 분석해보도록 하겠습니다. 

우선 쿼리 문자열은 아래와 같은 방식으로 표현 된다는 점 기억해주세요!
> URL?KEY="VALUE"&KEY="VALUE"...

## 사이트 접속

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/get1.png" width="100%" height="70%">
</p>

[팟빵 사이트](http://www.podbbang.com/)를 검색해 접속합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/get2.png" width="100%" height="70%">
</p>

카테고리 중 순위를 클릭합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/url1.png" width="100%" height="70%">
</p>

현재 팟빵 사이트의 url은 GET 방식으로 나타나지 않습니다.

## URL 분석

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/get3-1.png" width="100%" height="70%">
</p>

페이지의 스크롤을 가장 밑까지 내리면 위 사진과 같이 페이지를 이동할 수 있습니다. 다음 페이지를 클릭합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/url2.png" width="100%" height="70%">
</p>

다른 페이지를 클릭하면, URL이 GET 방식으로 나타나는 것을 확인할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/url3.png" width="100%" height="70%">
</p>

또 다른 페이지를 클릭하면, 역시 GET 방식으로 나타나고 같은 KEY에 값이 조금씩 달라지는 것을 확인할 수 있습니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/chrome-development.png" width="100%" height="70%">
</p>

참고로, 개발자 도구의 Network 탭에서 해당 URL을 찾아서 클릭하면 "query string"이라는 탭에 키와 값 형태로 같은 결과를 확인 할 수 있습니다.

## 규칙 찾기

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course08/static/get3-2.png" width="100%" height="70%">
</p>

왼 쪽에서 오른 쪽으로 탭을 클릭할 때 마다 URL의 start 키의 값이 총 9 번 100 씩 증가하는 것을 확인할 수 있습니다. (만약, 날짜를 바꾸면 date에 해당하는 값도 달라지게 됩니다.) 이걸 수식으로 바꿔쓰면 다음과 같이 쓸 수 있습니다.

(100⋅0)+1, (100⋅1)+1, (100⋅2)+1,...(100⋅9)+1

이게 기초적인 GET 방식으로 표현된 URL을 분석하는 것이라고 할 수 있습니다.  

만약 GET 방식 쿼리 문자열 표현 방법이 잘 이해가 가신다면 자신이 좋아하는 어떤 사이트의 URL을 분석하는 작업을 진행해보세요 :)