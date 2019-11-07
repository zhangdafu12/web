<template>
  <div class="left1">
    <div class="message">
      <img src="../../../assets/img11.png" class="head_img">
          <div class="private">
            <div class="name">瓜包熟吗</div>
            <div class="stylist">
              <img src="../../../assets/designer.png">
              <span v-show="isShow==1">设计师</span>
          <span v-show="isShow==0">摄影师</span>
        </div>
        <div class="phone">
          <img src="../../../assets/phone.png">
          <span>13858000000</span>
        </div>
      </div>
    </div>
    <div class="add">
      <button>添加我的盘符</button>
    </div>
    <div class="elect" v-show="isShow==0"  >
      <p>选择公司</p>
      <el-dropdown @command="vLoading">
        <el-button type="primary" >
          选择<i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown" >
          <el-dropdown-item >太郎花子</el-dropdown-item>
          <el-dropdown-item> 纽约纽约</el-dropdown-item>
          <el-dropdown-item>贝斯特</el-dropdown-item>
          <el-dropdown-item>春天里</el-dropdown-item>
          <el-dropdown-item>Bespoke婚礼</el-dropdown-item>
          <el-dropdown-item>苏州一生一世婚...</el-dropdown-item>
          <el-dropdown-item>苏州皇家婚庆集团</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <div class="electFlush" v-show="isShow==1">
      <span>太郎花子</span>
      <span @click="isShow=0"><img src="../../../assets/切换.png">切换公司</span>
    </div>
    <div class="box" v-show="isShow==1">
      <div class="case" @click="onPaper">
        <img src="../../../assets/folder.png">
        <p>时间+地点</p>
      </div>
      <div class="case" @click="onPaper">
        <img src="../../../assets/folder.png">
        <p>时间+地点</p>
      </div>
      <div class="case" @click="onPaper">
        <img src="../../../assets/folder.png">
        <p>时间+地点</p>
      </div>
      <div class="case" @click="onPaper">
        <img src="../../../assets/folder.png">
        <p>时间+地点</p>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "mine",
      data(){
          return{
            isShow:0
          }
      },
      methods:{
        onPaper(){
          this.$router.push({path:"paper"})
        },
        vLoading(){
          this.isShow=1;
          console.log(1111)
        }

      }
    }
</script>

<style scoped>

  .message {
    /*width: 400px;*/
    height: 139px;
    display: flex;
    justify-content: start;
    align-items: center;

    background: url("../../../assets/message_img.png");
  }
  .head_img{
    width: 64px;
    height: 64px;
    border-radius: 50%;
    margin:0 12px 0 23px;
  }
  .name{
    font-size: 15px;
    margin-top: 14px;
  }
  .stylist,.phone{
    display: inline-block;
    margin: 12px 20px 0 0;
    font-size: 12px;
    color: #f0f0f0;
  }

  .stylist span,.phone span{
    position: relative;
    bottom:3px;
  }
  .stylist img{
    width: 14px;
    height: 14px;
  }
  .phone img{
    width: 9px;
    height: 14px;
  }
  .add{
    width: 100%;
    height: 66px;
    line-height: 66px;
    text-align: center;
  }
  button{
    width: 250px;
    height: 36px;
    background-color: #3d97ff;
    border-radius: 5px;
    border: 0;
    color: #ffffff;
  }
  .box{
    background-color: #ffffff;
  }
  .case{
    height: 64px;
    display: flex;
    justify-content: start;
    align-items: center;

    border-bottom:1px solid #E7E7E7;
    padding-left: 17px;
  }
  .case:first-child{
    border-top:1px solid #E7E7E7;
  }
  .case img{
    width: 40px;
    height: 33px;
  }
  .case p{
    font-size: 15px;
    margin-left: 10px;
  }
  .elect{
    padding: 0 23px;
  }
  .elect p{
    display: inline-block;
    font-size: 15px;
    font-weight: 600;
    margin-right: 5px;
  }
  .elect .el-button--primary {
    width: 153px;
    height: 36px;
    background-color: #ffffff;
    border-radius: 5px;
    color: #78B6FF;
  }
  .electFlush{
    padding: 15px 23px 10px 17px;
    display: flex;
    justify-content: space-between;
    font-size: 15px;
  }
  .electFlush span:first-child{
    font-weight: 600;
  }
  .electFlush span:last-child{
    color: #5b5b5b;
  }
  .electFlush span img{
    width: 13px;
    height: 13px;
    margin-right: 3px;
  }
</style>
