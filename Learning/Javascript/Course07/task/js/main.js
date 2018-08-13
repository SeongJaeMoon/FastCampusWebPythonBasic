// 문자열 결합 반복 처리하기
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var result = "";
var len = arr.length;
for(var i = 0; i < len; ++i){
    for (var j = 1; j <= 9; ++j) {
        result += arr[i] + " x " + j + " = " + (arr[i] * j) + "<br>";
    }
}
document.write(result);
