# Javascript 마우스 이벤트
키워드 : [마우스 이벤트](https://www.w3schools.com/jsref/obj_mouseevent.asp)

웹 사이트에 방문한 클라이언트가 가장 많이 할 수 있는 액션은 마우스 커서로 할 수 있는 행동과 키보드로 할 수 있는 행동을 들 수 있습니다. 이번 장에서는 마우스 이벤트에 대해서 알아보도록 하겠습니다.

## 마우스 이벤트
우리는 이벤트에 대해서 얘기할 때 특정 엘리먼트를 클릭할 때 발생하는 이벤트인 `onclick` 혹은, `click`에 대해서 알아보았습니다. 이번 절에서는 더 다양한 마우스 관련 이벤트에 대해서 알아보겠습니다.

이벤트|의미
|:-:|:-:|
onclick|엘리먼트를 클릭할 때 발생하는 이벤트
ondbclick|엘리먼트를 더블 클릭할 때 발생하는 이벤트
oncontextmenu|마우스 우클릭으로 메뉴가 나타날 때 발생하는 이벤트
onmousedown|마우스 버튼을 클릭할 때 발생하는 이벤트
onmouseenter|엘리먼트로 마우스 커서가 올라갈 때 발생하는 이벤트
onmouseleave|마우스 커서가 엘리먼트를 벗어날 때 발생하는 이벤트
onmousemove|엘리먼트 안에서 마우스 커서가 움직이는 동안 발생하는 이벤트
onmouseover|마우스 커서가 해당 엘리먼트 혹은, 자식 엘리먼트에 올라갈 때 발생하는 이벤트
onmouseout|마우스 커서가 해당 엘리먼트 혹은, 자식 엘리먼트를 벗어날 때 발생하는 이벤트
onmouseup|엘리먼트를 클릭하고 땔 때 발생하는 이벤트

마우스 관련 이벤트가 꽤 많죠..?^^ 그만큼 마우스 관련 이벤트를 다양하게 처리할 수 있다는 것을 나타내는 것이라고 할 수 있습니다! 각각의 이벤트가 의미하는 바를 직접 코드로 작성하고 확인하는 시간을 가져보세요. :)

## preventDefault
우리가 공부하고 있는 모든 이벤트는 모두 사실 DOM 구조를 따르는 event '객체'입니다. 이벤트 객체라는 것은 결국 각각의 이벤트가 갖는 기본 속성(properties)과 메서드(Methods)를 사용할 수 있다는 의미입니다.

이벤트 객체에는 다양한 속성과 메서드가 존재합니다. 이번 절에선 자주 사용되는 이벤트 메서드인 preventDefault 메서드에 대해서  정리해보겠습니다.

우선, 아래와 같은 코드가 있다고 가정해보겠습니다.
- html
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>preventDefault 테스트</title>
    </head>
    <body>
        <input type="checkbox" id="test">
        <script type="text/javascript" src="js/main.js">
    </body>
</html>
```
- main.js
```javascript
document.getElementById("test").addEventListener("click", function(e){
    //1번 코드
    e.preventDefault();
}, false);
```
우선 위 코드는 `test`라는 이름의 아이디를 갖는 체크박스를 생성하고, 자바스크립트 코드로 addEventListener 메서드의 `click`이란 이벤트를 수신하고, 이벤트 객체의 preventDefault() 메서드를 호출하고 있습니다. 

preventDefault()는 이름에서 느껴지듯이, 엘리먼트가 갖는 기본 이벤트를 취소할 수 있습니다. 위 코드에서 1번 코드처럼 코드를 작성하면, 체크 박스의 클릭에 해당하는 기본 이벤트를 막을 수 있습니다. (체크 박스의 기본 이벤트는 체크 표시가 나타나고, 사라지는 것입니다.(Toggling)) 

단, 모든 이벤트의 기본 액션을 취소시킬 순 없습니다. 이벤트 취소가 가능한지 확인하기 위한 속성인 `cancelable`을 이용해서 논리 조건을 처리할 수 있습니다. (IE에서는 9.0 이상부터 지원)

이벤트 객체의 더 많은 속성과 메서드가 궁금하시다면 [여기](https://www.w3schools.com/jsref/obj_event.asp)를 참고해주세요.

마우스 이벤트는 이벤트 중에서도 굉장히 사용 빈도가 높은 이벤트입니다. 모든 마우스 관련 이벤트를 한 번에 다 기억할 필요 없이, 자연스럽게 익히실 수 있을 겁니다. 또한, 제가 다 언급해드리지 않은 이벤트 객체에 대해서도 더 깊이 학습해보세요! :)