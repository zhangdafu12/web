<template>
  <div class="hello">
    <div class="left" v-if="hide">
      <img src="../../assets/hide.png" class="left-hide" @click="hideCont">
      <router-view></router-view>
    </div>
    <img src="../../assets/show.png" class="left-show" v-if="show" @click="hideCont">
  </div>
</template>

<script>
export default {
  name:"left",
  data(){
    return{
      hide:true,
      show:false,
    }
  },
  methods:{
    hideCont: function() {
      this.show = !this.show;
      this.hide = !this.hide;
    }

  }
}
</script>

<style scoped>
  body{
    margin: 0;
    padding: 0;
  }
  p{
    margin: 0;
    padding: 0;
  }
  .left{
    width: 400px;
    height: 877px;
    background-color: #f0f0f0;
    border-right: 1px solid #E2E2E2;
    position: relative;
  }
  .left-hide{
    width: 30px;
    height: 30px;
    position: absolute;
    top:calc(50% - 15px);
    left: 385px;
    z-index: 200;
  }
  .left-show{
    width: 30px;
    height: 30px;
    position: absolute;
    top:calc(50% - 15px);
    left: 0;
    z-index: 999;
  }
</style>
