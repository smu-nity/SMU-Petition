// 모달 창 끄기 + 다시 보지 않음 쿠키 설정
var home = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];
var expiredays = 7;

$( document ).ready(function() {
    cookiedata = document.cookie;
    if ( cookiedata.indexOf("ncookie=done") < 0 ){
        home.style.display = "block";    //  팝업창 아이디
    } else {
        home.style.display = "none";    // 팝업창 아이디
    }
});

function setCookie(name, value) {
    var todayDate = new Date();
    todayDate.setDate( todayDate.getDate() + expiredays);
    document.cookie = name + "=" + escape( value ) + "; path=/; expires=" + todayDate.toGMTString() + ";"
}

var Spanclick_set_cookie = function (x, y) {
    x.onclick = function () {
        y.style.display = "none";
        var chk = document.getElementById('unlook');
        // 체크하고 누르면 쿠키 생성
        if (chk.checked) {
            setCookie("ncookie", "done");
        }
    }
}
Spanclick_set_cookie(span, home);

window.onclick = function (event) {
    if (event.target == target_modal) {
        target_modal.style.display = "none";
    }
}
window.onclick = function (event) {
    if (event.target == home) {
        home.style.display = "none";
    }
}
