# CSS 선택자
키워드 : [CSS 선택자](https://www.w3schools.com/cssref/css_selectors.asp)

CSS를 공부할 때 필수적으로 알아야 하는 내용이지만, 생각보다 익숙해지는데 시간이 걸리는 내용이 바로 이 CSS 선택자 문법 사용인데요. 그렇다면, CSS 선택자 문법에 대해서 정리해보도록 하겠습니다.

우리는 기본적으로 총 네 가지 선택자 문법을 공부했습니다. 

**선택자 문법**
> "부모 엘리먼트 <선택자> 자식 엘리먼트"

```css
    div p{
        color: red;
    }
```
첫 째, "자손 선택자"는 위 코드처럼 div 엘리먼트 안에 작성된 모든 p 엘리먼트를 선택해서 색을 변경하는 예시입니다.

```css
    div > p{
        color: red;
    }
```
둘 째, "자식 선택자"는 위 코드처럼 div 엘리먼트 안에 작성된 바로 하위 자식으로 있는 p 엘리먼트만을 선택해서 색을 변경하는 예시입니다.
```css
    div + p{
        color: red;
    }
```
셋 째, "인접 형제 선택자"는 위 코드처럼 div 엘리먼트 안에 가장 가까운 p 엘리먼트를 찾아서 하나만 색을 변경하는 예시입니다.
```css
    p ~ span{
        color: red;
    }
```
넷 째, "일반 형제 선택자"는 위 코드처럼 p 엘리먼트 안에 작성된 span 엘리먼트를 찾아서 모두 색을 변경하는 예시입니다.

단순히 엘리먼트 이름 뿐만 아니라, 아이디와 클래스 속성 등을 혼합해서 사용 가능하다는 점도 잊지 마세요!

강의에서는 위의 예시로 든 네 가지 선택자 문법만 다뤘습니다. 사실, 선택자 문법을 사용할 수 있는 범위는 굉장히 다양합니다. 필요에 따라서 다양한 엘리먼트를 선택할 필요가 있기 때문입니다. 이 장에선, 추가로 a 태그의 속성과 관련된 선택자 문법에 대해서 살펴보도록 하겠습니다!

우선 a 태그가 다음과 같이 작성되어 있다고 가정 해보겠습니다
```html
<a href="https://wwww.google.com">구글</a>
```
<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course02/static/atag.png" width="50%" height="50%">
</p>

a 태그는 위 사진처럼 사용자가 클릭해서 href 속성에 해당하는 주소를 방문한 경우 방문한 걸 나타내기 위해서 기존의 색에서 보라색으로 색상이 변경되게 됩니다.

만약, 방문 여부에 상관없이 색을 유지하고 싶다면 어떻게 해야할까요? 여기서 선택자 문법을 활용할 수 있습니다.
```html
<style>
    a:visited{
        color: black;
    }
</style>
```
위에서 사용된 콜론(:)은 "가상 선택자"라는 이름의 선택자 문법입니다. 동적으로 특정 요소를 선택해서 변경하고 싶을 경우에 사용할 수 있는 이 방법에는 굉장히 다양한 것들이 존재합니다.
```html
<style>
    a:hover {
        color: black;
    }
    a:link{
        color: black;
    }
    a:visited{
        color: black;
    }
</style>    
```
이런식으로 작성하면 사용자가 마우스를 a 태그 위에 올려 놓거나 방문하지 않은 링크 등에 대해서도 색을 일관되게 적용할 수 있습니다.

참고로, 개발자 도구를 활용하면 특정 엘리먼트를 찾아가기 위해서 어떤 선택자 문법을 거쳐야 하는지 확인 할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course02/static/selector1.png" width="100%" height="70%">
</p>

우리는 구글 사이트에 접속해서 메인화면에 나타나는 이미지에 접근하는 방법에 대해서 궁금하다고 가정해보도록 하겠습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course02/static/selector2.png" width="100%" height="70%">
</p>

우선 로고 이미지 위에 마우스를 올려 놓고 우클릭해서 나오는 메뉴 중에 "검사"를 클릭합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course02/static/selector3.png" width="70%" height="70%">
</p>

개발자 도구가 열리면 자동으로 구글 로고 이미지가 선택되어 있습니다. 마찬가지로 마우스 우클릭을 하여 나타내는 메뉴 중에 "Copy" 메뉴 위에 마우스를 올려 놓으면 여러 메뉴가 나타납니다. 이 중에서 "Copy selector"를 클릭합니다. 그러면 선택자 문법이 클립보드에 복사됩니다.

클립보드에 복사된 내용을 획인하면 `#hplogo`로 나타나는 것을 확인할 수 있고, 이는 hplogo라는 아이디 속성 값으로 해당 엘리먼트를 선택할 수 있는 것을 나타냅니다.

끝으로, 이 밖에도 더 다양한 선택자 문법이 존재하는데요. 선택자라는 것에 대한 기본적인 개념을 파악했으니, 추가적인 선택자 내용에 대해선 어렵지 않게 활용하실 수 있을 거라고 생각합니다! :) 

다양한 선택자 문법에 대해서 궁금하시다면 [여기](https://www.w3schools.com/cssref/css_selectors.asp)를 참고해주세요.