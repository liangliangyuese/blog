// 调取接口
function user_info() {
    console.log("获取用户的个人信息");
    alert("获取用户的个人信息");
    $.ajax({
        type: "post",
        url: "/user/info/",
        data: {},
        dataType: "json",
        callback: "test",
        success: function (data) {
            console.log("渲染用户数据到页面");
            the_str = "<p>用户昵称：</p>" + "<p>用户邮箱：</p>" + "<p>用户头像：</p>"
            $(user_info_i).append(the_str)
        }
    })

}