var time = 0; //타이머를 나타낼 변수 선언
var isTime = false; //타이머가 시작됐는지 체크할 변수 선언
var timer = null; //타이머 객체를 담을 변수 선언
var button = document.getElementById("starttimer"); //타이머(버튼)을 가리킬 변수 선언

//타이머 함수 선언
function myTimer(){
    document.getElementById("test").innerHTML = time++;
}

//타이머 실행
document.getElementById("starttimer").addEventListener("click", function(e){
    //타이머가 실행 중이 아닐 경우 실행할 코드
    if(!isTime){
        isTime = true;
        //타이머 시작
        timer = window.setInterval(myTimer, 1000);
        button.innerHTML = "타이머 중지";
    //타이머가 실행 중일 경우 실행할 코드
    }else{
        isTime = false;
        //타이머 초기화
        clearInterval(timer);
        button.innerHTML = "타이머 시작";
    }
}, false)


