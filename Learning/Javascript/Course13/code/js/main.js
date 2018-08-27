var idx = 0;
function changeText(){
    var textArr = ["html", "css", "js", "python"];
    document.getElementById("test").innerHTML = textArr[idx++];
    if(idx == textArr.length){
        idx = 0;
    }
}

document.getElementById("btn").onclick = function(){
    changeText();
}