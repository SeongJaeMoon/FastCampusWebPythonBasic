# Python 크롤러1 - 웹 사이트 분석
키워드 : [robots.txt](https://ko.wikipedia.org/wiki/%EB%A1%9C%EB%B4%87_%EB%B0%B0%EC%A0%9C_%ED%91%9C%EC%A4%80), [웹 크롤러](https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%81%AC%EB%A1%A4%EB%9F%AC)

우리의 강의 목표는 웹 클라이언트 개발 기초에 대한 공부와 파이썬 크롤러 개발의 관한 내용을 다루는 것이었습니다. 이번 장에서부터 마지막 장까지는 우리의 최종 목표인 크롤링과 관련된 내용을 정리해보도록 하겠습니다.

## robots.txt
우선, 검색 엔진과 `robots.txt`에 대해서 이야기하고 시작하도록 하겠습니다. 강의에서도 잠시 언급했듯이, 우리가 보는 포털 사이트와 여러 검색 엔진은 우리가 특정 키워드를 검색하면, 해당 검색어에 해당하는 웹 페이지를 미리 정의된 알고리즘에 따라서 '검색 봇'(Search Bot)이 웹 페이지를 찾고 우리에게 보여주게 됩니다. 

웹 사이트마다 검색 봇에게 잘 노출되길 희망하는 부분도 있겠지만, 특정 페이지나 디렉터리는 검색 노출이 되지 않길 희망할 수도 있습니다. 이번 절에서 살펴볼 `robots.txt`는 검색 봇에게 노출 허용, 노출 거부 등을 설정할 수 있는 텍스트 파일이라고 할 수 있습니다.

우리 말로는 '로봇 배제 표준'이라는 명칭으로 불리며, 검색 봇이 접근하는 것을 방지하기 위한 국제규약입니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/facambot.png" width="45%" height="100%">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/googlebot.png" width="45%" height="100%">
</p>

위 사진은 왼쪽에서부터, 패스트캠퍼스와 구글의 `robots.txt`을 나타냅니다. 위 사진에 나와있는 것 처럼, 최상위 도메인 주소(root)에 `/robots.txt`를 입력하면, 로봇 배제 표준을 확인할 수 있습니다.(`e.g., https://www.google.com/robots.txt`) 

국내 포털을 비롯한, 대부분의 웹 사이트가 이 로봇 배제 표준을 가지고 있습니다. `robots.txt`의 의미는 [여기](https://ko.wikipedia.org/wiki/%EB%A1%9C%EB%B4%87_%EB%B0%B0%EC%A0%9C_%ED%91%9C%EC%A4%80)를 참고해주세요.

이 규약은 권고안이며, 로봇이 `robots.txt `파일을 읽고 접근을 중지하는 것을 목적으로 합니다. 따라서 접근방지 내용을 작성하였다고 해도, 다른 사람들이 그 파일에 접근할 수 있습니다. 반대로 말하면, 위 권고안을 지키지 않을 경우엔 웹 사이트에서 접근 IP를 강제 차단할 수도 있습니다.

또한, `robots.txt`가 구성되어 있지 않거나 구체적으로 명시되어 있지 않다고 하더라도, 고유한 저작권이 없는 것은 아닙니다. 크롤링을 진행할 때, 가능하다면 최대한 `robots.txt`의 명시된 내용을 존중해주는 것이 좋습니다.

결론적으로, 공격적이고 악의적인 목적의 크롤링은 무조건적으로 **지양**되어야 한다는 점 말씀드리고 싶습니다.

## 테스트 크롤링 사이트 분석
이제 본격적으로 크롤링과 관련된 내용을 정리해보도록 하겠습니다. 우선, 크롤링할 사이트를 선택해야 합니다. 저의 경우 'NDSL'(National Digital Science Library)이라는 국가과학기술정보센터 사이트를 크롤링 테스트 사이트로 사용할 것입니다. 참고로 많은 분들이 이미 잘 아시겠지만, 해당 사이트는 다양한 논문 자료와 특허, 보고서 등을 확인할 수 있는 유용한 사이트입니다. :) 

> https://www.ndsl.kr/index.do

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/html0.png" width="100%" height="100%">
</p>

우선 해당 사이트에 접속하고, 원하는 키워드를 입력합니다. 저의 경우엔 '파이썬'이라고 입력했습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/html1.png" width="100%" height="100%">
</p>

99건의 논문 정보가 나오는 것을 확인할 수 있습니다. 우리는 앞으로 크롤링 코드를 통해서 논문의 제목과 초록을 가져오고 싶다고 가정하겠습니다. 계속해서, 스크롤을 가장 하단부까지 내려보겠습니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/html1_2.png" width="100%" height="100%">
</p>

이렇게 어떤 정보를 보여주는 웹 페이지는 대부분 페이징(Paging)이라는 것을 지원합니다. 즉, 하나의 페이지에 모든 정보를 볼 수 있는 것이 아니라, 사용자가 특정 버튼을 클릭해서 원하는 페이지로 이동하는 식으로 나눠서 보게 됩니다. HTML 과제였던 GET 방식 URL 분석을 기억하고 계신다면, 익숙한 내용이실 겁니다. :)

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/html1_1.png" width="100%" height="100%">
</p>

