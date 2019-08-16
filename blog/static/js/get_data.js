// 调取接口
function user_info() {
    console.log("获取用户的个人信息");
    $.ajax({
        type: "post",
        url: "/user/info/",
        data: {},
        dataType: "json",
        callback: "test",
        success: function (data) {
            console.log(data);
            the_str =
                "<p>用户昵称：" + data.username + "</p>" +
                "<p>用户邮箱：" + data.email + "</p>" +
                "<p>用户电话：" + data.phone + "</p>" +
                "<p>用户头像</p>" +
                "<img src='" + data.user_img + "' alt='用户头像' style='width: 100px'/>";
            $(user_info_i).append(the_str)
        }
    })

}