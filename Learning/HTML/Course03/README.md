# HTML 관계
키워드 : [HTML](https://ko.wikipedia.org/wiki/HTML)

HTML은 HyperText Markup Language의 약자라는 점은 이미 함께 알아보았습니다. 여기서 "Markup"이라는 구조를 쌓는다는 의미는 굉장히 중요합니다. 이 안에는 다양한 의미가 들어있지만, 직접 코드를 작성하는 개발자 입장에서 바라볼 때 이 구조라는 것은 우리의 웹 페이지를 클라이언트(사용자)에게 어떻게 보여줄 것인가를 고민하는 과정이라고 할 수 있습니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course03/static/relation1.png" width="100%" height="70%">
</p>

```html
<!doctype html>
<html> 
    <head>
        <meta charset="utf-8">
        <title>제목</title>
    </head>
    <body>
    <!-- 부모 -->
        <div> 
            <!-- p 태그는 서로 형제 -->
            <p>div 태그의 첫 번째 자식</p>
            <p>div 태그의 두 번째 자식</p>
            <p>div 태그의 세 번째 자식</p>
        </div>
    </body>
</html> 
```

위 코드에서 div 태그는 범용 요소로서 p 태그들의 부모 태그가 되며, 반대로 p 태그는 자식 태그가 됩니다. 또한 각각의 p 태그는 하나의 div 부모 태그를 갖는 형제 태그라고 표현할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course03/static/relation2.png" width="100%" height="70%">
</p>

꼭 같은 종류의 태그가 아니더라도 하나의 부모를 기준으로 형제 태그의 종류는 서로 다른 여러 가지로 작성될 수 있다는 점도 함께 기억해주세요! 포함 관계를 구성하는 것은 HTML 코드를 작성하는 가장 기본적인 단위가 엘리먼트라는 점에서 다른 엘리먼트 안에 또 다른 엘리먼트를 계속해서 담아가는 과정을 이해하는 것은 굉장히 중요합니다! 

또한, 부모 엘리먼트를 자식 엘리먼트가 감싸는 것은 권장하지 않는다는 것도 꼭 기억해주세요!