크롤링 코드를 작성할 때 중요하게 생각할 부분 중 하나가 바로 자동화입니다. 반복문을 통해서 원하는 정보를 자동으로 가져올 수 있도록 작성하려면, 반복문을 어떻게 적용할 수 있을지 확인해야 합니다. 가장 기본은, 웹 사이트가 어떻게 정보를 보여주는지 확인하는 작업입니다.

위 사진은, 크롬 개발자 도구 메뉴 중 `Network` 탭을 클릭하여, 가장 상단에 있는 주소를 클릭했을 때 나오는 사진입니다. (Recording network activity...라는 화면이 나오면 새로 고침 해주세요!)

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/page1.png" width="45%" height="100%">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/page2.png" width="45%" height="100%">
</p>

이제 `Headers` 탭에서 스크롤을 가장 하단으로 내리면, `Query String Parameters`라는 탭이 나옵니다. 여기서 현재 보고 있는 웹 페이지의 쿼리 문자열을 확인할 수 있습니다. 위 사진은 1 페이지에서 2 페이지로 이동했을 때, 쿼리 문자열 값이 변하는 것을 확인하는 사진입니다. 다른 값은 모두 변하지 않지만, `page` 값만 변하는 것을 확인할 수 있습니다. 이 정보를 잘 이용하면, 코드 상에서 페이징 작업을 진행할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/a.png" width="100%" height="100%">
</p>

위 정보를 가지고서 크롤링 코드를 작성하기 전에, 우리가 가져올 HTML 구조를 파악해야 합니다. 먼저, 개발자 도구를 통해서 제목은 어떤 형태로 이루어져 있는지 확인합니다.

>  #result_list > li:nth-child(1) > div.list_con > p.title > a


<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Python/Course11/static/p.png" width="100%" height="100%">
</p>

제목과 마찬가지로, 개발자 도구를 통해서 초록은 어떤 형태로 이루어져 있는지 확인합니다.

> #result_list > li:nth-child(1) > div.list_con > div:nth-child(4) > p:nth-child(2)

참고로, 선택자 문법 안에 `nth-child()`라는 선택자 문법이 있으면, HTML 태그를 가져올 때 다소 까다로운 점이 존재한다는 것을 의미합니다. 우리가 이번 장에서 눈여겨볼 점은, 우리가 찾으려는 태그의 값이 클래스 속성이 `list_con`인 `div` 태그에 자식으로 묶여있는 것을 확인할 수 있습니다. 

이 정보를 가지고 어떻게 태그의 콘텐츠를 추출하는지에 대한 내용은 특정 콘텐츠만 추출하는 부분에서 집중적으로 다루도록 하겠습니다.  

이번 장에서는 크롤링 테스트를 진행할 사이트를 선정하고, 간단히 사이트 분석에 대한 내용을 알아보았습니다. 제가 크롤링 예시로 보여드릴 사이트가 아닌 원하는 다른 사이트가 있으시다면, 원하는 사이트에 정보를 분석하시고, 크롤링 테스트를 시도하시면 됩니다. 

단, 크롤링 테스트 사이트를 선정하실 때 한 가지 주의하실 점이 있습니다. 포털 사이트의 댓글 정보나 우리가 흔히 'SNS'라고 말하는 소셜 미디어와 같은 동적으로 정보를 가져와 보여주는 페이지의 경우엔 강의에서 다루는 내용만 가지고는 크롤링 하기에 어려움이 있습니다. 예를 들어, '페이스북', '트위터'와 같이 하나의 페이지에서 마우스 스크롤을 내리는 행동을 인지하여 새로운 정보를 추가로 보여주는 페이지 등을 말합니다. 

저의 경우엔 다양한 사진을 무료로 제공하는 사이트인 [wallpaperscraft](https://wallpaperscraft.com/)라는 사이트와 강의에서 보여드린 [Fastcampus](https://www.fastcampus.co.kr/dev_online_introdev/) 사이트로 크롤링 테스트 코드를 작성하시는 것을 추천드립니다.