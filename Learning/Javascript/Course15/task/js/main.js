//결과 리스트를 나타낼 변수 선언
var autocomplete = document.getElementById("autocomplete");
//input 태그의 값을 받아올 변수 선언
var search = document.getElementById("search");
//특정 키워드에 해당하는 입력 값에 대한 결과를 반환할 배열 선언
var wordList = ["Russian blue", "British Longhair", "Burmilla", "Bombay"];
//문자열 결합을 위한 변수 선언
var word = "";

search.addEventListener("keyup", function(e){ 
    //입력값
    var keyword = search.value;
    //입력 값이 "cat"인 경우
    if(keyword == "cat"){
        //문자열 결합
        for(var i = 0; i < wordList.length; ++i){
            word += "<li>" + wordList[i] + "</li>";
        }
        autocomplete.innerHTML = word;
    //입력 값이 없는 경우
    }else if(keyword == ""){
        autocomplete.innerHTML = "";
    //입력 값은 있지만, "cat"이 아닌 경우
    }else{
        autocomplete.innerHTML = "<li>검색 결과가 없습니다.</li>";
    }
    //이벤트 종료시 word 값 초기화
    word = "";
}, false);

