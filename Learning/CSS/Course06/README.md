# CSS 추가 내용
키워드 : [CSS Position](https://www.w3schools.com/css/css_positioning.asp), [display 속성](https://www.w3schools.com/css/css_display_visibility.asp)

이번 장에서는 CSS 강의에서 다루진 않았지만 CSS 코드를 작성할 때 필요한 몇 가지 내용에 대해서 추가적으로 정리하도록 하겠습니다.

## CSS Position
우선, 기존의 CSS 속성에 대한 내용을 기억하고 계셔야 이해하시는 데 도움이 되실 겁니다. 엘리먼트는 크게 인라인 요소와 블록 요소로 나눠지며, 요소 별로 갖는 특징이 있었습니다. 

또한, CSS 박스 모델에서 각각의 엘리먼트는 마진, 패딩 등과 같이 콘텐츠를 나타내는 고유한 영역을 가지며, 이 크기를 조절할 수 있다고 알아보았습니다.

이번 절에서 살펴볼 포지션은 박스 모델의 내용을 확장하여 각각의 엘리먼트의 위치를 어떻게 결정할지 구체적으로 명시하는 방법이라고 할 수 있습니다. 

포지션 속성은 다음과 같습니다.

속성|의미
:-:|:-:
static|지정하지 않은 기본값
relative|현재 위치를 기준으로 상대위치를 지정(상대 위치)
fixed|스크린을 기준으로 위치 고정
absolute|body 또는 박스를 기준으로 위치를 지정(절대 위치)

위의 표 내용 중에 static 속성은 우리가 CSS 코드의 `position` 속성을 지정해주지 않으면, 기본값으로 설정됩니다. 다음으로, 포지션 속성의 전용 프로퍼티에 대해서 알아보겠습니다.

속성|의미
:-:|:-:
top|위쪽 여백을 지정
bottom|아래쪽 여백을 지정
left|왼쪽 여백을 지정
right|오른쪽 여백을 지정

우선 위 표의 내용은 포지션 속성과 함께 사용되는 속성들이라고 할 수 있습니다. 포지션 속성이 정해진 상태에서, 각각의 속성을 기준으로 여백을 지정할 수 있습니다. 

```css
<style>
    p {
        position: relative;
        right: 0px;
        bottom: 0px;
    }
</style>
```
예를 들어, 위와 같은 코드를 작성하면, 오른쪽 여백과 바닥 여백이 `0px`이므로 오른쪽 하단에 `p` 요소가 나타나게 됩니다. 

### overflow 속성
oveflow 속성은 요소에 내용이 넘칠 경우에 넘치는 내용을 어떻게 처리할지 결정하는 속성입니다.

속성|의미
:-:|:-:
hidden|넘치는 내용을 숨길때 사용
auto|내용이 넘칠때는 스크롤바가 생기고, 넘치지 않을 때는 스크롤바를 숨김
scroll|내용과 상관없이 무조건 스크롤 생성

### z-index
z-index 속성은 요소가 위, 아래로 이동하거나 또는 정렬시킬 때 사용합니다. 기본값은 auto이며, 값이 클수록 요소가 위로 올라갑니다. z-index 속성은 일반적으로 postion 속성인 relative, absolute 속성이 적용된 상태에서 사용해야 합니다.

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>z-index</title>
        <style>
            img {
                position: absolute;
                left: 0px;
                top: 0px;
                z-index: -1;
                width: 300px;
                height: 300px;
            }
            p {
                color: white;
            }
        </style>
    </head>
    <body>
        <img src="cat.jpeg">
        <p>고양이</p>
    </body>
</html>
```
예를 들어, 위와 같이 `img` 엘리먼트의 `z-index` 속성의 값을 -1로 줄 경우에 이미지 위에 `p` 엘리먼트를 나타나게 할 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course06/static/test1.png" width="100%" height="70%">
</p>

## display 속성
display 속성은 요소의 성격을 바꿀 때 사용합니다. 속성 값은 다음과 같습니다.

속성|의미
:-:|:-:
inline|블록 요소를 인라인 요소로 바꿈
block|인라인 요소를 블록 요소로 바꿈
inline-block|요소를 인라인 블록 요소로 바꿈
none|요소를 숨길 때 사용

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>inline</title>
        <style>
            div#container p{
                display: inline;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <p>문단 태그</p>
            <p>문단 태그</p>
            <p>문단 태그</p>
        </div>
    </body>
</html>
```
예를 들어, 위와 같이 코드를 작성할 경우에 `p` 엘리먼트의 블록 속성이 인라인 속성으로 변경되어 한 줄에 나란하게 문단 태그를 나타낼 수 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course06/static/test2.png" width="100%" height="70%">
</p>


위의 내용 말고도 CSS 코드를 작성할 때 사용할 수 있는 속성은 굉장히 다양합니다. 모든 내용을 기억하고 사용할 수 있으면 좋겠지만, CSS 스타일을 적용하는 일은 생각보다 까다롭습니다. 한 번에 모든 내용을 적용하려고 하기보다는, 코드를 조금씩 수정해 나가며 내가 원하는 스타일을 적용하기 위한 코드를 많이 작성해보세요. :)