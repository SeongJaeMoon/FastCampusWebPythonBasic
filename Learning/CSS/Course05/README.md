# 부트스트랩
키워드 : [부트스트랩 4](https://www.w3schools.com/bootstrap4/default.asp)

부트스트랩은 웹 개발을 위해 사용되는 많은 프레임워크 중 특히 많은 사랑을 받는 굉장히 유용한 프레임워크라고 할 수 있습니다. 강의에서 기존의 테이블 태그와 ul 태그의 모양을 자유자재로 변경하는 모습을 감상하셨을 거라고 생각합니다. 이 부트스트랩만 잘 활용해도 굉장히 많은 디자인 처리와 모바일 환경 대응도 가능합니다.

우리는 "Bootstrap 4"를 사용하였습니다. 이 부트스트랩을 사용하기 위해 [여기](https://www.w3schools.com/bootstrap4/bootstrap_get_started.asp)에서 "MaxCDN" 부분의 내용을 head 태그에 작성합니다. (작성할 때 한 가지 주의할 점은 코드 작성 순서가 바뀌면 적용이 안 될 수 있다는 점입니다!)

```html
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Popper JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
```
부트스트랩이 제공하는 디자인 요소는 굉장히 다양합니다. 마찬가지로, [여기](https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp)에 접속해서 각각의 요소에 어떤 클래스 속성 값이 있는지 확인하고 내가 원하는 디자인의 속성을 적용하면 됩니다.

외부 CSS 스타일과 부트스트랩을 적절히 혼용하면 아주 멋진 디자인의 웹 페이지를 구성할 수 있으실 겁니다! 아래 내용은 부트스트랩을 사용할 때 참고하면 좋을 내용들입니다.

## 레이아웃
### 컨테이너(Container)
컨테이너는 부트스트랩에서 가장 기본적인 레이아웃 요소이며 기본 그리드 시스템을 사용하려면 필요합니다. 반응형, 고정폭 컨테이너(각 중단점에서 최대 넓이 변경), 유동 폭 컨테이너(항상 ‘100% 넓이’) 중에서 선택할 수 있습니다. 중단점의 내용은 아래에서 추가로 알아보도록 하겠습니다. 컨테이너를 정의하는 방법은 간단합니다. 전체 콘텐츠를 감싸는 부모 역할을 하는 `<div>`요소에 클래스 속성 값을 `container`로 주면 됩니다.

```html
<!-- 중략 -->
<body>
    <div class="container">
    <!-- 콘텐츠는 여기에 -->
    </div>
</body>
<!-- 중략 -->
```

컨테이너를 지정하면, 자동으로 width 값이 결정되고, `margin`이 설정됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course05/static/naver.JPG" width="100%" height="70%">
</p>

예를 들어, 우리가 잘 아는 포털 사이트인 네이버 사이트의 경우 빨간색 테두리로 표시된 빈 영역을 가지고 있으며, 콘텐츠는 고정폭 안에 정렬되어 있는 것을 확인할 수 있습니다. 다음으로 말씀드릴 내용은, 중단점(breakpoints)과 관련된 내용에 대해서 알아보겠습니다. 

부트스트랩은 기본적으로 모바일 환경을 우선적으로 지원하도록 설계된 프레임워크입니다. 일반적으로, 대부분의 웹 사이트는 디바이스 화면의 크기에 따라 다른 스타일로 콘텐츠를 제공하게 되는데요, 이러한 경우 CSS 코드의 스타일이 동적으로 변경될 수 있도록 [미디어 쿼리](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries)라는 것을 사용하게 됩니다. 미디어 쿼리 를 이용해 디바이스 크기별 다른 스타일을 적용하는 지점을 중단점이라고 표현할 수 있습니다.

```css
//small devices (portrait phones, 576px 미만)
//부트스트랩의 기본값이므로 미디어 쿼리가 없습니다.

// Small devices (landscape phones, 576px 이상)
@media (min-width: 576px) { ... }

// Medium devices (tablets, 768px 이상)
@media (min-width: 768px) { ... }

// Large devices (desktops, 992px 이상)
@media (min-width: 992px) { ... }

// Extra large devices (large desktops, 1200px 이상)
@media (min-width: 1200px) { ... }
```
위 코드에 표현된 것처럼, 부트스트랩은 각 디바이스 별 최솟값을 기준으로 중단점을 나누게 됩니다. `{...}` 부분에 디바이스 크기 별로 동작하게 하고 싶은 CSS 코드를 작성하면 됩니다. 

### 그리드(Grid)
일반적으로 부트스트랩을 사용할 때 많이 사용되는 레이아웃 구성 요소는 그리드 시스템(Grid-system)입니다. 이름에서 느껴지듯이, 격자 모양으로 영역을 구분 짓고 각 영역에 맞게 세분화하여 콘텐츠를 담는 형태로 작성할 수 있습니다. 12개의 열(Column)을 갖는 것을 기본으로 합니다. 

```html
<!-- 중략 -->
<div class="container">
  <div class="row">
    <div class="col-sm">
      세 칼럼 중 하나
    </div>
    <div class="col-sm">
      세 칼럼 중 하나
    </div>
    <div class="col-sm">
      세 칼럼 중 하나
    </div>
  </div>
</div>
<!-- 중략 -->
```
부트스트랩의 그리드 시스템은 일련의 컨테이너, 행 및 열을 사용하여 내용을 정렬하고 구성합니다. 위의 예시는 사전에 정의된 그리드 클래스를 사용하여 small, medium, large 및 extra large 디바이스를 고려하여 세 개의 동일폭(equal-width) 칼럼으로 작성되었습니다. 이 칼럼들은 부모에 `.container`가 적용된 페이지의 가운데에 배치됩니다.

```html
<!-- 중략 -->
<div class="container">
  <div class="row">
    <div class="col-4">
      세 칼럼 중 하나
    </div>
    <div class="col-4">
      세 칼럼 중 하나
    </div>
    <div class="col-4">
      세 칼럼 중 하나
    </div>
  </div>
</div>
<!-- 중략 -->
```

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course05/static/col.JPG" width="70%" height="50%">
</p>

위의 예시는 동일한 폭의 칼럼 크기를 구분하기 위해서 사용되는 방법입니다. 칼럼 클래스는 행(row) 당 12개의 가능한 칼럼 중에서 사용하려는 칼럼의 수(number)를 나타냅니다. 따라서 동일한 폭의 3개의 칼럼이 필요하다면 `.col-4`를 사용할 수 있습니다. 단, 하나의 `.row` 안에 `.col-x`를 나열할 경우, 각각의 열의 합이 `12`가 되도록 적용합니다.

## 컴포넌트(Component)
### 알림(Alert)
알림은 사용자와 상호작용을 하기 위해서 자주 사용되는 컴포넌트 중 하나입니다. 사용자의 행동(글 입력, 버튼 클릭, etc.)에 따른 반환 결과를 원활하게 제공하기 위해서 사용합니다.
```html
<div class="alert alert-danger alert-dismissible" role="alert">
  <strong>실패!</strong> 글을 삭제하는데 실패했습니다. 잠시 후 다시 시도해주세요.
  <a type="button" class="close" data-dismiss="alert" aria-label="닫기">
    <span aria-hidden="true">&times;</span>
  </a>
</div>
```
위와 같이 코드를 작성하면, 아래와 같이 결과가 나타나게 됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course05/static/alert.JPG" width="70%" height="50%">
</p>

기본적으로 `.alert` 클래스 속성이 기본으로 사용되며, `.alert-danger`, `.alert-primary`, `.alert-info`, `.alert-warning`, `.alert-success` 등과 같이 클래스의 이름에 따라 상태에 맞는 적절한 색이 지정되게 됩니다. 알림을 닫을 수 있도록 하기 위해서 버튼을 정의하고, 클래스 속성을 `.close`로 작성합니다. (`&times;`는 브라우저에서 `X` 모양을 나타냅니다.)

### 버튼(Button)
부트스트랩은 다양한 모양, 색을 지원하는 버튼을 사용할 수 있습니다. 또한, `<button>` 태그 뿐만 아니라, `<a>` 태그와 `<input>` 태그에도 사용할 수 있습니다. 기본적으로 `.btn` 클래스 속성을 사용하여 버튼 모양으로 구성할 수 있습니다.
```html
<a class="btn btn-primary" href="#" role="button">링크</a>
<button class="btn btn-primary" type="submit">제출</button>
<input class="btn btn-primary" type="button" value="입력">
```
위와 같이 코드를 작성하면, 아래와 같이 결과가 나타나게 됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course05/static/button.JPG" width="50%" height="40%">
</p>

`alert`와 마찬가지로 `btn-primary`, `btn-danger`, `btn-info`, `btn-success`, `btn-link`, `btn-secondary`, `btn-warning`, `btn-light`, `btn-dark`  등과 같이 의미에 따라 버튼의 색을 변경할 수 있습니다.

### 카드(Card)
앞서, `.container` 클래스 속성을 통해 전체 콘텐츠를 감싸는 요소를 정의할 수 있다고 알아보았습니다. 마찬가지로, 개별 콘텐츠를 담을 컨테이너 영역을 설정하기 위해서 `.panel`과 `.card`를 사용할 수 있습니다. 여기선 카드 클래스 속성에 대해서 알아보도록 하겠습니다.
```html
<div class="card text-center bg-info" style="width: 300px;">
    <img class="card-img-top" src="cat.jpeg">
    <div class="card-body">
        <h4 class="card-title">고양이</h4>
      <p class="card-text">껌껌이는 아주 아주 귀여운 고양이입니다.</p>
      <a href="#" class="btn btn-primary">클릭</a>
    </div>
</div>
```
위와 같이 코드를 작성하면, 아래와 같이 결과가 나타나게 됩니다.

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course05/static/card.JPG" width="70%" height="50%">
</p>

`.card` 클래스 속성을 통해 카드 모양의 영역을 표현합니다. 또한, `.text-center` 클래스 속성을 적용하면, 카드 내의 콘텐츠를 가운데 정렬할 수 있습니다. 여기서 사용된 `.bg-info`의 경우 `btn`, `alert`와 마찬가지로 이름에 따라 배경색이 변경되게 됩니다. 카드는 크게 `card-header`, `card-body`, `card-title`, `card-text`로 나뉘게 됩니다. 필요에 따라 각각의 영역에 사용되는 콘텐츠를 구분 지어 사용하면 됩니다.

### 캐러셀(Carousel)
이번 절에서 살펴볼 캐러셀은 부트스트랩에서 특히 자주 사용되는 요소 중에 하나입니다. 경우에 따라서 다양한 응용이 가능하므로, 캐러셀 코드를 많이 작성해보는 것을 추천드리고 싶습니다. :) 캐러셀을 한 마디로 쉽게 표현하면, "슬라이드 쇼"라고 할 수 있습니다. 
```html
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <!-- 슬라이드 인디케이터 표시 영역 -->
        <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        </ol>
        <!-- 실제 캐러셀 콘텐츠 영역 -->
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img class="d-block w-100" src="cat.jpeg" alt="첫번째 슬라이드">
                <div class="carousel-caption d-none d-md-block">
                    <h3>고양이1</h3>
                    <p>첫 번째 콘텐츠</p>
                </div>
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="cat.jpeg" alt="두번째 슬라이드">
                <div class="carousel-caption d-none d-md-block">
                    <h3>고양이3</h3>
                    <p>두 번째 콘텐츠</p>
                </div>
            </div>
              <div class="carousel-item">
                <img class="d-block w-100" src="cat.jpeg" alt="세번째 슬라이드">
                <div class="carousel-caption d-none d-md-block">
                    <h3>고양이3</h3>
                    <p>세 번째 콘텐츠</p>
                </div>
              </div>
            </div>
            <!-- 이전/다음 컨트롤 영역 -->
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">이전</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">다음</span>
            </a>
    </div>
```
위와 같이 코드를 작성하면, 아래와 같이 결과가 나타나게 됩니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course05/static/cs.JPG" width="70%" height="70%">
</p>


캐러셀은 자동으로 슬라이드 크기를 표준화하지는 않습니다. 따라서 콘텐츠의 크기를 적절하게 조정하려면 사용자 정의 스타일을 사용해야 합니다. 캐러셀은 이전/다음을 나타내는 컨트롤 및 인디케이터를 지원하지만 꼭 요구되지는 않습니다. 필요에 따라 원하는 대로 추가하고 사용자 정의 코드를 작성하면 됩니다. 코드가 생각보다 길어 보일 수 있습니다. 하지만, 위와 같은 효과를 우리가 직접 만들기 위해서 코드를 작성하면 훨씬 많은 양의 코드를 작성해야 되기 때문에 유용하게 사용될 수 있겠죠? :)

