var colorArr = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
var p = document.getElementById("test");

p.onmouseover = function(){
    var rand = Math.floor(Math.random() * colorArr.length);
    p.style.backgroundColor = colorArr[rand];
};

p.onmouseout = function(){
    p.style.backgroundColor = "black";
}

document.getElementById("btn1").addEventListener("click", function(){
    alert("실행문1");
}, false);

document.getElementById("btn1").addEventListener("click", function(){
    alert("실행문2");
}, false);

    