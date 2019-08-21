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