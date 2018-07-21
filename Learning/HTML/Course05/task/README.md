# 화면설계(레이아웃 구성하기)
화면 설계는 실제 웹 페이지를 제작 하기 전에 여러가지 툴을 이용해서 프로토타입을 작성하는 작업을 이야기합니다. 우리가 실제 그림을 그리기 전에 간단하게 그림의 스케치를 그리는 것을 웹 페이지에 똑같이 적용한다고 생각하면 이해하기 편할 것 같습니다.

이러한 화면 설계 툴은 굉장히 여러가지가 있습니다. 제가 추천 드리는 프로그램은 크게 두 가지입니다. 하나는 [발사믹 목업](https://balsamiq.com/products/)이라는 것이고, 다른 하나는 [카카오 오븐](https://ovenapp.io/)입니다. 

둘 모두 웹 상에서 작업하고 편하게 저장할 수 있는 장점이 있지만, 저는 처음 사용하시기엔 카카오에서 제공하는 오븐이 더 접근성이 높을 거라고 판단하여 카카오 오븐을 사용하는 걸 추천 드리겠습니다. (다른 웹 페이지 화면 디자인 프로그램을 사용하셔도 무방합니다.)

## 카카오 오븐 시작하기

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/layout1.png" width="100%" height="70%">
</p>

[카카오 오븐 사이트](https://ovenapp.io/)에 접속하고 회원 가입을 진행하고, "새로운 프로젝트를 만들기"를 클릭합니다.

## 새로운 프로젝트 만들기

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/layout2.png" width="100%" height="70%">
</p>

"새로운 프로젝트를 만들기"를 클릭하면 위와 같은 화면이 나타납니다. 프로젝트 이름과 설명 등을 작성하고 화면 크기는 PC로 선택해줍니다.

## 화면 디자인

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/layout3.png" width="100%" height="70%">
</p>

프로젝트를 생성하면 위와 같이 작업 영역이 나타나게 됩니다. 오른쪽 빨간색 테두리로 둘러쌓인 부분에 있는 여러가지 요소나 사진 등을 드래그 해서 파란색으로 둘러쌓여진 부분에 가져다 놓고 원하는 디자인으로 변경합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/layout4.png" width="100%" height="70%">
</p>

우리는 자기소개 화면 페이지를 구성할 것이므로, 다음과 같이 본인이 원하는 자기소개 화면 페이지를 구성합니다.

## HTML Layout

HTML 코드를 통해 화면을 구성하는 방법을 보통 Layout이라고 부릅니다. 화면 전체를 하나의 큰 사각형으로 지정하고, 그 안에 콘텐츠별로 작은 사각형의 영역을 배치합니다. (이러한 영역과 영역 사이에는 약간의 공백 지정 필요합니다.)

레이아웃을 구성하기 위해 HTML5에서 사용하는 태그는 크게 8가지가 존재합니다.

1. `<header>` - 웹 페이지의 가장 상단 부분의 영역을 정의합니다.
2. `<nav>` - 웹 페이지의 네비게이션 영역을 정의합니다.
3. `<section>` - 웹 페이지의 섹션 영역을 정의합니다.
4. `<article>` - 웹 페이지의 독립적인 자체 영역을 정의합니다.
5. `<aside>` - 웹 페이지의 사이드바 영역을 정의합니다.
6. `<footer>` - 웹 페이지의 가장 하단 부분의 영역을 정의합니다.
7. `<details>` - 상세 보기 기능을 추가합니다.
8. `<summary>` - `<details>` 엘리먼트의 내용을 정의합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/layout5.png" width="100%" height="70%">
</p>

레이아웃 생각하고 다시 화면 디자인 부분을 살펴보면, 위 사진처럼 각각의 영역을 분리해서 설계할 수 있다는 것을 알 수 있습니다.

아래 코드는 레이아웃 태그를 적용한 HTML 예시 코드입니다.
```html
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>SIST_쌍용교육센터</title>
    </head>
    <body>
        <div class="container">
            <header>
                <img src="img">
                <h1>About me</h1>
            </header>
            <nav>
                <ul>
                    <li><a href="#">About me</a></li>
                    <li><a href="#">Click here more</a></li>
                </ul>
            </nav>
            <section>
                <h2>Suwon, Republic of Korea, 문성재</h2>
                <p>안녕하세요. 저의 이름은 문성재입니다.</p>
            </section>
            <footer>Copyright &copy; Seongjae Moon.</footer>
        </div>
    </body>
</html>
```

자기소개 페이지를 어떻게 구성할 것인지 디자인하고, 또 레이아웃은 어떻게 구분 지을지 등에 대해서 생각하는 시간을 가져보세요! :)