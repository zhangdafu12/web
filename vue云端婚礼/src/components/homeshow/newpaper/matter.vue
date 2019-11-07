<template>
  <div class="hello">
    <div class="seek">
      <input placeholder="请输入"></input>
      <img src="../../../assets/search.png"></img>
    </div>
    <div class="box-cont">
      <div class="box">
        <div class="box-left">
          <img src="../../../assets/技术文档.png">
          <div class="paper">
            <p class="paper-name">新郎.jpg</p>
            <p class="paper-time">2019/07/13 12:23</p>
          </div>
        </div>
        <div class="box-right">来自：阿星</div>
      </div>
      <div class="box">
      <div class="box-left">
        <img src="../../../assets/技术文档.png">
        <div class="paper">
          <p class="paper-name">新郎.jpg</p>
          <p class="paper-time">2019/07/13 12:23</p>
        </div>
      </div>
      <div class="box-right">来自：阿星</div>
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
    name: "matter"
  }
</script>

<style scoped>
  p{
    margin: 0;
    padding: 0;
  }
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
    margin-bottom: 10px;
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
    height: 80px;
    margin:0 23px 0 23px;
    border-bottom: solid 1px #e0e0e0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .box-left{
    display: flex;
    justify-content: space-between;
  }
  .box-left img{
    width: 33px;
    height: 41px;
    margin-right: 15px;
  }
  .paper-name{
    font-size: 15px;
  }
  .paper-time,.box-right{
    font-size: 12px;
    color: #9b9b9b;
    margin-top: 4px;
  }
  .box-right{
    margin-top: 24px;
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
