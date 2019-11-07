<template>
  <div>
    <div class="head">
      <div class="head_name">云端婚礼</div>
      <div class="head_mess">
        <img src="../assets/sch.png" class="search">
        <div class="screen_name">
          <el-dropdown>
  <span class="el-dropdown-link screen_name">
    曼****m<i class="el-icon-arrow-down el-icon--right"></i>
  </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>员工管理</el-dropdown-item>
            <el-dropdown-item>信息修改</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown></div>
        <img src="../assets/img11.png" class="portrait">
      </div>
    </div>
    <div class="content">
      <router-view/>
      <right/>
    </div>
  </div>
</template>

<script>
  import {left,right} from '@/components/homeshow';

  export default {
    name: 'App',
    data(){
      return{

      }
    },
    components: {
      left,
      right
    }
  }
</script>

<style>
  body{
    margin: 0;
    padding: 0;
  }
.head{
  width: 100%;
  height: 70px;
  background: url("../assets/head_img.png");
  display: flex;
  justify-content: space-between;
  line-height: 70px;
}
  .head_name{
    font-size: 30px;
    color: #ffffff;
    margin-left: 130px;
  }
  .head_mess{
    display: flex;
    justify-content: end;
    margin-right: 33px;
    align-items: center;
  }
  .search{
    width: 16px;
    height: 16px;
  }
  .screen_name{
    font-size: 16px;
    color: #ffffff;
    margin: 0 8px 0 20px;
  }
  .portrait{
    width: 24px;
    height: 24px;
    border-radius: 50%;
  }
  .content{
    display: flex;
    justify-content: flex-start;
  }
</style>
