<template>
  <div class="hello">
    <div class="seek">
      <input placeholder="请输入"></input>
      <img src="../../../assets/search.png"></img>
    </div>
    <div class="box-cont">
      <div class="box">
        <div class="mess">
          <div class="mess-left">
            <span class="name">随风飘去</span>
            <span class="time">2019/07/13 12:23</span>
          </div>
          <div class="mess-right">
            <img src="../../../assets/微信.png">
            <span class="weixin">微信</span>
          </div>
        </div>
        <div class="gaine">确认伴娘和伴郎的人选、确认花童、戒童、主婚人、证婚人</div>
      </div>
      <div class="box">
        <div class="mess">
          <div class="mess-left">
            <span class="name">往事随风</span>
            <span class="time">2019/07/13 12:23</span>
          </div>
          <div class="mess-right">
            <img src="../../../assets/信息实图.png">
            <span class="weixin">WebBox</span>
          </div>
        </div>
        <div class="gaine client">新郎新娘开始规律的管理皮肤、身材，调整作息、饮食等</div>
      </div>
    </div>
    <div class="send">
      <input type="text" placeholder="请输入"></input>
      <input type="submit" value="发送"></input>
    </div>

  </div>
</template>

<script>
  export default {
    name: "client"
  }
</script>

<style scoped>
  input{
    margin: 0;
    padding: 0;
    outline: none;
  }
  .hello{
    height: 705px;
    position:relative ;
  }
  .seek{
    text-align: center;
    position: relative;
    padding-top: 20px;
  }
  .seek input{
    width: 342px;
    height: 38px;
    background-color: #ffffff;
    border-radius: 5px;
    border: 0;
    padding-left: 12px;
  }
  .seek img{
    width: 16px;
    height: 17px;
    position: absolute;
    right: 38px;
    top: 32px;
  }
  .box{
    margin:30px 23px 0 23px;
  }
  .mess{
    display: flex;
    justify-content: space-between;

  }
  .name{
    font-size: 15px;
  }
  .time,.weixin{
    font-size: 12px;
    color: #9b9b9b;
  }
  .mess-right{
    padding: 4px 9px;
    background-color: #ffffff;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .mess-right img{
    width: 15px;
    height: 13px;
    margin-right: 3px;
  }
  .gaine{
    background-color: #4dcb06;
    border-radius: 5px;
    margin-top: 8px;
    line-height: 21px;
    padding: 15px 9px;
    font-size: 14px;
  }
  .client{
    background-color: #e8d801;
  }
  .send{
    width: 100%;
    display: flex;
    justify-content: center;
    position: absolute;
    bottom: 23px;
  }
  .send input[type="text"]{
    width: 280px;
    height: 38px;
    border: 0;
    padding-left: 12px;
    border-radius:5px 0px 0px 5px;
  }
  .send input[type="submit"]{
    width: 62px;
    height: 38px;
    background-color: #3d97ff;
    border-radius: 0px 5px 5px 0px;
    border: 0;
    color: #fff;
  }
</style>
