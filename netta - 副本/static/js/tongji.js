/**
 * Created by BYM on 2016/8/29.
 */
var second = 0;
window.setInterval(function () {
    second++;
}, 1000);


$(function () {
    var mousemove = [];
    var mouseclick = [];
    var keyboard = [];
    var el = window.document.body;
    var time;
    var locationarray = [];

    function test() {
        var t = document.documentElement.scrollTop || document.body.scrollTop;
        if (locationarray.length > 0) {
            var lastvalue = locationarray[locationarray.length - 1][0];
            if (lastvalue == t) {
                locationarray[locationarray.length - 1][1] += 1;
            }
            else {
                locationarray.push([t, 1]);
            }
        }
        else {
            locationarray.push([t, 1]);
        }
    }

    document.body.addEventListener('mouseover', function (event) {
        el = event.target;//鼠标每经过一个元素，就把该元素赋值给变量el
        time = new Date().getTime();
    });
    document.body.addEventListener('click', function (event) {
        el_click = event.target;
        if (el_click.tagName === "BODY") {
            return
        }
    mouseclick.push(['click', el_click.textContent, el_click.getAttribute('href'), el_click.getAttribute('src'), new Date().getTime()]);
    });
    // document.body.addEventListener('contextmenu',function(event){
    //     el_click = event.target;
    //     if(el_click.tagName === "BODY"){
    //         return
    //     }
    //      mouseclick.push(['contextmenu',el_click.textContent,el_click.getAttribute('href'),el_click.getAttribute('src'),new Date().getTime()]);
    // });
    document.body.addEventListener('dblclick', function (event) {
        el_click = event.target;
        if (el_click.tagName === "BODY") {
            return
        }

        mouseclick.push(['dblclick', el_click.textContent, el_click.getAttribute('href'), el_click.getAttribute('src'), new Date().getTime()]);
    });
    console.log(mouseclick);
    document.body.addEventListener('mouseout', function (event) {
        el = event.target;//鼠标每经过一个元素，就把该元素赋值给变量el
        if (new Date().getTime() - time > 1000) {

            if (el.tagName !== "BODY") {
                mousemove.push([el.textContent, el.getAttribute('href'), el.getAttribute('src'), new Date().getTime() - time]);

            }
        }
    });

    console.log(mousemove);
    $(document).keydown(function (event){
        if(event.ctrlKey && event.keyCode == 67){
            var txt = window.getSelection?window.getSelection():document.selection.createRange().text;
            keyboard.push(['ctrl+c',txt.toString(),new Date().getTime()]);
            console.log(keyboard);
        }
    
  });


    function send_data() {

        var dataArr = {
            'url': location.href,
            'mousemove': mousemove,
            'mouseclick': mouseclick,
            'keyboard': keyboard,
            'locationarray': locationarray,
            'time': second,

        };
        console.log(dataArr);
        mouseclick = [];
        mousemove = [];
        keyboard = [];
        locationarray = [];
        $.ajax({
            url: "/info",
            type: "POST",
            dataType: 'json',
            data: JSON.stringify(dataArr),
            contentType: "application/x-www-form-urlencoded; charset=utf-8",
            success: function (msg) {

            }
        });
    }

    send_data();
    setInterval(function () {
        test()
    }, 200);
    setInterval(send_data, 100000);
});


// function getReferrer() {
//     var referrer = '';
//     try {
//         referrer = window.top.document.referrer;
//     } catch(e) {
//         if(window.parent) {
//             try {
//                 referrer = window.parent.document.referrer;
//             } catch(e2) {
//                 referrer = '';
//             }
//         }
//     }
//     if(referrer === '') {
//         referrer = document.referrer;
//     }
//     return referrer;
// }