function getDate(){
    var result = "";
    var year = new Date().getFullYear();
    var month = new Date().getMonth() + 1; //getMonth 메서드는 (0부터 1월을 나타냅니다.)
    var day = new Date().getDate();
    result = year + "-" + month + "-" + day;
    document.getElementById("test").innerHTML = result;
}