### 네비게이션(Navigation)
네비게이션은 강의에서도 살펴봤던 요소 중에 하나입니다. 네비게이션을 통해 사용자에게 페이지의 이동 혹은, 새로운 콘텐츠 보여주기 등의 기능을 제공할 수 있습니다.
```html
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">활성탭</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">탭2</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">탭3</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">선택 불가</a>
  </li>
</ul>
```
위와 같이 코드를 작성하면, 아래와 같이 결과가 나타나게 됩니다. 

<p align="center">
    <img src="https://github.com/SeongJaeMoon/FastCampusWebPythonBasic/blob/master/Learning/CSS/Course05/static/nv.JPG" width="70%" height="70%">
</p>

네비게이션 뿐만 아니라, 네비게이션 바(Navigation bar)라고 부르는 상단 영역에 고정되어 있는 탭 또한 사용할 수 있습니다. 네비게이션 사용에 익숙해지셨다면, [네비게이션 바](https://www.w3schools.com/bootstrap4/bootstrap_navbar.asp)의 사용도 꼭 해보시길 바라겠습니다.

부트스트랩에는 위에서 알아본 속성뿐만 아니라, 더 다양한 스타일 요소들이 존재합니다. 사실, 모든 디자인 기능을 부트스트랩 만으로 해결하긴 어렵습니다. (사용자 정의 스타일 코드가 필수 불가피합니다.) 하지만 대부분의 큰 틀의 디자인 요소는 부트스트랩을 통해 해결 가능하고, 디테일한 부분의 디자인 요소를 고민하는 시간을 더 많이 가질 수 있습니다. 부트스트랩의 클래스 속성을 바꿔가며 스타일이 어떻게 변해가는지 확인해보시길 바라겠습니다. :)