# Javascript 구조
키워드 : [Javascript](https://www.w3schools.com/js/default.asp), [DOM trees](https://www.w3schools.com/js/js_htmldom.asp), [HTML parsing](https://www.w3.org/TR/2011/WD-html5-20110113/parsing.html)

강의를 통해서 우리가 제작한 사이트가 사용자에게 보여지기 위해서 여러가지 과정이 필요하다는 것을 알아봤습니다. (쉬운게 없죠..? ^^) 그렇다면, 자바스크립트 코드의 동작과 DOM trees 라는 것에 대해서 간단히 살펴보겠습니다.

우선, 자바스크립트 코드를 HTML 문서에 바로 작성하기 위해선 아래와 같이 `<script>`태그를 작성하고 스크립트 태그 안에 자바스크립트 코드를 작성합니다.
```HTML
<head>
    <script type="text/javascript">
        // 자바스크립트 코드 작성
    </script>
</head>
```
외부 js 파일을 불러오기 위해선 `<script>`태그의 "src" 속성을 이용할 수 있습니다.
```HTML
<head>
    <script type="text/javascript" src="파일 주소"></script>
</head>
```
자바스크립트에서 주석 처리를 위해서 사용되는 기호는 HTML에서 사용되는 주석 기호와 차이가 있습니다. 

한 줄 주석의 경우 "//주석 내용" 형태로 작성하고, 여러 줄에 걸쳐 주석을 작성하고자 할 경우 "/* 주석 내용 */" 형태로 작성합니다.

```Javascript
    //한 줄 짜리 주석
    
    /*
    여러 줄의 주석
    여러 줄의 주석
    */
```

또한, 위 두 가지 방법은 head 태그에 작성되어 있지만, `<body>`태그의 가장 밑에 작성하는 방법도 있다고 함께 기억해주세요!

## HTML DOM

우선 DOM은 Document Object Model의 약자입니다. 이 DOM이라는 것은 W3C(World Widw Web Consortium)라는 여러가지 웹 표준을 정의하는 기구에서 제정한 하나의 표준입니다.

DOM은 쉽게 말해서 문서(Document)에 접근하는 방법을 정의한 것이라고 할 수 있습니다. 동적으로 문서에 객체(Object)에 접근해서 내용(Contents), 구조(Structure), CSS(Style) 등을 동적으로 제어할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course03/static/dom1.png" width="100%" height="70%">
</p>

결론적으로, HTML DOM이라는 것은 HTML의 모든 엘리먼트 하나하나를 객체(Object)로 인식하고, 특정 엘리먼트의 내용을 얻어오거나, 수정, 추가, 삭제 등을 할 수 있도록 제정된 방법이며, 웹 표준이라고 할 수 있습니다.



   