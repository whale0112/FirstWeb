window.onload = function () {
    var head = document.getElementById('head');
    head.addEventListener('click', function(){
        var date = new Date();
        alert(date);
    });
}
        // head 에서 불러옴
        // window.onload 없는 상태로 실행하면 오류가 남
        // -> body를 그리기 전에 script를 실행하므로

        // window.onload : 웹브라우저 로드가 끝났을때 호출됨
        