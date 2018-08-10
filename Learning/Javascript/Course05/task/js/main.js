// 문자열, 숫자 결합
/*
문자열(String)과 숫자(Number)를 덧셈 "+" 기호로 결합할 수 있습니다. 단, 피연산자 순서에 주의해야 합니다.
자바스크립트 언어는 문자열과 숫자를 결합할 경우 문자열 데이터 타입이 됩니다.
*/
var str1 = "귀요미" + 1;
console.log(typeof str1, str1); 
var str2 = 1 + "귀요미";
console.log(typeof str2, str2);
var str3 = 1 + 1 + "귀요미";
console.log(typeof str3, str3);
var str4 = "귀요미" + 1 + 1;
console.log(typeof str4, str4);