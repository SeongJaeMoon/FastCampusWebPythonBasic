# CSS 스타일
키워드 : [박스모델](https://www.w3schools.com/css/css_boxmodel.asp)

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course03/static/boxmodel.png" width="100%" height="100%">
</p>

CSS를 이야기할 때 빼놓지 않고 등장하는 내용이 이 번 장에서 다룰 박스 모델(Box Model)이라는 것입니다. 박스 모델은 우리가 웹 페이지에 보여줄 콘텐츠의 영역을 다룰 때 사용되는 아주 중요한 부분입니다. 

이 박스 모델은 이름 그대로 내용을 네모 모양의 박스로 감싸는 형태로 나타내게 됩니다. 박스 모델은 다음과 같이 크게 네 가지로 구성되게 됩니다. 

**박스 모델** 
> 콘텐츠(Contents): 실제 내용이 나타나는 부분 

> 보더(Border): 내용과 일정 부분 떨어진 위치에서 내용을 감싸고 있는 테두리 

> 패딩(Padding): 내용과 테두리 간의 간격 

> 마진(Margin): 엘리먼트 간의 간격 

우리가 HTML 부분에서 화면 설계를 이야기할 때 레이아웃(Layout)이라는 것에 대해서 알아봤습니다. 레이아웃을 구성할 때 이 박스 모델을 적절하게 이용하면 배경화면이 나타나는 부분, 사진이 나타나는 부분 등을 적절하게 구분할 수 있습니다 :) 

## width, height 
처음 CSS가 등장했을 때는 콘텐츠의 영역의 크기만을 계산하여 너비(width)와 height(높이)를 계산하였습니다. 그렇기 때문에 너비와 높이 속성 값은 콘텐츠의 크기만을 조절할 수 있습니다. 

하지만, 콘텐츠가 갖는 실제 너비와 높이는 콘텐츠의 너비와 높이에 패딩과 보더 값을 더해서 계산을 해야 합니다. 예를 들어 다음과 같은 코드가 있다고 가정해보겠습니다. 
```html
<!-- 스타일 적용 -->
<style>
p {
    border: 10px solid red;
    padding: 10px;
    width: 100px;
    height: 100px;
}
</style>
<!-- p 태그 작성-->
<p>p태그</p>
```
<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course03/static/box1.png" width="70%" height="70%">
</p>

코드를 실행하면 위 사진과 같이 브라우저에 나타나게 됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course03/static/box2.png" width="70%" height="70%">
</p>

콘텐츠를 크롬 개발자 도구의 검사 기능을 통해서 확인해보겠습니다. 위 사진과 같이 실제 콘텐츠의 너비와 높이는 100(px) x 100(px)으로 나타납니다. 하지만, 실제 p 엘리먼트가 차지하는 영역은 **너비: 100(width) + 20(좌,우 패딩) +20(좌,우 보더)**, **높이: 100(height) + 20(상,하 패딩) + 20(상,하 보더) + 32(기본 마진)** 인 것을 확인할 수 있습니다. 

(height 프로퍼티는 콘텐츠의 높이에 따라 자동으로 늘어나거나 줄어듭니다. 그렇기 때문에, 특별한 경우가 아니면 높이 값은 지정하지 않아도 됩니다!)

```html
<!-- 스타일 적용 -->
<style>
p {
    width: 100%;
}
</style>
<!-- p 태그 작성-->
<p>p태그</p>
```
또한, 너비와 높이는 위 코드처럼 퍼센트(%)로도 지정할 수 있습니다. 이렇게 퍼센트로 지정하게 되면 해당 요소가 갖는 콘텐츠 너비의 크기가 브라우저를 기준으로 비율에 맞게 요소가 조절 됩니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course03/static/50.png" width="100%" height="70%">
</p>

<p align="center">width: 50%; border 10px;</p>

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course03/static/70.png" width="100%" height="70%">
</p>


<p align="center">width: 70%; border 10px;</p>

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course03/static/100.png" width="100%" height="70%">
</p>


<p align="center">width: 100%; border 10px;</p>

너비값을 브라우저 전체를 사용하게 할 경우(100%) 테두리가 차지하는 크기가 있기 때문에 화면을 벗어나는 영역이 나타나는 것도 알 수 있습니다. 이 부분도 필요에 따라 자주 사용할 수 있는 부분이니 콘텐츠가 어떻게 변화하는지 직접 코드를 작성해보고 브라우저 크기를 줄였다 늘렸다 하면서 직접 눈으로 확인해보세요!

만약, 생각했던 영역보다 특정 엘리먼트가 갖는 영역이 작거나 넓다면, 마진과 패딩 등 다른 속성이 갖는 크기도 함께 생각해보세요!

## 영역 설정
다음으로, 영역 설정에 대해서 예를 들어보겠습니다. 
```html
<!-- 스타일 적용 -->
<head>
    <style>
        div#box{
            margin:auto;
            width:800px;
            border: 10px solid blue;
        }
    </style>
</head>
<!-- 스타일을 적용한 부모 요소로 태그 감싸기 -->
<body>
    <div id="box">
        <h1>제목</h1>
        <p>문단</p>
        <!-- 엘리먼트 구성... -->
    </div>
</body>
```

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course03/static/layout.png" width="100%" height="100%">
</p>

코드를 실행하면 위 사진과 같이 브라우저에 나타나게 됩니다. 

우선 css 코드의 내용을 살펴보면 id 가 box인 div 태그에 마진 값을 auto로 지정하고, 너비 값을 800px로 제한했습니다. 그리고 해당 영역을 둘러싸는 부분을 표현하기 위해 보더를 지정했습니다. 가장 바깥쪽 부모(div) 요소의 마진을 auto로 지정하고, 너비 값을 조절하면 위 사진처럼 부모 요소를 가운데 정렬한 것과 같은 효과를 주고, 그 안에 엘리먼트를 담을 수 있습니다. 

이처럼 영역을 나타낼 부모 요소(일반적으로 div)의 크기를 조절하여 레이아웃을 설정하고 그 안에 자식 요소들을 담는 형태로 콘텐츠를 구성하면 콘텐츠들이 나타날 영역을 구분 짓는데 훨씬 수월하다는 점도 참고해주세요! 

끝으로, 콘텐츠를 다양한 방법으로 배치하기 위한 CSS 속성은 굉장히 다양합니다. 개인적으로 생각하는 중요도와 난이도에 따라서 부분적으로 구성한 부분이 있으니, 배치와 관련된 더 다양한 CSS 속성에 대해서 궁금하시다면 [여기](https://www.w3schools.com/css/css_positioning.asp)와 [여기](https://www.w3schools.com/css/css_float.asp)를 참고해주세요!
