// html 요소 가져오기
// button = _______
var button = document.getElementById('button');
var input = document.getElementById('input');
var list = document.getElementById('list');

// 이벤트와 함수 연결하기
button.addEventListener('click', clickButton);

var listCount = 2;

// def clickButton
function clickButton() {
    //print
    console.log(input.value);
    var li = document.createElement('li');
    li.setAttribute("id", "li"+listCount)

    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.setAttribute("onclick", "clickCheckbox("+listCount+")")


    li.appendChild(checkbox);

    li.innerHTML += input.value;

    var buttonHtml = "<button type='button' style='float: right;' onclick='removeTodo(" + listCount + ")'>삭제</button></li>";
    li.innerHTML = li.innerHTML + buttonHtml
    list.appendChild(li);
    listCount = listCount + 1
}

function removeTodo(count) {
    var li = document.getElementById('li'+count)
    list.removeChild(li)
}

function clickCheckbox(count) {
    var li = document.getElementById('li'+count)
    if (li.style.textDecoration == 'line-through') {
        li.style.textDecoration = 'none'
    } else (
        li.style.textDecoration = 'line-through'
    )
}
