# Javascript 변수
키워드 : [자바스크립트 변수](https://www.w3schools.com/js/js_variables.asp)

우리가 어떤 프로그램을 실행하고 해당 프로그램이 동작하기 위해선 메모리라는 공간에 해당 프로그램이 자신만의 공간을 갖는 과정이 필요합니다. 이렇게 해당 프로그램이 메모리 공간에 자리를 잡을 때는, 해당 프로그램에서 사용하는 여러가지 자원들이 함께 자리를 잡게 되는데요.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course04/static/var1.png" width="100%" height="70%">
</p>

프로그램에서 선언하고 사용하는 변수라는 친구도 그 자원 중에 하나라고 할 수 있습니다. 변수는 우리가 프로그램에서 어떤 처리나 연산을 하기 위해서 사용하는 하나의 메모리 공간입니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course04/static/var2.png" width="100%" height="70%">
</p>

변수는 우리가 작명해준 이름을 갖고, 우리는 이 이름을 통해 이 변수에 어떤 값을 할당하거나, 수정 등을 할 수 있습니다. 단, 변수명은 의미 있는 이름으로 작성합니다. 또한, 일반적으로 "CamelCase"라는 낙타 등 모양의 형태로 작성합니다. 방법은 간단합니다. 우선, 변수의 의미는 사용자가 스크롤을 할 때 사용되는 변수라고 가정하겠습니다. 

var **userScroll** = "값"; 

변수의 시작은 소문자로 시작합니다. "user" 하나의 단어만으로 변수의 의미를 부여하는게 어려운 경우 또 다른 단어를 조합합니다. 단, 다음 단어의 첫 시작은 대문자로 시작합니다. "user" + "Scroll" (변수 선언 끝에 꼭 세미콜론(;)을 붙여 해당 코드의 끝을 알립니다.)

참고로 변수를 선언할 때 주의해야할 점이 몇 가지 있습니다.
1. 변수의 시작은 문자로 시작해야합니다.("$" 혹은 "_" 로 시작할 수도 있습니다.)
2. 대소문자를 구분합니다. (x와 X는 서로 다른 변수입니다.)
3. Javascript에서 이미 제공하는 키워드는 변수명으로 사용하지 않습니다.

이 방식은 나중에 공부할 함수라는 것에도 똑같이 적용되는 방법이니 잘 기억해주세요 :)

또한, 이 변수는 값에 따라서 여러가지 자료형(Type)을 갖습니다.

1. String(문자형)
2. Number(숫자형)
3. Boolean(논리형)
4. Undefined(값의 미정)
5. null

"console.log()"와 "typeof"를 이용해 개발자 도구에서 변수의 자료형을 확인할 수 있었습니다.
```Javascript
var x = 0, y = '10';
//number, string
console.log(typeof x, typeof y);
```

변수의 이름을 짓는 방법에는 여러가지 방법이 있습니다. 한 가지 예를 들면 참, 거짓(boolean)을 나타내는 변수명은 보통 "is"로 시작합니다. 변수명을 짓는 방법은 자유이지만, 변수가 갖는 의미를 어렵지 않게 알 수 있도록 이름을 작성하고, 주석을 통해 해당 변수의 역할을 기록하는 습관을 들이는 것도 프로그램 코드를 작성할 때 많은 도움이 될 수 있습니다 :)  