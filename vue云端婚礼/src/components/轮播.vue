<template>
    <div class="lunbo">
      <div class="big-cont">
        <ul class="big-img">
          <li v-for="(item, index) in imgs" :key="index">
            <img :src="item.img" alt="">
          </li>
        </ul>
        <div class="left-img">
          <img src="../assets/left.png">
        </div>
        <div class="right-img">
          <img src="../assets/right.png">
        </div>
      </div>
      <div class="title-cont">
        <ul class="title-img">
          <li></li>
        </ul>

      </div>
    </div>
</template>

<script>
    export default {
      name: 'lunbo',
      data(){
          return{
            imgs: [
              {
                img: 'http://img.hb.aicdn.com/adbde61e4343dedd21e97ea7f22666825a8db7d077ffe-qn8Pjn_fw658'
              },
              {
                img: 'http://img.hb.aicdn.com/adeed7d28df6e776c2fa6032579c697381d1a82b7fe00-fwRqgn_fw658'
              },
              {
                img: 'http://img.hb.aicdn.com/ab7f48509b3c0353017d9a85ef1d12400c9b2724540d4-p3zouo_fw658'
              },
              {
                img: 'http://img.hb.aicdn.com/60f788fc2a846192f224b9e6d4904b30e54926211d3d67-ACFJ9G_fw658'
              },
              {
                img: 'http://img.hb.aicdn.com/22ded455284aab361b8d2056e82f74a891a019704296a-PSraEB_fw658'
              }]
          }
      }
    }
</script>

<style scoped>
ul, li{
  margin: 0;
  padding: 0;
  list-style: none;
}
.big-cont{
  width: 1220px;
  height: 654px;
  margin: 0 auto;
  overflow: hidden;
  position: relative;
}
.big-img{
  width: 7000px;
}
.big-img li{
  float: left;
}
.big-img img{
  width: 1220px;
  height: 654px;
}
.left-img,.right-img{
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: #3d97ff;
}
.left-img img,.right-img img{
  width: 12px;
  height: 21px;
}
  .left-img{
    position: absolute;
    top:calc(50% - 30px);
    left: -70px;
    z-index: 999;

  }
</style>
