// datestring
var date = new Date("1970-01-01");
// 하루 24시간, 1시간 60분, 1분 60초, 1초 1000밀리초 
console.log(24 * 60 * 60 * 1000)
console.log(date.getTime());

var str1 = "Fastcampus";
var str2 = "Seongjae Moon";

console.log(str1.length);
console.log(str2.length);

// charAt(index)
console.log(str1.charAt(0));
console.log(str1.charAt(1));
// split(구분자)
console.log(str2.split(","));
// indexOf(찾을 문자)
console.log(str2.indexOf("p"));