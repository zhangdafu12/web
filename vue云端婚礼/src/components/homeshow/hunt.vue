<template>
    <div class="hunt">
      <h3>聚合搜索模式</h3>
      <div class="hunt-input">
        <input type="text" placeholder="请输入"></input>
        <img src="../../assets/search.png">
      </div>
      <div class="hunt-cont">
        <input type="radio" v-model="bill" value="one"></input>
        <label>图片</label>
        <input type="radio" v-model="bill" value="two"></input>
        <label>视频</label>
        <input type="radio" v-model="bill" value="three"></input>
        <label>设计原件</label>
        <input type="radio" v-model="bill" value="four"></input>
        <label>方案</label>
      </div>
    </div>
</template>

<script>
    export default {
        name: "hunt",
      data(){
          return{
            bill:""
          }
      }
    }
</script>

<style scoped>
  *{
    box-sizing: border-box;
  }
  body{
    margin: 0;
    padding: 0;
  }
  h3{
    margin: 0;
    padding: 0;
  }
  .hunt{
    width: 100%;
    margin-top: 180px;
    text-align: center;
  }
  .hunt-input{
    margin-top: 23px;
    position: relative;
  }
  .hunt-input input{
    width: 466px;
    height: 38px;
    background-color: #e9e9e9;
    border-radius: 5px;
    border: none;
    outline: none;
    padding-left: 10px;
  }
  .hunt-input img{
    width: 16px;
    height: 16px;
    position:absolute;
    top:calc(50% - 9px);
    right:calc(39% - 9px);
    z-index: 100;
  }
  .hunt-cont{
    margin-top: 10px;
  }
  .hunt-cont label{
    font-size: 15px;
    color: #5b5b5b;
    margin-right: 20px;
  }
  .hunt-cont label:last-child{
    margin-right: 0;
  }
</style>
