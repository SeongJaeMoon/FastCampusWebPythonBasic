var test = document.getElementById("test");
// window.open("https://www.google.com");
// window.close();
// var trueOrFalse = window.confirm("true of false");
// test.innerHTML = trueOrFalse;
// test.innerHTML = "width: " + window.innerWidth + " height: " + window.outerHeight;
// window.alert("알림창입니다.");
var x = 0;
window.setInterval("interval()", 1000);
function interval(){
    test.innerHTML = ++x;
}