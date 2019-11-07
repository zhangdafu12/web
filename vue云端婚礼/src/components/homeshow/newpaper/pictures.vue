<template>
    <div class="hello">
      <div class="seek">
        <input placeholder="请输入"></input>
        <img src="../../../assets/search.png"></img>
      </div>
      <div class="box-cont">
        <div class="box">
          <div class="box-time">2019/07/13 12:23</div>
          <div class="box-img">
            <img src="../../../assets/img11.png" @click="goNewPage">
            <img src="../../../assets/img11.png" @click="goNewPage">
            <img src="../../../assets/img11.png" @click="goNewPage">
          </div>
        </div>
        <div class="box">
          <div class="box-time">2019/07/13 12:23</div>
          <div class="box-img">
            <img src="../../../assets/img11.png" @click="goNewPage">
            <img src="../../../assets/img11.png" @click="goNewPage">
            <img src="../../../assets/img11.png" @click="goNewPage">
            <img src="../../../assets/img11.png" @click="goNewPage">
            <img src="../../../assets/img11.png" @click="goNewPage">
          </div>
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
        name: "pictures",
        data:function(){
          return{

          }
        },
        methods:{
          goNewPage:function(){
            this.$router.push({
              name:'newPage'
            })
          }
        },
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
  .box-cont{
    padding:0 23px;
  }
  .box-time{
    font-size: 15px;
    color: #9b9b9b;
    padding: 25px 0 10px 0;
    border-bottom: solid 1px #e0e0e0;
    margin-bottom: 3px;
  }
  .box-img img{
    width: 90px;
    height: 70px;
    margin: 10px 10px 0 0;
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
