// 获取热门文章列表
function hot_article_list() {
    console.log("获取当前热门文章");
    $.ajax({
            type: "get",
            url: "/article/hot/",
            data: {},
            dataType: "json",
            // TODO 回调函数
            callback: "test",
            success: function (data) {
                console.log("文章的列表渲染");
                // the_str =
                //     "<p>用户昵称：" + data.username + "</p>" +
                //     "<p>用户邮箱：" + data.email + "</p>" +
                //     "<p>用户电话：" + data.phone + "</p>" +
                //     "<p>用户头像</p>" +
                //     "<img src='" + data.user_img + "' alt='用户头像' style='width: 100px'/>";
                // $(user_info_i).append(the_str);

                data = [{
                    "label": "HTML",
                    "collect": "100",
                    "like": "100",
                    "title": "HTML的来源",
                    "content": "HTML的来源HTML的来源HTML的来源HTML的来源HTML的来源HTML的来源"
                }, {
                    "label": "CSS",
                    "collect": "200",
                    "like": "200",
                    "title": "CSS的来源",
                    "content": "CSS的来源CSS的来源CSS的来源CSS的来源CSS的来源CSS的来源"
                }];

                var the_str = "<ul  style='list-style-type:none;'>";
                for (let i = 0; i < data.length; i++) {
                    console.log("当前的内容");
                    console.log(the_str);
                    the_str +=
                        "<li>" + "文章标题：" + data[i]["title"] + "</li>" +
                        "<li>" + "文章内容：" + data[i]["content"] + "</li>" +
                        "<li>" + "文章标签：" + data[i]["label"] + "</li>" +
                        "<li>" + "文章收藏：" + data[i]["collect"] + "</li>" +
                        "<li>" + "文章点赞：" + data[i]["like"] + "</li>"
                }
                the_str += "</ul>";
                console.log("最终拼接结果");
                console.log(the_str);
                $(hot_article).append(the_str);
            }

        }
    )

}
