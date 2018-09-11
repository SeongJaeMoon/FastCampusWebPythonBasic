# HTML
키워드 : [HTML](https://ko.wikipedia.org/wiki/HTML), [태그언어](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EC%97%85_%EC%96%B8%EC%96%B4), [HTML5](https://ko.wikipedia.org/wiki/HTML5), [DOCTYPE](https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%84%9C_%ED%98%95%EC%8B%9D_%EC%84%A0%EC%96%B8), [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

드디어 우리는 모든 웹 페이지의 근간이 되는 언어인 HTML에 대해서 공부를 시작했습니다! 이번 장에선, 웹의 기본 구조를 작성하는 이 HTML이라는 것에 대한 내용을 간단하게 살펴보도록 하겠습니다 :)

HTML은 HyperText Markup Language의 약자로 우리가 웹 페이지 상에 어떤 내용 혹은 정보(콘텐츠)를 표현하기 위한 구조를 작성하는 언어입니다. 

이러한 HTML은 정해진 표식(태그)에 따라 다른 모양으로 내용을 표현할 수 있습니다. 이 표식은 이미 정해진 각각의 역할에 맞게 작성하게 됩니다. 

이 내용은 아래 코드를 통해서 확인할 수 있습니다. <태그>내용</태그> 형태로 HTML 코드를 작성하게 되고, 슬래시(/) 표시가 없는 앞에 태그를 "여는 태그", 슬래시(/) 표시가 있는 뒤에 태그를 "닫는 태그"라고 부르게 됩니다.

```html
<!-- <표식>내용<표삭> --> 
<tag>contents</tag>
```

위의 코드 중에 한 가지 의문점이 드는 내용이 있으실 텐데요. 그건 아마도 표식이라고 쓰인 부분을 둘러싼 무언가 일 것입니다. 우리는 망각의 동물? 이므로 기억보다는 기록에 의존해야 하는 경우가 많습니다. 이 주석은 프로그램 코드를 작성할 때 해당 코드가 의미하는 바를 기록하는 것이라고 할 수 있습니다. 

위의 코드에서 처럼 `"<!--"` 로 시작하는 부분부터 `"-->"`로 끝나는 부분 안에 기록하고 싶은 내용을 작성해주면, 해당 내용은 브라우저가 자동적으로 HTML 코드에서 제외하고, 웹 페이지를 만들어주게 됩니다. 

주석은 코드를 작성할 때 중요한 내용들을 기록하는 부분이므로 굉장히 중요합니다. 저는 원활한 강의 진행을 위해 강의 안에선 주석을 잘 사용하지 않지만, 프로그램 코드를 작성할 때 이 주석을 작성하는 것은 굉장히 굉장히 중요합니다! 코드를 작성하다가 중요하다고 생각되는 부분이 있거나 기록으로 무언가 남겨야 할 경우가 생긴다면 꼭 주석을 작성하는 습관을 들이시면 좋겠습니다 :)

**VS Code 주석 단축키**
> 윈도우 : Ctrl + /

> 맥 : Cmd + /

다시 돌아와서 우리는 이렇게 "<태그>내용</태그>" 형태를 **요소(Element)** 라고 부를 것입니다. 

그렇다면, 이 엘리먼트를 어떻게 작성해야 할까요? 표식(태그)엔 어떤 내용을 작성해야 할까요? 그 부분을 우리가 앞으로 함께 HTML을 공부하며 알아가 볼 것입니다! 

다음으로 이야가 할 내용은, 우리가 공부하는 HTML 코드는 "HTML5"라는 겁니다. 스마트폰을 예로 들자면, 매년 새로운 버전의 스마트폰이 출시가 되고 새로운 스마트폰은 기존의 스마트폰과 같은 기능을 갖는 부분도 있지만, 여러 가지 부분이 새롭게 업데이트되는 것을 확인할 수 있습니다. 마찬가지로, 이 HTML이라는 마크업 언어 또한 여러 가지 버전이 존재하고 각 버전마다 용도와 내용에 약간씩 차이가 나타나게 됩니다. 

