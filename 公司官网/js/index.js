$(function () {
  //轮播
  carousel(
    $('.demo1'),	//必选， 要轮播模块(id/class/tagname均可)，必须为jQuery元素
    {
      type: 'leftright',	//可选，默认左右(leftright) - 'leftright' / 'updown' / 'fade' (左右/上下/渐隐渐现)
      arrowtype: 'move',	//可选，默认一直显示 - 'move' / 'none'	(鼠标移上显示 / 不显示 )
      autoplay: true,	//可选，默认true - true / false (开启轮播/关闭轮播)
      time: 5000	//可选，默认3000
    }
  );
  //视频播放控制
  var v = document.getElementsByClassName("myVideo");
  console.log(v, 111);
  $.each(v, function (i, v) {
    console.log(v);// 隐藏播放控制条，并且用点击 video 节点的时候 控制暂停和播放
    $(v).on('click', function () {
      var vPaused = v.paused;
      if (vPaused == true) {
        v.play();
      } else {
        v.pause();
      }
    });
  });
//横向滚动
  var length = 0;
  $(".control_right").click(function () {
    $(this).attr({src: "./images/arr_r_a.png"});
    $(this).prev().attr({src: "./images/arr_l.png"});
    if (length >= 2330) {
      $(".team_all ul").scrollLeft(2330);
      length = 2330;
    } else {
      length += 200;
      $(".team_all ul").scrollLeft(length);
    }
  });
  $(".control_left").click(function () {
    $(this).attr({src: "./images/arr_l_a.png"});
    $(this).next().attr({src: "./images/arr_r.png"});
    if (length <= 0) {
      $(".team_all ul").scrollLeft(0);
      length = 0;
    } else {
      length -= 200;
      $(".team_all ul").scrollLeft(length);
    }
  })
//  合作伙伴
  $(".teamwork_tips li").click(function () {
    console.log($(this).next().length)
    if ($(this).next().length == 0) {
      $(this).addClass("active");
      $(this).siblings().removeClass("active");
      $(".teamwork_show").eq(1).show();
      $(".teamwork_show").eq(0).hide();

    } else {
      $(this).addClass("active");
      $(this).siblings().removeClass("active");
      $(".teamwork_show").eq(0).show();
      $(".teamwork_show").eq(1).hide();

    }
  })
//复制文本
  $(".copy").click(function () {
    $('.tryInput input').select();
    document.execCommand("copy"); // 执行浏览器复制命令
  });
//下拉菜单
  $('.dropdown-toggle').dropdown();
});
