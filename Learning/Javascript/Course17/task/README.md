# Firebase 배포하기
키워드 : [Firebase](https://firebase.google.com/), [Firebase CLI](https://www.npmjs.com/package/firebase-tools?activeTab=readme), [Firebase 호스팅](https://firebase.google.com/docs/hosting/quickstart?hl=ko)

직접 제작한 웹 페이지를 Firebase 호스팅 서비스를 이용해서 실제 배포하고, 코드 변경 사항 적용을 위한 재배포를 위한 참고 자료를 정리하도록 하겠습니다. 차근차근 따라 해 주세요! :) 

강의에서 말씀드렸듯이, [Node.js 공식 홈페이지](https://nodejs.org/ko/)에서 Node.js를 먼저 다운로드하고 진행해주세요. 아래 예시는 Windows 운영체제를 예로 들었지만, Mac OS에서도 같은 방법으로 진행해주시면 됩니다. 

윈도 7을 사용하시는 분은 탐색기를 실행하고(Ctrl + ESC), 명령 프롬프트를 입력합니다. 명령 프롬프트가 나타나면 관리자 권한으로 실행합니다. 

윈도 10을 사용하시는 분도 마찬가지로 탐색기를 실행하고(window + x) 관리자 권한으로 명령 프롬프트를 실행합니다. (윈도 10을 사용하시는 분은 Powershell로 진행됩니다.) 

맥 운영체제를 사용하시는 분은 터미널을 열고 실행하면 됩니다.(Permmission 에러 방지를 위해 명령어 앞에 sudo를 붙여줍니다.)

## 1. Firebase-tools 준비

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb0.JPG" title="준비" width="100%" height="70%">
</p>

터미널을 실행하고, Firebase CLI(Command Line Interface)를 사용하기 위해 아래 명령어를 입력합니다. 

> npm install -g firebase-tools

## 2. Firebase 로그인

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb1.JPG" title="로그인" width="100%" height="70%">
</p>

Firebase CLI를 사용하기 위해 터미널에 아래 명령어를 입력합니다. 

> firebase login

## 3. Firebase 로그인 계속

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb2.JPG" title="로그인" width="30%" height="100%">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb3.JPG" title="로그인" width="30%" height="100%">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb4.JPG" title="로그인" width="30%" height="50%">
</p>

처음 터미널로 로그인을 시도하면, 웹 브라우저로 로그인을 진행해야 합니다. **Firebase 프로젝트를 만들 때 사용했던** 아이디로 로그인을 진행합니다.

## 4. Firebase init
<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb6.JPG" title="프로젝트 생성" width="100%" height="70%">
</p>

로그인까지 정상적으로 이루어졌다면, 본격적으로 Firebase 호스팅 서비스를 이용해 배포할 전용 프로젝트 폴더를 구성해야 합니다. 

원하는 위치에 원하는 이름으로 폴더를 하나 생성해주세요. 단, 윈도우 운영체제를 사용하시는 분들은 바탕화면보다는 C드라이브 혹은, D드라이브 등에 구성하는 걸 추천드립니다. 

저의 경우 D드라이브에 `firebase`라는 이름의 폴더를 만들었습니다. firebase 프로젝트를 시작하기 위해서 터미널에 `cd 경로` 형태로 작성하여 해당 폴더로 경로 이동(Change directory) 합니다. 경로는 윈도우 탐색기에서 복사해서 붙여 넣기 해주시면 됩니다. 맥 운영체제의 경우엔 파인더의 경로 복사 기능을 이용하면 됩니다.

> cd D:₩firebase 

프로젝트 폴더로 이동한 후, 아래 명령어를 입력합니다. `Are you ready to proceed?`라는 문구가 나오면 `Y`를 입력하고 엔터(Enter)를 쳐줍니다. 

> firebase init

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb7.JPG" title="프로젝트 생성" width="100%" height="70%">
</p>

앞 단계까지 정상적으로 진행되면, 위 사진처럼 원하는 Firebase 플랫폼 서비스를 선택하는 창이 나오게 됩니다. 우리는 hosting 서비스를 이용할 것이기 때문에 방향키를 이용해 hosting을 선택하고 스페이스바(Space bar)를 클릭하면 선택됩니다. 선택이 된 상태에서 엔터를 쳐줍니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb8.JPG" title="프로젝트 생성" width="100%" height="70%">
</p>

잠시 기다리면 `Select default Firebase project for this directory:`라는 문구가 나오며 [Firebase 콘솔](https://console.firebase.google.com/)에서 만든 프로젝트가 터미널에 표시됩니다. 저의 경우 `fastcampus`라는 이름의 프로젝트를 만들어뒀기 때문에 `fastcampus` 프로젝트를 선택했습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb9.JPG" title="프로젝트 생성" width="100%" height="70%">
</p>

또 잠시 기다리면, 위와 같은 화면이 나오게됩니다. 우리는 새롭게 프로젝트를 실행하는 것이기 때문에 기본 설정을 그대로 사용합니다. `what do you want to use ase your public directory` 문구가 나오면 그냥 엔터를 쳐줍니다. `Configure as single-page app (rewirte all urls to /index.html)`라는 문구가 나오면 `y`를 입력하고 엔터를 쳐줍니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb11.JPG" title="프로젝트 생성" width="100%" height="70%">
</p>

잠시 기다리면 위와 같이 `Firebase initialization complete!`라는 문구가 나오며 프로젝트 생성이 완료됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb12.JPG" title="프로젝트 배포" width="100%" height="70%">
</p>

프로젝트 폴더를 확인해보면, `public`이라는 폴더와 `.firebaserc`, `firebase.json` 파일이 자동으로 생성된 것을 확인할 수 있습니다. 우리는 기본 설정을 그대로 사용하면 되기 때문에, 따로 설정을 변경할 필요가 없습니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb10.JPG" title="프로젝트 생성" width="100%" height="70%">
</p>

생성된 `public` 폴더에 들어가서 index.html 파일을 확인해보면 위 사진과 같이 기본으로 들어가 있는 코드가 있습니다. 기존에 작성해둔 html 코드를 이 파일에 덮어쓰기 해줍니다. 마찬가지로, 미리 구성해둔 폴더 구조가 있으시다면, 구조 그대로 js, css, static, etc. 폴더 등도 `public` 폴더에 함께 저장해줍니다.

## 5. Firebase deploy

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb13.JPG" title="프로젝트 생성" width="100%" height="70%">
</p>

이제 마지막으로 웹 페이지를 실제 배포만 하면됩니다. 배포를 위해 아래 명령어를 입력합니다. 잠시 기다리면, 위 화면과 같이 Deploy complete!라는 문구와 함께 `Hosting URL`이 나타난 것을 확인할 수 있습니다.

> firebase deploy

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course17/static/fb14.JPG" title="프로젝트 배포" width="100%" height="70%">
</p>

정상적으로 배포가 되었는지 확인하기 위해 [Firebase 콘솔](https://console.firebase.google.com/)에 접속합니다. 프로젝트에 접속하고, `hosting` 탭을 클릭합니다. 도메인 부분 밑에 있는 주소를 클릭하면 배포된 웹 페이지를 확인할 수 있습니다. 

이제 고유한 도메인 URL을 갖는 웹 페이지가 생겼습니다! 필요한 경우에 이 URL만 있으면 직접 제작한 웹 페이지에 누구나 접속하도록 할 수 있습니다! 

처음부터 완벽한 웹 페이지를 만들고 배포하긴 어려움이 많습니다. 코드 변경 사항이 생길 경우에 터미널을 열고 프로젝트 폴더에 접속합니다. (e.g., cd D:₩firebase) 접속이 정상적으로 이루어지면, `firebase deploy` 명령어만 입력해주면 변경 사항이 자동으로 재배포되어 적용되게 됩니다! :)