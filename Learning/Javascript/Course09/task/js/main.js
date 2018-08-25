var now = new Date(); //오늘 날짜
var count = new Date("2018-12-31"); //D-day 날짜
var gap = now.getTime() - count.getTime(); //오늘 날짜와 D-day 날짜의 차를 밀리초로 계산
//두 날짜 사이의 차를 하루를 기준으로 나눈 값을 소숫점 이하를 버림 연산
gap = Math.floor(gap / (24 * 60 * 60 * 1000)); 

var result = ""; //결과를 반환할 변수

//D-day 계산
if (gap > 0) {
    result = "+" + gap;
} else if (gap == 0) {
    result = "day";
} else {
    result = gap;
}
//계산 결과 출력
document.write("D-day를 기준으로 D" + result + "입니다.");