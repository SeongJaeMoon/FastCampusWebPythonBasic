# background 이미지 사용하기
키워드 : [background 이미지](https://www.w3schools.com/cssref/pr_background-image.asp), [full 페이지](https://www.w3schools.com/howto/howto_css_full_page.asp)

CSS에 대한 전반적인 내용의 이해를 가지고 약간의 CSS 응용을 해보도록 하겠습니다. 결론적으로 이미지 풀 페이지라는 것을 만들어 보겠습니다. 

우선, 이미지를 활용해 풀 페이지를 구성한 사이트를 한 번 살펴보겠습니다. 아마 보시면 바로 "아~" 하실 거라 생각됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course04/static/63.png" width="100%" height="70%">
</p>

눈치채셨겠지만, 위 사이트는 63 빌딩을 소개하는 사이트입니다. 화면의 뒷 배경 부분을 화려한 이미지가 둘러싸고 있는 것을 확인할 수 있습니다. 보통, 회사 소개 페이나 광고 페이지 등에서 이렇게 후면을 커다란 이미지로 가득 채우고, 그 위에 콘텐츠를 쌓는 방식을 사용하곤 합니다.

간단하게 한 번 직접 만들어 보도록 하겠습니다. 
## 사진 준비
우선 화면을 가득 채울 사진이 필요합니다. 사진은 png 혹은 jpg 확장자를 갖는 이미지를 준비합니다. (크기가 너무 작은 사진인 경우 화면을 가득 채우는 과정에서 깨지는 현상이 발생할 수 있습니다.)

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course04/task/img/cat.jpeg" width="70%" height="70%">
</p>

저 같은 경우엔 제 지인이 키우는 고양이인 "껌껌이"로 배경 화면을 가득 채워보도록 하겠습니다. (아주 귀엽죠?)

## 폴더 구성
우리는 폴더를 구분해서 의미 있는 것들끼리 따로 파일별로 모으는 것을 권장하기로 했습니다.

우선 폴더 구성은, index.html 파일을 기준으로 css, img라는 이름으로 하위 폴더를 만들고 css 폴더에 main.css라는 이름으로 css 파일을 만듭니다. img 폴더엔 원하는 사진을 가져다 놓습니다.

## 코드 작성

### html

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>css 스타일 상속</title>
        <!-- css 주소 연결 -->
        <link rel="stylesheet" type="text/css" href="css/main.css">
    </head>
    <body>
       <div>
           <!-- p태그 안에 a태그 포함 -->
           <p><a href="https://seongjaemoon.github.io/" target="_blank">Read my blog</a></p>
       </div>
    </body> 
</html>
```
우선 html 코드는 위와 같이 구성해줍니다. a태그에 설정할 수 있는 속성 중 target이란 속성이 있습니다. 이 속성 값을 "_blank"라고 선언하면, 기존의 창이 아닌 새로운 탭이 열리면서 해당 url로 이동합니다. 사실, html 코드는 우리가 이미 잘 알고 있는 부분입니다.

### css

```css
html {
    /* background 이미지 설정 */
    background-image: url("../img/cat.jpeg");
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
    /* 이미지 크기 설정(꽉 차게) 너비, 높이 */
    background-size: 100% 100%; 
}
```
css 코드를 구성하는게 조금 생소한 프로퍼티가 등장해서 어렵게 느껴지실 수 있지만, 전혀 어려울게 없습니다! 

1. 우선 "background-image" 프로퍼티를 이용해서 배경 이미지 파일 주소를 연결합니다.
2. "background-attachment" 프로퍼티의 값을 "fixed(고정)"로 설정하면 스크롤이 생기지 않습니다.
3. "background-position" 프로퍼티의 값을 "center(가운데)"로 설정하면 이미지가 가운데로 위치합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course04/static/no-repeat.png" width="100%" height="70%">
</p>

4. "background-repeat" 프로퍼티는 기본 값이 "repeat"(반복)입니다. 그렇기 때문에, "no-repeat"로 값을 설정해주지 않으면 이미지의 반복이 일어납니다.
5. "background-size" 프로퍼티가 중요한데요, 너비와 높이 속성을 100%씩 적용합니다. 그러면, 브라우저의 크기가 줄어들어도 그 비율을 유지하게됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course04/static/full_page_size.png" width="100%" height="70%">
</p>

<p align="center">브라우저의 너비를 줄여도 이미지의 비율이 유지됩니다.</p>

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course04/static/full_page.png" width="100%" height="70%">
</p>

저는 p태그와 a태그에 몇 가지 스타일을 적용해서 위 화면처럼 나타나게 했습니다. 여러분이 좋아하는 사진을 가지고 직접 전체 화면을 가득 채우는 페이지를 만들어보세요! 그리고 그 위에 여러 엘리먼트를 구성해서 다양하게 표현해보세요! (참고로 background-image는 body태그 보다는 html태그를 기준으로 작성하는 것이 브라우저 높이를 맞추는데 도움이 됩니다!)