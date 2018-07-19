# 클라이언트와 서버
키워드 : [인터넷](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%EB%84%B7), [웹](https://ko.wikipedia.org/wiki/%EC%9B%94%EB%93%9C_%EC%99%80%EC%9D%B4%EB%93%9C_%EC%9B%B9), [Client](https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8_%EC%84%9C%EB%B2%84_%EB%AA%A8%EB%8D%B8), [Server](https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8_%EC%84%9C%EB%B2%84_%EB%AA%A8%EB%8D%B8), [HTTP](https://tools.ietf.org/html/rfc2616)

우리는 인터넷이라는 컴퓨터 네트워크 공간에서 웹 기술을 통해 서로 자원과 정보를 공유하고 있습니다. 그 과정은 자원과 정보를 제공해주는 측(서버)과 제공된 자원과 정보를 보는 사용자 측(클라이언트)과 같은 각자만의 고유한 역할을 갖게 됩니다.

또한, 이러한 역할극이 이루어지는 공간은 브라우저라는 프로그램이 하나의 공간이라고 할 수 있습니다. 

그렇다면, 이러한 역할극에 대해서 간단히 살펴보도록 하겠습니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Orientation/Course02/static/ClientServer1.png" width="100%" height="70%">
</p>

정보를 제공하는 역할을 맡은 **서버** 측은 브라우저를 통해 사용자의 요청에 맡는 정보를 제공합니다. 사용자 역할을 맡은 **클라이언트** 측은 이러한 정보를 서버가 제공하는 방식에 따라서 보게 됩니다.

> 클라이언트 : 요청(Request)하는 역할

> 서버 : 응답(Response)하는 역할

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/Orientation/Course02/static/ClientServer2.png" width="100%" height="70%">
</p>

이러한 역할극을 하는 데는 이유가 존재하는데요. 사용자는 자신이 원하는 자원과 정보를 보기 원하는 기대가 들어있고, 서버는 그러한 사용자에 요청에 맞는 웹 페이지를 보여주는 일종의 사명?을 갖는다고 할 수 있습니다.

이렇게 인터넷 공간에서 누군가와 어떤 정보를 주고받는 과정에는 굉장히 여러 가지 기술들이 사용되며, 많은 과정을 거치게 됩니다. 

그 많은 과정 중에서 우리가 직접적으로 웹 자원을 주고받는 과정을 담당하는 영역이 존재합니다. 일반적으로 응용계층(네트워크 연결 과정)이라고 불리는 과정입니다. 이 과정에서 필요한 많은 규칙들이 존재합니다. **이 규칙을 우리는 HTTP라고 부릅니다.** 

사실, HTTP는 이렇게 쉽게 이야기할 수 있는 개념은 아닙니다. 이 규칙 안에는 수많은 개념들과 기술들이 들어가 있는데요. 우리는 이 규칙이 웹 상에서 사용자(클라이언트)가 누군가(서버)와 정보를 주고받기 위한 규칙이라고 이해해주시면 됩니다. 

조금 더 상세한 내용은 HTML 강의 부분에서 GET과 POST 방식에 대해 이야기하며 더 살펴보도록 하겠습니다 :)