그렇다면, 왜 "doctype html"을 HTML 코드 가장 상단부에 작성하는 것일까요? 그건 바로 "웹 표준"이라는 것 때문인데요. 우리가 작성하는 HTML 코드는 브라우저가 해당 HTML 코드를 해석하는 작업을 진행하게 됩니다. 그런데 이 브라우저의 종류는 생각보다 무수히 많은 종류가 존재합니다. 때문에 모든 브라우저에게 "우리가 작성하는 것은 HTML5 코드야!"라고 알려줌으로써 모든 브라우저에서 우리가 원하는 형태로 표식(태그)이 나타날 수 있도록 하는 것입니다.

그리고 이걸 HTML 코드로 나타내는 선언문이 아래 보이는 "doctype html 코드"입니다.

```html
<!doctype html>
```

우리는 이렇게 HTML 코드를 작성하고, 실제로 코드를 실행하기 위해서 VS Code의 마켓 플레이스에서 확장 프로그램을 다운로드하고 사용했습니다. 윈도를 기준으로 간단하게 Live Server 확장팩을 VS Code에서 설치하는 방법에 대해서 알아보겠습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/liveserver1.JPG" width="100%" height="70%">
</p>

마켓플레이스에서 "Live Server"를 입력하여 확장 프로그램을 검색합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/liveserver2.JPG" width="100%" height="70%">
</p>

설치를 진행하고 "다시 로드"를 클릭합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/liveserver3.JPG" width="100%" height="70%">
</p>
확장 프로그램의 "설치됨" 부분에 Live Server가 나타나면 정상적으로 설치가 완료된 것입니다! 

이 라이브 서버를 VS Code에서 실행하기 위한 방법은 두 가지가 있습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/run1.png" width="70%" height="70%">
</p>

첫 번째 방법은 index.html 파일을 열고 마우스 버튼 우클릭을 해주면 "Open with Live Server"가 나타납니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/run2.png" width="70%" height="70%">
</p>

두 번째 방법은 명령 팔레트를 통해 실행하는 방법입니다. 명령 팔레트를 실행하고 Live Server라고 입력하면 "Open with Live Server"가 나타납니다.

**명령 팔레트 단축키**

> 윈도우 : Ctrl + Shift + P

> 맥 : Cmd + Opt + p

두 가지 방법 모두 변경 사항을 저장하면 자동으로 크롬에 변경 사항이 적용되므로 변경 사항이 생기면 저장만 해주시면 됩니다 :) 만약, 적용이 되지 않는다면 페이지 새로 고침을 해주세요!

## Live Server 기본 브라우저 선택

VS Code의 Live Server 확장을 통해 우리가 작성한 프로그램 코드를 실행할 때 기본 실행 브라우저가 크롬이 아닌, Internet Explorer로 실행되는 경우가 있을 수 있습니다. (특히, 윈도 환경) 이럴 경우 Live Server로 실행할 브라우저를 따로 설정해주어야 합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/setting1.png" width="100%" height="70%">
</p>

우선 위에서 살펴본 명령 팔레트를 실행하고, `setting`이라고 입력합니다. `Preferences: Open User Settings`이라고 나오는 부분을 클릭하여 실행합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/setting2.png" width="100%" height="70%">
</p>

정상적으로 실행되면 위 처럼 여러가지 설정 정보가 나오게 됩니다. 검색창에 `liveServer.settings`이라고 입력해줍니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/setting4.png" width="60%" height="50%">
</p>

여러 설정 중에서 `"liveServer.settings.CustomBrowser: null",`이라고 작성된 부분을 찾습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/HTML/Course01/static/setting5.png" width="60%" height="60%">
</p>

왼쪽의 펜 모양 아이콘을 클릭하면 브라우저를 선택할 수 있는 창이 나타납니다. `chrome` 브라우저를 선택하고 변경 사항을 저장합니다. 

VS Code는 Live Server 뿐만 아니라, 우리가 코드를 작성할 때 꼭 필요하거나 선택 사항이지만 꽤나 유용한 확장 프로그램이 많이 존재합니다. VS Code를 사용하면서 꼭 제가 말씀드리는 것뿐만 아니라, 다른 여러 가지 확장 프로그램을 검색해서 찾아보고 본인이 사용하고 싶은 확장 프로그램을 설치하고 사용해도 괜찮습니다 :) 

HTML에 대해서 조금 감이 오시나요? 우리가 프로그래밍 언어를 공부할 때 용어, 그리고 개념들이 굉장히 많이 등장하는데요. 이러한 용어의 기원과 개념들에 대해 하나하나 알아가는 과정에서 점점 프로그래밍과 가까워지실 수 있을 거라고 믿습니다 :)