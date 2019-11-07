<template>
  <div class="hello">
    <div class="project">
      <div class="project_name">
        <div class="name">项目名称</div>
        <router-link to="/#" class="back">返回</router-link>
      </div>
      <div class="drop_down">
        <el-dropdown>
          <el-button type="primary">
          中式<i class="el-icon-arrow-down el-icon--center"></i>
        </el-button>
          <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>中式一</el-dropdown-item>
          <el-dropdown-item>中式二</el-dropdown-item>
          <el-dropdown-item>中式三</el-dropdown-item>
          <el-dropdown-item>中式四</el-dropdown-item>
          <el-dropdown-item>中式五</el-dropdown-item>
        </el-dropdown-menu>
        </el-dropdown>
        <el-dropdown>
          <el-button type="primary">
            红色<i class="el-icon-arrow-down el-icon--center"></i>
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>橙色</el-dropdown-item>
            <el-dropdown-item>黄色</el-dropdown-item>
            <el-dropdown-item>绿色</el-dropdown-item>
            <el-dropdown-item>青色</el-dropdown-item>
            <el-dropdown-item>蓝色</el-dropdown-item>
            <el-dropdown-item>紫色</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
    <div class="tab">
        <ul class="tab-tilte">
          <li @click="cur(0)" :class="{active:curs==0}">
            <img src="../../../assets/微信.png" class="tab-img1">
            <span>微信</span>
          </li>
          <li @click="cur(1)" :class="{active:curs==1}">
            <img src="../../../assets/信息实图.png" class="tab-img2">
            <span>客户</span>
          </li>
          <li @click="cur(2)" :class="{active:curs==2}">
            <img src="../../../assets/技术文档.png" class="tab-img3">
            <span>文件</span>
          </li>
          <li @click="cur(3)" :class="{active:curs==3}">
            <img src="../../../assets/图片.png" class="tab-img4">
            <span>图片</span>
          </li>
        </ul>
        <div class="tab-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>

    export default {
      name: "paper",
      data(){
        return{
          curs: 0 //默认选中第一个tab
        }
      },
      methods:{
        cur:function(index){
          this.curs=index;
          var path=['message','client','matter','pictures'];
            this.$router.push({
              name:path[index]
            })
        }
      }
    }

</script>

<style scoped>
  a {
    text-decoration: none;
  }
  .project{
    padding: 32px 23px 16px 23px;
  }
  .project_name{
    display: flex;
    justify-content: space-between;
    margin-bottom: 15px;
  }
  .name{
    font-size: 15px;
    font-weight: 600;
  }
  .back{
    font-size: 15px;
    color: #3d97ff;
  }
  .el-button--primary {
    width: 100px;
    height: 36px;
    background-color: #ffffff;
    border: 0;
    color: #5b5b5b;
    border-radius: 5px;
    margin-right: 15px;
  }
  .el-dropdown-menu__item{
    width: 100px;
    text-align: center;
  }
  .tab{
    width: 100%;
    height: 56px;
    background-color: #e0e0e0;
  }

  ul,li {

    margin: 0;
    padding: 0;
    list-style: none;
  }
  .tab-img1{
    width: 31px;
    height: 25px;
  }
  .tab-img2{
    width: 24px;
    height: 25px;
  }
  .tab-img3{
    width: 19px;
    height: 22px;
  }
  .tab-img4{
    width: 26px;
    height: 21px;
  }
  .tab-tilte {
    width: 100%;
    height: 53px;
    line-height: 53px;
  }
  .tab-tilte li {
    float: left;
    width: 25%;
    display: flex;
    justify-content: center;
    align-items:center;
    cursor: pointer;
  }
  .tab-tilte li span{
    font-size: 15px;
    margin-left: 8px;
  }
  .tab-tilte .active {
    border-bottom: solid 3px #3d97ff;
  }

  /*.tab-content div {*/
  /*  float: left;*/
  /*  width: 25%;*/
  /*  line-height: 100px;*/
  /*  text-align: center;*/
  /*}*/
</style>
