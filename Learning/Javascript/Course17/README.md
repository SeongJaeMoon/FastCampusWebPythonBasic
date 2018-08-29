# Firebase 배포하기
키워드 : [Web Developer Roadmap](https://github.com/kamranahmedse/developer-roadmap), [VS code Emmet](https://code.visualstudio.com/docs/editor/emmet)

Firebase 배포하기 참고 자료는 [여기](https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/tree/master/Learning/Javascript/Course17/task/)에서 확인할 수 있습니다.

이번 장에서는 웹 개발 기초 강의 마무리와 웹 개발과 관련된 몇 가지 내용에 대해서 소개하도록 하겠습니다.

## VS code emmet
우선 우리가 사용하는 개발 환경인 VS code는 `Emmet`이라는 기능을 사용할 수 있습니다. 이 `Emmet` 기능을 이용하면, 같은 역할을 하는 HTML 코드를 훨씬 짧은 코드로 작성할 수 있습니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/emmet.gif" title="Emmet" width="100%" height="70%">
</p>

위 화면에서 보이듯 느낌표(!) 하나만 입력하면 우리가 알고 있는 템플릿이 순식간에 자동으로 만들어집니다. 이 뿐만 아니라, 선택자 문법과 연산 기호를 통해서 여러 줄의 코드를 한 줄로 만들어 낼 수 있습니다. 

예를 들어, `ul>li.test*3`이라고 작성하면, 아래와 같은 코드를 만들어 낼 수 있습니다.
```html
<ul>
    <li class="test"></li>
    <li class="test"></li>
    <li class="test"></li>
<ul>
```
HTML 코드를 작성하는 데 어느 정도 익숙해지셨다면, Emmet 기능을 이용해서 더 빠르게 엘리먼트를 구성해보세요! VS code에서 Emmet 기능을 활용하는 더 자세한 설명은 [여기](https://code.visualstudio.com/docs/editor/emmet)를 참고해주세요. 

## Javascript 코딩 스타일 
우리가 코드를 작성할 때 여러 가지 측면을 고려하면서 작성해야 합니다. 혼자서 모든 걸 다 개발하지 않는 이상(혼자 개발할 때도 중요합니다!), 여러 사람이 하나의 프로그램을 동시에 개발하게 됩니다. 각자 맡은 파트를 열심히 코딩하고, 서로 코드 리뷰를 하는 시간을 갖기도 하며, 최종적으로 하나의 프로그램으로 통합하는 과정을 거치게 됩니다. 

어떤 프로그래밍 언어를 선택하는지, 혹은 어떤 팀에서 개발하는지에 따라서 코딩 스타일은 달라질 수 있습니다. 하지만, 기본적으로 모두가 베이스로 생각하고 코드를 작성하는 하나의 표준적인 코딩 스타일이 존재하지 않는 것은 아닙니다.

 처음 잡힌 코딩 스타일은 꽤나 오랜 시간 코드를 작성하는 데 영향을 끼치게 됩니다. 결국, 처음 코딩 스타일을 잘 습관 들여놓으면, 계속해서 보기 좋은 코드(Clean code)를 작성하는 데 도움이 됩니다. 

사소한 부분이지만, 자바스크립트 코드를 작성할 때 도움이 될 만한 코딩 스타일에 대해 간단히 정리해보도록 하겠습니다. 

1. 변수나 함수의 이름을 지을 때는(명명 규칙) `camelCase`라는 것을 준수합니다. 또한, 강의에서도 언급했듯이, 코드의 가독성을 높이기 위해 변수나 함수는 이름만 보고도 어떤 역할을 하는지 짐작할 수 있도록 작성하는 것이 좋다고 이야기했습니다. 뿐만 아니라, 변수나 함수의 이름을 `$`로 시작하지 않는 것이 좋습니다. (라이브러리 등을 사용할 때 에러가 발생할 수 있습니다.)

2. 상수(Constant)는 영문 대문자로 작성합니다.

3. 전역 변수를 많이 선언하지 않는 것이 좋습니다. 전역 변수는 잘 사용하면 효율이지만, 관리하기 어려운 경우가 더러 있습니다. 가능하다면 함수로 정의하고, 지역 변수로 선언하고 사용합니다.

4. 변수를 선언할 때 초기화하고 사용합니다. `(e.g., var x = 0;, var str = "";)`

5. 코드 중복이 생길 경우 하나의 변수 혹은, 함수로 정의하고 사용합니다. 예를 들어, 같은 엘리먼트를 탐색하는 DOM 객체가 있다면 하나의 변수로 선언하여 할당하고 사용하는게 효율적입니다.

6. 자바스크립트 코드를 외부 파일 (`external`) 형태로 불러올 때 `type` 속성은 작성하지 않아도 됩니다. `(e.g., <script src="js/main.js"></script>)`

7. 파일이름은 소문자로 작성합니다.

8. 주석은 항상 작성합니다.

이 밖에도 다양한 규칙들이 있습니다만, 위의 내용 정도만 잘 지키도록 노력해도 나머지 내용들은 자연스럽게 익숙해지실 거라 생각합니다! :)

## Roadmap
웹 개발 기초 강의 과정을 듣고 웹 개발을 더 공부하고 싶지만 어떤 것부터 공부해야 될지 막막한 분들을 위해 [Web Developer Roadmap](https://github.com/kamranahmedse/developer-roadmap)을 첨부합니다. 웹 개발자를 위한 커리어 로드맵이 깔끔하게 정리된 자료입니다. 해당 URL로 가시면, 웹 개발과 관련된 여러 가지 동향과 트렌드를 확인할 수 있습니다.

우리 강의 과정 중에는 자바스크립트 코드를 작성할 때 중요하지만 다루지 못한 부분도 있습니다. 다음 챕터에서 나오는 파이썬 파트에서 다루지 못한 개념들을 다루는 것도 있고, 그렇지 못한 것도 있습니다. 자바스크립트의 [호이스팅](https://www.w3schools.com/js/js_hoisting.asp)(Hosting), [클로저](https://www.w3schools.com/js/js_function_closures.asp)(Closure), [정규 표현 객체](https://www.w3schools.com/js/js_regexp.asp)(Regular Expression) 등이 대표적이라고 할 수 있습니다. 

제가 강의에서 다루지 않은 내용이라고 중요하지 않은 내용이 절대 절대 아니기 때문에, 꼭 어떤 내용들이 있는지 꾸준히 찾아보고 공부를 진행해주시길 부탁드립니다!! 또한, 제가 참고 자료 중간중간에 첨부해드린 URL의 내용들을 다 보실 수는 없겠지만, 시간이 되신다면 제가 첨부해드린 참고 URL도 확인해주시면 좋겠습니다! :)

 