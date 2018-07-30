# Javascript 렌더링 순서 이해하기

우리는 강의를 통해 자바스크립트 코드를 작성할 때, 두 가지 위치에 코드를 작성할 수 있다는 점에 대해 알아보았습니다.

첫 번째, `<head>` 엘리먼트에 작성하는 방법

```html
<!doctype html>
<html>
    <head>
        <meta charset = "utf-8">
        <title>Javascript 기초</title>
        <script type="text/javascript" src="js/main.js"></script>
    </head>
    <body>
        <p>안녕하세요.</p>
    </body>
</html>
```

두 번째, `<body>` 엘리먼트 제일 밑에 작성하는 방법
```html
<!doctype html>
<html>
    <head>
        <meta charset = "utf-8">
        <title>Javascript 기초</title>
    </head>
<body>
    <p>안녕하세요.</p>
    <script type="text/javascript" src="js/main.js"></script>
</body>
</html>
```

위 두 가지 방법의 가장 큰 차이점은, 웹 페이지를 보여주는 속도에 차이라고 할 수 있습니다. 일반적으로 script 코드를 브라우저가 해석하는 과정에서 웹 사이트가 사용자에게 보여지는 전체적인 속도가 저하될 수 있습니다.(코드가 짧을 경우에는 큰 차이가 안 느껴질 수 있습니다.. ^^)  

때문에 HTML 코드를 우선 해석하고 사용자에게 보여준 다음에 사용자 동작에 대한 반응이 이루어질 수 있도록 코드를 작성하는 방법인 `<body>` 엘리먼트에 작성하는 방법이 속도 향상을 위해 사용될 수 있습니다. 단, 애니메이션 효과, 광고 등 script 코드가 먼저 동작해야 하는 경우가 있습니다. 이럴 경우에는 `<head>` 엘리먼트에 작성됩니다.

또한, 우리가 Javascript 코드를 js라는 폴더를 구성해서 CSS 코드와 같이 외부(External) 파일 형태로 저장하고 불러오는 이유 중 하나도 이 속도라는 것과 관련이 있습니다.

자바스크립트 코드를 분리하는 이유는 크게 세 가지가 있는데요. 

1. HTML 코드와 분리해서 작성할 수 있습니다.
2. HTML 코드와 자바스크립트 코드의 유지보수가 더 수월합니다.
3. 캐시라는 것에 자바스크립트 코드가 저장되어 속도가 향상 될 수 있습니다.

위와 같은 이유로 대부분의 Javascript 코드는 외부 파일로 저장하고 사용합니다. 

단, 외부 파일 형식으로 저장해서 script 코드를 작성할 때는 `<script>` 태그를 작성하지 않습니다.

```Javascript
    //script 태그를 작성하지 않고, 바로 자바스크립트 코드를 작성합니다.
    document.write("안녕하세요.");
```

`<head>` 엘리먼트와 `<body>` 엘리먼트에 script 코드를 작성할 수 있다는 점과 이 둘의 차이점을 간략하게나마 기억해주세요 :)