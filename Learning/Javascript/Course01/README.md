# Firebase 시작하기
키워드 : [Firebase](https://firebase.google.com/), [구글 클라우드 옵션](https://cloud.google.com/storage-options/)

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course01/static/client_server.png" width="100%" height="70%">
</p>

우리가 작성한 코드는 브라우저를 통해 결과를 확인할 수는 있지만, 코드가 실행중인 PC를 제외한 다른 브라우저에서 함께 보기 위해선 같은 네트워크에 연결되어 있어야만 합니다. 그렇기 때문에, 전 세계 누구나 URL만 브라우저에 입력하면 웹 페이지를 볼 수 있도록 배포하는 작업이 필요합니다. 본인의 PC를 직접 서버로 사용해도 되지만, 그럴 경우 나의 컴퓨터가 웹 페이지 요청을 처리하기 위해서 계속해서 켜져 있어야 합니다. 전기세가 많이 나오겠죠..?

우리는 고유한 웹 페이지 도메인 주소를 제공하고, 클라이언트 요청에 웹 페이지를 대신 보내주는 Firebase 호스팅 서비스를 이용합니다. 

파이어베이스 호스팅 서비스를 이용하기 위해서 먼저, [Firebase 콘솔](https://console.firebase.google.com/)에 접속합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course01/static/firebase1.png" width="50%" height="50%">
</p>

콘솔에 접속한 후 프로젝트 시작하기를 클릭합니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course01/static/firebase0.png" width="50%" height="50%">
</p>

다음은, 새로운 프로젝트를 만들기 위한 정보를 입력합니다. 입력 내용 중 프로젝트 ID는 도메인 주소에 나타나는 이름이기도 합니다. 그렇기 때문에 의미 있는 프로젝트 ID로 작성해주세요!(e.g., aboutme)

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Javascript/Course01/static/firebase2.png" width="100%" height="70%">
</p>

프로젝트가 정상적으로 생성되면 위 사진처럼 해당 프로젝트의 고유한 대시보드(DashBoard)를 확인할 수 있습니다.

Firebase 호스팅 서비스를 이용해서 실제 웹 페이지를 배포하는 방법은 추후에 다루도록 하겠습니다. Firebase 플랫폼에서 제공하는 여러가지 기능들에 대해서도 함께 살펴보세요 :)
