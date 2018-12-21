# 블록, 인라인 엘리먼트
키워드 : [블록 엘리먼트](https://www.w3schools.com/html/html_blocks.asp), [인라인 엘리먼트](https://www.w3schools.com/html/html_blocks.asp)

HTML 엘리먼트는 대표적인 특징에 따라 크게 두 가지로 나눠볼 수 있습니다. 바로, 블록(Block-level Element)과 인라인(Inline-level Element)으로 나눌 수 있습니다.

## 블록 엘리먼트
<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/block.png" width="100%" height="70%">
</p>
블록 엘리먼트의 종류는 더 다양하게 있지만 위의 태그가 대표적인 블록 엘리먼트라고 할 수 있습니다.

대표적인 블록 엘리먼트의 특징은 다음과 같습니다.
>1. 자동 줄바꿈이 일어난다.
>2. 블록 요소를 포함 할 수 없다.(범용 요소는 예외 존재)
>3. 인라인 요소는 자식으로 포함할 수 있다.
## 인라인 엘리먼트
<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/inline.png" width="100%" height="70%">
</p>
인라인 엘리먼트의 종류는 더 다양하게 있지만 위의 태그가 대표적인 인라인 엘리먼트라고 할 수 있습니다.

대표적인 인라인 엘리먼트의 특징은 다음과 같습니다.
>1. 자동 줄바꿈 속성이 없다.
>2. 블록 요소를 포함할 수 없지만, 인라인 요소는 포함할 수 있다.

## 그룹 요소(Grouping tags)
HTML 태그 중에는 `<div>`와 `<span>`이라는 다른 태그를 그룹화하기 위해 자주 사용하는 두 가지 중요한 태그가 있습니다. `<div>`태그의 경우 범용 요소로 다른 요소들의 부모 역할을 한다고 말씀드렸는데요, 그렇다면 그룹화라는 것이 무언인지 알아보겠습니다. 

### `<div>`
우선 `<div>`태그는 여러 다른 HTML 요소들을 그룹화하고 요소 그룹에 CSS(스타일)를 적용하는 데 매우 중요한 역할을 하는 블록 요소입니다. `<div>`태그를 사용하여 페이지의 다른 부분 (Left, Right, Top 등)을 정의하는 웹 페이지 레이아웃을 만드는 데 사용할 수 있습니다. 이 태그는 블록에 시각적인 변화를 주지는 않지만 CSS와 함께 사용하면 더 의미가 있습니다. 

예를 들어, 다음과 같은 코드가 있다고 가정해보겠습니다.
```html
<!DOCTYPE html>
<html>
   <head>
        <meta charset="utf-8"/>
        <title>HTML div</title>
   </head>
   <body>
      <!-- 첫 번째 그룹 -->
      <div style = "color:red">
         <h1>제목1</h1>
         <p>문단1</p>
      </div>
      <!-- 두 번째 그룹 -->
      <div style = "color:green">
         <h1>제목2</h1>
         <p>문단2</p>
      </div>
   </body>
</html>
```
위 코드의 내용 중 `style` 부분은 콘텐츠의 문자 색을 변경하는 코드이며 CSS 파트에서 볼 수 있는 내용입니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/ret1.PNG" width="50%" height="70%">
</p>

코드를 실행하면 위와 같은 결과가 나오는데요, 눈 여겨볼 점은 첫 번째 그룹과 두 번째 그룹의 `<h1>`태그와 `<p>`태그가 각각 빨간색, 초록색으로 변경된 점입니다. 참고로 이렇게 부모 요소에 적용한 스타일을 자식 요소들이 물려받고, 영향을 받는 형태를 일반적으로 스타일 상속이라고 부릅니다.

### `<span>`
다음은 `<span>`태그인데요, `<span>`태그는 인라인 요소이며 HTML 문서의 인라인 요소를 그룹화하는 데 사용할 수 있습니다. 이 태그는 `<div>`태그와 마찬가지로 블록에 시각적인 변경을 제공하지 않습니다.

`<span>`태그와 `<div>`태그의 차이점은 `<span>` 태그가 인라인 요소와 함께 사용되는 반면 `<div>`태그는 블록 수준 요소와 함께 사용된다는 것입니다. 물론, `<div>`태그는 범용 요소이기 때문에 모든 요소를 담을 수 있지만, `<span>`태그는 인라인 요소만 담습니다.

예를 들어, 다음과 같은 코드가 있다고 가정해보겠습니다.
```html
<!DOCTYPE html>
<html>
   <head>
        <meta charset="utf-8"/>
        <title>HTML span</title>
   </head>
   <body>
      <div style = "color:red">
         <h1>제목1</h1>
         <p>문단1<span style="color:black">블랙!</span></p>
         <p>문단1
             <span style="color:black">
                <sup>블랙!</sup><strong>블랙!</strong>
             </span></p>
      </div>
   </body>
</html>
```
<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course05/static/ret2.PNG" width="50%" height="70%">
</p>

코드를 실행하면 위와 같은 결과가 나오는데요, 눈 여겨볼 점은 `<span>`태그로 감싼 인라인 요소들은 검은색으로 변경된 점입니다. 

이 뿐만 아니라, 각 요소의 추가적인 특징 부분이 더 있습니다. 그 부분은 CSS 박스 모델을 이야기하고 추가로 정리하도록 하겠습니다.

마지막으로, 엘리먼트의 종류는 굉장히 다양하므로, 먼저 속성과 마찬가지로 내가 구현하려는 웹 페이지의 구조를 생각하며 어떤 태그를 적용할 수 있을지 찾아봅니다. 다음으로 해당 태그가 블록 요소인지, 인라인 요소인지를 구분짓고 내가 원하는 모양으로 나올 수 있도록 생각합니다. 

대부분의 태그가 이름에서 어떤 역할을 하는 태그인지가 직관적으로 느껴집니다. 때문에 어떤 태그를 사용해야 내가 원하는 모양으로 페이지에 나타나게 될지는 코드를 조금만 작성하다 보면 자연스럽게 익히실 수 있을겁니다 :)
