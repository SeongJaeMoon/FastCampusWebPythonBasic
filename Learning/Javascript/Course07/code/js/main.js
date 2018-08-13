var arr = [1, 2, 3, 4, 5];
var len = arr.length;
// for(var idx = 0; idx < len; ++idx){
//     console.log(arr[idx]);
// }
var idx = 0;
// while(idx < len){
//     console.log(arr[idx]);
//     ++idx;
// }

while(idx < len){
    if(idx == 2){
        break;
    }
    console.log(arr[idx]);
    ++idx;
}

for(var i = 0; i < 5; ++i){
    if(i % 2 == 0){
        continue;
    }
    console.log(i); //1, 3
}
//1, 3 (홀수만) 출력 후 아래 코드를 실행
console.log("for문 반복 중지!"); //for문 반복 중지!