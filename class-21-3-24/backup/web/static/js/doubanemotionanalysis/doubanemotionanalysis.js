// $(document).ready(function () {
//     $(".testb").click(function () {
//         $(".testp").slideToggle();
//         console.log("helloworld")
//     });
// });



// var doubanemotionanalysis = {
//     init: function () {
//         this.eventBind();
//         console.log("111")
//     },


//     // 事件绑定
//     eventBind: function () {
//         $(".card-content .do-analysis").click(function () {

//             var id = $(".card-content .do-analysis").val();

//             console.log(id)
//             $.ajax({
//                 url: common_ops.buildUrl("/wordcloud/emotionanalysis"),
//                 type: "POST",
//                 data: {
//                     'bookid': id
//                 },
//                 datatype: 'json',
//                 success: function (res) {
//                     common_ops.alert("nihao!")
//                 }
//             })
//         });
//     }
// }

// $(document).ready(function () {
//     doubanemotionanalysis.init();
//     console.log("222")
// });