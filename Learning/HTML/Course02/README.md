# HTML 구조
키워드 : [HTML](https://ko.wikipedia.org/wiki/HTML)

우리는 HTML 코드를 작성할 때 기본적으로 들어가는 문구를 작성하고 이걸 하나의 템플릿이라고 부르기로 했습니다. 사실, HTML 태그의 종류 중에 `<template>`이라는 전용 태그가 존재하는데 우리가 여기서 말하는 템플릿과는 전혀 다른 내용입니다!

그렇다면 HTML 템플릿을 어떻게 구성했는지 살펴보겠습니다.

## html 태그
html 태그는 해당 페이지의 모든 html 코드를 감싸는 태그로 모든 코드의 가장 바깥쪽에 작성했습니다.

`<html>html 코드</html>`

## head 태그
head 태그는 우리가 작성할 웹 페이지의 여러 가지 정보를 명시하는 역할을 하는 태그였고, html 태그 여는 태그 바로 밑에 작성했습니다.
```
<!doctype html>
<html> 
    <head>
        <meta charset="utf-8">
        <title>제목</title>
    </head>
</html> 
```
title 태그는 웹 페이지 탭 부분에 나타나는 제목 부분을 작성하는 역할을 하는 태그였습니다. 위 코드의 meta 태그의 charset과 관련된 내용은 HTML 속성 부분에서 정리하겠습니다. 

## body 태그 
body 태그는 실제로 우리가 클라이언트(사용자)에게 보여주고 싶은 내용(콘텐츠)을 작성하기 위해 구성하는 엘리먼트의 가장 바깥쪽에 작성해줍니다.

```
<!doctype html>
<html> 
    <head>
        <meta charset="utf-8">
        <title>제목</title>
    </head>
    <body>
        <!-- 엘리먼트 작성 -->
    </body>
</html> 
```

위 코드가 우리가 원하는 html 템플릿 코드였습니다. 또 하나! html 코드 작성 시 가장 먼저 `<!doctype html>`을 명시한다는 점 잊지 마세요!