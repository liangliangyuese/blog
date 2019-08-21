let myimg = document.querySelector('img');
myimg.onclick = function () {
    alert('添加点击事件，修改当前图片');
    let imgsrc = myimg.getAttribute('src');
    if (imgsrc == "/static/image/791e1a3aff021817b4028b1d91b92f80.jpeg") {
        myimg.setAttribute('src', '/static/image/c0a054d72dddb1df0d22f0bd2956a112.jpeg')
    } else {
        myimg.setAttribute('src', '/static/image/791e1a3aff021817b4028b1d91b92f80.jpeg')
    }
};

//替换h1标签内容
function setHead(name) {
    let myHead = document.querySelector('h1');
    myHead.textContent = '欢迎你' + name + '!'
}

//设置输入 内容设置到storage
function setName() {
    let myName = prompt('输入名称');
    localStorage.setItem('name', myName);
    setHead(myName)
}

let storgname = localStorage.getItem('name');
if (storgname) {
    setHead(storgname)
} else {
    setName();
}

let mybutton = document.querySelector('button');
mybutton.onclick = setName;