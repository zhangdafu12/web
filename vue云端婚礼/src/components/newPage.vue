<template>
  <div class="hello-cont">
    <div class="shade" v-if="shade"></div>
    <div class="collec-cont" v-if="hidden">
      <div class="coll_cont">
        <p>收藏</p>
        <img src="../assets/remove.png" @click="onHidden">
      </div>
      <img class="collec-imgs" src="../assets/surmon-1.jpg">
      <input type="text" placeholder="文字描述" class="describe"></input>
      <p class="task-p">选择任务管理器</p>
      <div class="task-manager">
        <div class="task" @click="onHidden1">
          <img src="../assets/task.png">
          <p>时间＋地点</p>
        </div>
        <div class="task">
          <img src="../assets/task.png">
          <p>时间＋地点</p>
        </div>
        <div class="task">
          <img src="../assets/task.png">
          <p>时间＋地点</p>
        </div>
        <div class="task">
          <img src="../assets/task.png">
          <p>时间＋地点</p>
        </div>
        <div class="task">
          <img src="../assets/task1.png">
          <p>添加任务管理器</p>
        </div>
      </div>
      <button class="ensure">确 定</button>
    </div>
    <div class="collec-cont1" v-if="hidden1">
      <div class="coll_cont">
        <p>收藏</p>
        <img src="../assets/remove.png" @click="onHidden2">
      </div>
      <form>
        <label>时间</label>
        <input type="text" class="time"></input><br>
        <label>地点</label>
        <input type="text" class="site"></input><br>
        <label>客户</label>
        <input type="text" class="client"></input><br>
        <label>销售</label>
        <input type="text" class="sell"></input><br>
        <label>设计</label>
        <input type="text" class="design"></input><br>
        <label>添加标签</label><br>
        <el-dropdown>
          <el-button type="primary">
            风格<i class="el-icon-arrow-down el-icon--center"></i>
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>风格一</el-dropdown-item>
            <el-dropdown-item>风格二</el-dropdown-item>
            <el-dropdown-item>风格三</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <el-dropdown>
          <el-button type="primary">
            色系<i class="el-icon-arrow-down el-icon--center"></i>
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>橙色</el-dropdown-item>
            <el-dropdown-item>黄色</el-dropdown-item>
            <el-dropdown-item>绿色</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown><br>
        <label>自定义标签</label><br>
        <button class="but manner">风格</button>
        <button class="but colour">色系</button><br>
        <button class="but certain">确 定</button>


      </form>
    </div>
    <div class="pattern">
      <div class="lump video">
        <img src="../assets/video.png">视频模式
      </div>
      <div class="lump print">
        <img src="../assets/print.png">图片模式
      </div>
    </div>
    <div class="collect" @click="onHidden">
      <img src="../assets/collect.png">
    </div>
    <div class="swiper-box">
      <!-- swiper1 -->
      <swiper :options="swiperOptionTop" class="gallery-top" ref="swiperTop">
        <swiper-slide class="slide-1">
          <img src="../assets/surmon-1.jpg">
        </swiper-slide>
        <swiper-slide class="slide-2">
          <img src="../assets/surmon-2.jpg">
        </swiper-slide>
        <swiper-slide class="slide-3">
          <img src="../assets/surmon-3.jpeg">
        </swiper-slide>
        <swiper-slide class="slide-4">
          <img src="../assets/surmon-4.jpg">
        </swiper-slide>
        <swiper-slide class="slide-5">
          <img src="../assets/surmon-5.jpg">
        </swiper-slide>
        <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
        <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>

      </swiper>
      <!-- swiper2 Thumbs -->
      <div class="area">
        <div class="lump usher">酒店迎宾区</div>
        <div class="lump sweet">甜品区</div>
        <div class="lump runway">T台区</div>
        <div class="lump editor">主舞台区</div>
      </div>
      <swiper :options="swiperOptionThumbs" class="gallery-thumbs" ref="swiperThumbs">
        <swiper-slide class="slide-1">
          <img src="../assets/surmon-1.jpg">
        </swiper-slide>
        <swiper-slide class="slide-2">
          <img src="../assets/surmon-2.jpg">
        </swiper-slide>
        <swiper-slide class="slide-3">
          <img src="../assets/surmon-3.jpeg">
        </swiper-slide>
        <swiper-slide class="slide-4 ">
          <img src="../assets/surmon-4.jpg">
        </swiper-slide>
        <swiper-slide class="slide-5">
          <img src="../assets/surmon-5.jpg">
        </swiper-slide>
        <div class="position swiper-button-next1" slot="button-next"></div>
        <div class="position swiper-button-prev1" slot="button-prev"></div>
      </swiper>

    </div>

  </div>
</template>
<script>
  export default {
    data() {
      return {
        hidden:false,
        hidden1:false,
        shade:false,
        swiperOptionTop: {
          spaceBetween: 10,
          // loop: true,
          // loopedSlides: 5, //looped slides should be the same
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        swiperOptionThumbs: {
          spaceBetween: 10,
          slidesPerView: 'auto',
          centeredSlides: true,
          touchRatio: 0.2,
          // loop: true,
          // loopedSlides: 5, //looped slides should be the same
          slideToClickedSlide: true,
          navigation: {
            nextEl: '.swiper-button-next1',
            prevEl: '.swiper-button-prev1'
          }
        }
      }
    },
    mounted() {
      this.$nextTick(() => {
        const swiperTop = this.$refs.swiperTop.swiper;
        const swiperThumbs = this.$refs.swiperThumbs.swiper;
        swiperTop.controller.control = swiperThumbs;
        swiperThumbs.controller.control = swiperTop
      })
    },
    methods: {
      onHidden: function () {
        this.hidden = !this.hidden
        this.shade = !this.shade
      },
      onHidden1: function () {
        this.hidden1 = !this.hidden1;
        this.hidden = !this.hidden;
      },
      onHidden2: function () {
        this.hidden1 = !this.hidden1;
        this.shade = !this.shade
      }
    },


  }
</script>

<style scoped>
  *{
  box-sizing: border-box;
  }
  p{
    margin: 0;
    padding: 0;
  }
  input,button{
    border: none;
    outline: none;
  }
  /*.position{*/
  /*  position: relative;*/
  /*  top: 700px;*/
  /*  z-index: 999;*/
  /*}*/

  .hello-cont{
    position: relative;
    padding-top: 50px;
    height: 947px;
    background-color: #2F302F;
  }
  .shade{
    width: 100%;
    height: 100%;
    background-color: #000000;
    opacity: 0.5;
    position: absolute;
    top:0;
    left: 0;
    z-index: 200;
  }
  .collect{
    position: absolute;
    top:80px;
    right: 380px;
    z-index: 100;
  }
  .collect img{
    width: 39px;
    height: 36px;
  }
  .collec-cont,.collec-cont1{
    width: 496px;
    height: 612px;
    background-color: #ffffff;
    border-radius: 5px;
    z-index: 301;
    position: absolute;
    top:calc(50% - 306px);
    left:calc(50% - 248px);
  }

  .coll_cont{
    width: 100%;
    height: 76px;
    line-height: 77px;
    border-bottom: solid 1px #e0e0e0;
    padding: 0 23px;
    position: relative;
  }
  .coll_cont img{
    width: 15px;
    height: 16px;
    position: absolute;
    right: 23px;
    top:23px;
  }
  .collec-imgs{
    width: 262px;
    height: 140px;
    border-radius: 5px;
    margin: 30px 117px;
  }
  .describe{
    width: 450px;
    height: 69px;
    background-color: #f0f0f0;
    border-radius: 5px;
    border: none;
    outline: none;
    margin: 0 23px;
    padding-left: 10px;
  }
  .task-p{
    margin: 15px 23px;
    font-size: 15px;
  }
  .task-manager{
    width: 450px;
    height: 120px;
    background-color: #f0f0f0;
    border-radius: 5px;
    margin: 0 23px;
    display: flex;
    justify-content: space-between;
  }
  .task{
    width: 20%;
    text-align: center;
    padding:21px 0 ;
    font-size: 11px;
  }
  .task img{
    width: 44px;
    height: 55px;
    margin-bottom: 5px;
  }
  .ensure{
    width: 100px;
    height: 36px;
    background-color: #3d97ff;
    border-radius: 5px;
    border: none;
    outline: none;
    color: #fff;
    margin: 26px 198px 0 198px;
  }
  form{
    margin: 0 23px;
  }
  form input{
    margin: 15px 0 0 5px;
    width: 170px;
    height: 36px;
    background-color: #f0f0f0;
    border-radius: 5px;

    padding-left: 10px;
  }
  .design{
    margin-bottom: 15px;
  }
  form label{
    font-size: 15px;
  }
  .el-dropdown{
    margin: 15px 0;
  }
  .el-button--primary {
    width: 100px;
    height: 36px;
    background-color: #f0f0f0;
    border: 0;
    color: #5b5b5b;
    border-radius: 5px;
    margin-right: 15px;
  }
  .el-dropdown-menu__item{
    width: 100px;
    text-align: center;
  }
  .but{
    width: 100px;
    height: 36px;
    border-radius: 5px;

  }
  .manner,.colour{
    background-color: #f0f0f0;
    margin: 15px 15px 0 0;
    color: #9b9b9b;
  }
  .certain{
    background-color: #3d97ff;
    margin: 40px 175px 0 175px;
    color: #fff;
  }
  .pattern{
    position: absolute;
    top:50px;
    right: 100px;
    z-index: 400;
  }
  .lump{
    color: #fff;
    width: 132px;
    height: 36px;
    /*line-height: 36px;*/
    /*text-align: center;*/
    background-color: #171717;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 15px;
  }
  .print{
    margin-top: 12px;
    background-color: #3d97ff;
  }
  .video img,.print img{
    width: 31px;
    height: 20px;
    margin-right: 10px;
  }
  .area{
    margin:20px 0 20px 350px;
  }
  .area .lump{
    display: inline-block;
    text-align: center;
    line-height: 36px;
  }
  .gallery-top .swiper-button-next,
  .gallery-top .swiper-button-prev{
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 0;
    background-color: #3d97ff;
    font-size: 20px;
  }
  .swiper-box{
    width: 100%;
    /*height: 947px;*/
    /*background-color: #000;*/
    /*position: relative;*/
  }


  .gallery-top img{
    width: 1220px;
    height: 654px;
  }
  .gallery-thumbs img{
    width: 235px;
    height: 141px;
  }
  .gallery-thumbs .swiper-slide{
    width: 235px;
    height: 141px;
  }
  .swiper-container:nth-child(1) {
    width: 100%;
    text-align: center;
  }
  .swiper-container:nth-child(2) {
    width: 1620px;
    overflow: hidden;
  }
  /*.swiper-slide {*/
  /*  background-size: cover;*/
  /*  background-position: center;*/
  /*}*/
  /*.gallery-top {*/
  /*  height: 80%!important;*/
  /*  width: 100%;*/
  /*}*/
  .gallery-thumbs {
    /*height: 20%!important;*/
    box-sizing: border-box;
    /*padding: 10px 0;*/
  }
  .gallery-thumbs .swiper-slide {
    width: 235px;
    height: 141px;
    opacity: 0.4;
  }
  .gallery-thumbs .swiper-slide-active {
    opacity: 1;
  }
</style>


<!--<template>-->
<!--  <div id="dataCenter">-->
<!--    <div class="window" @mouseover="stop" @mouseleave="play">-->
<!--      <ul class="container" :style="containerStyle">-->
<!--        <li>-->
<!--          &lt;!&ndash; 把最后一张图放在最开始 &ndash;&gt;-->
<!--          <img :style="{width:imgWidth+'px'}" :src="sliders[sliders.length - 1].img" alt="">-->
<!--        </li>-->
<!--        <li  v-for="(item, index) in sliders" :key="index">-->
<!--          <img :style="{width:imgWidth+'px'}" :src="item.img" alt="" @click="amplification(index)">-->
<!--        </li>-->
<!--        <li>-->
<!--          &lt;!&ndash; 把第一张图放在最后 &ndash;&gt;-->
<!--          <img :style="{width:imgWidth+'px'}" :src="sliders[0].img" alt="">-->
<!--        </li>-->
<!--      </ul>-->
<!--      // 左右切换按钮-->
<!--      <ul class="direction">-->
<!--        <li class="left" @click="move(imgWidth, 1, speed)">-->
<!--          <svg class="icon" width="30px" height="30.00px" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path fill="#ffffff" d="M481.233 904c8.189 0 16.379-3.124 22.628-9.372 12.496-12.497 12.496-32.759 0-45.256L166.488 512l337.373-337.373c12.496-12.497 12.496-32.758 0-45.255-12.498-12.497-32.758-12.497-45.256 0l-360 360c-12.496 12.497-12.496 32.758 0 45.255l360 360c6.249 6.249 14.439 9.373 22.628 9.373z"  /></svg>-->
<!--        </li>-->
<!--        <li class="right" @click="move(imgWidth, -1, speed)">-->
<!--          <svg class="icon" width="30px" height="30.00px" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path fill="#ffffff" d="M557.179 904c-8.189 0-16.379-3.124-22.628-9.372-12.496-12.497-12.496-32.759 0-45.256L871.924 512 534.551 174.627c-12.496-12.497-12.496-32.758 0-45.255 12.498-12.497 32.758-12.497 45.256 0l360 360c12.496 12.497 12.496 32.758 0 45.255l-360 360c-6.249 6.249-14.439 9.373-22.628 9.373z"  /></svg>-->
<!--        </li>-->
<!--      </ul>-->
<!--      // 小圆点-->
<!--      <ul class="dots">-->
<!--        <li v-for="(dot, i) in sliders" :key="i"-->
<!--            :class="{dotted: i === (currentIndex-1)}"-->
<!--            @click = jump(i+1)-->
<!--        >-->
<!--        </li>-->
<!--      </ul>-->
<!--    </div>-->
<!--    // 点击图片预览-->
<!--    <div class="mask-div" @click="maskFun()" v-if="maskBol">-->
<!--      <img :style="{width:imgWidth+'px'}" :src="sliders[imgNumber].img" alt="" class="mask-img">-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->
<!--<script>-->
<!--  export default {-->
<!--    name: 'dataCenter',-->
<!--    props: {-->
<!--      initialSpeed: {-->
<!--        type: Number,-->
<!--        default: 20-->
<!--      }, // 图片移动速度-->
<!--      initialInterval: {-->
<!--        type: Number,-->
<!--        default: 1-->
<!--      } // 如果是一个组件 接受外部传入的切换周期-->
<!--    },-->
<!--    data () {-->
<!--      return {-->
<!--        sliders: [-->
<!--          {-->
<!--            img: 'http://img.hb.aicdn.com/adbde61e4343dedd21e97ea7f22666825a8db7d077ffe-qn8Pjn_fw658'-->
<!--          },-->
<!--          {-->
<!--            img: 'http://img.hb.aicdn.com/adeed7d28df6e776c2fa6032579c697381d1a82b7fe00-fwRqgn_fw658'-->
<!--          },-->
<!--          {-->
<!--            img: 'http://img.hb.aicdn.com/ab7f48509b3c0353017d9a85ef1d12400c9b2724540d4-p3zouo_fw658'-->
<!--          },-->
<!--          {-->
<!--            img: 'http://img.hb.aicdn.com/60f788fc2a846192f224b9e6d4904b30e54926211d3d67-ACFJ9G_fw658'-->
<!--          },-->
<!--          {-->
<!--            img: 'http://img.hb.aicdn.com/22ded455284aab361b8d2056e82f74a891a019704296a-PSraEB_fw658'-->
<!--          },-->
<!--          {-->
<!--            img: 'http://img.hb.aicdn.com/22ded455284aab361b8d2056e82f74a891a019704296a-PSraEB_fw658'-->
<!--          },-->
<!--          {-->
<!--            img: 'http://img.hb.aicdn.com/22ded455284aab361b8d2056e82f74a891a019704296a-PSraEB_fw658'-->
<!--          }-->
<!--        ], // 放图片的数组-->
<!--        imgWidth: 600, // 图片宽度-->
<!--        currentIndex: 1, // 原点起始位置-->
<!--        distance: -600, // 外层嵌套的初始移动距离-->
<!--        transitionEnd: true, // 防止多次快速点击切换出现问题的闸门-->
<!--        speed: this.initialSpeed,-->
<!--        timer: null, // 定时器-->
<!--        imgNumber: 0, // 点击放大的图片-->
<!--        maskBol: false-->
<!--      }-->
<!--    },-->
<!--    computed: {-->
<!--      containerStyle () {-->
<!--        return {-->
<!--          transform: `translate3d(${this.distance}px, 0, 0)`-->
<!--        }-->
<!--      },-->
<!--      interval () {-->
<!--        return this.initialInterval * 1000-->
<!--      }-->
<!--    },-->
<!--    created () {-->
<!--      this.init()-->
<!--    },-->
<!--    methods: {-->
<!--      init () {-->
<!--        this.play()-->
<!--      },-->
<!--      move (offset, direction, speed) { // 移动一次的距离， 向左还是向右移动， 图片移动速度-->
<!--        if (!this.transitionEnd) return-->
<!--        this.transitionEnd = false-->
<!--        direction === -1 ? this.currentIndex += offset / this.imgWidth : this.currentIndex -= offset / this.imgWidth-->
<!--        if (this.currentIndex > this.sliders.length) this.currentIndex = 1-->
<!--        if (this.currentIndex < 1) this.currentIndex = this.sliders.length-->

<!--        const destination = this.distance + offset * direction-->
<!--        this.animate(destination, direction, speed)-->
<!--      },-->
<!--      animate (des, direc, speed) { // 实际移动距离 想左还是向右 移动速度 负右正左-->
<!--        if (this.temp) {-->
<!--          window.clearInterval(this.temp)-->
<!--          this.temp = null-->
<!--        }-->
<!--        this.temp = window.setInterval(() => {-->
<!--          if ((direc === -1 && des < this.distance) || (direc === 1 && des > this.distance)) {-->
<!--            this.distance += speed * direc-->
<!--          } else {-->
<!--            this.transitionEnd = true-->
<!--            window.clearInterval(this.temp)-->
<!--            this.distance = des-->
<!--            let allWidth = this.sliders.length * this.imgWidth-->
<!--            if (des < -allWidth) this.distance = -this.imgWidth-->
<!--            if (des > -this.imgWidth) this.distance = -allWidth-->
<!--          }-->
<!--        }, 10)-->
<!--      },-->
<!--      jump (index) {-->
<!--        const direction = index - this.currentIndex >= 0 ? -1 : 1-->
<!--        const offset = Math.abs(index - this.currentIndex) * this.imgWidth-->
<!--        const jumpSpeed = Math.abs(index - this.currentIndex) === 0 ? this.speed : Math.abs(index - this.currentIndex) * this.speed-->
<!--        this.move(offset, direction, jumpSpeed)-->
<!--      },-->
<!--      // 自动播放函数-->
<!--      play () {-->
<!--        if (!this.maskBol) {-->
<!--          if (this.timer) {-->
<!--            window.clearInterval(this.timer)-->
<!--            this.timer = null-->
<!--          }-->
<!--          this.timer = window.setInterval(() => {-->
<!--            this.move(this.imgWidth, -1, this.speed)-->
<!--          }, this.interval)-->
<!--        }-->
<!--      },-->
<!--      stop () {-->
<!--        window.clearInterval(this.timer)-->
<!--        this.timer = null-->
<!--      },-->
<!--      amplification (index) {-->
<!--        this.imgNumber = index-->
<!--        this.maskBol = true-->
<!--        this.stop()-->
<!--      },-->
<!--      maskFun () {-->
<!--        this.maskBol = false-->
<!--        this.play()-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--</script>-->
<!--<style lang="scss">-->
<!--  *{-->
<!--    box-sizing: border-box;-->
<!--    margin:0;-->
<!--    padding:0;-->
<!--  }-->
<!--  ol,ul{-->
<!--    list-style: none;-->
<!--  }-->
<!--  #dataCenter{-->
<!--    text-align: center;-->
<!--    .window{-->
<!--      position:relative;-->
<!--      width:600px;-->
<!--      height:400px;-->
<!--      margin:0 auto;-->
<!--      overflow:hidden;-->
<!--      .container{-->
<!--        display:flex;-->
<!--        position:absolute;-->
<!--      }-->
<!--      .left, .right{-->
<!--        position:absolute;-->
<!--        top:50%;-->
<!--        transform:translateY(-50%);-->
<!--        width:50px;-->
<!--        height:50px;-->
<!--        background-color:rgba(0,0,0,.3);-->
<!--        border-radius:50%;-->
<!--        cursor:pointer;-->
<!--      }-->
<!--      .left{-->
<!--        left:3%;-->
<!--        padding-left:12px;-->
<!--        padding-top:10px;-->
<!--      }-->
<!--      .right{-->
<!--        right:3%;-->
<!--        padding-right:12px;-->
<!--        padding-top:10px;-->
<!--      }-->
<!--      img{-->
<!--        user-select: none;-->
<!--      }-->
<!--    }-->
<!--    .dots{-->
<!--      position:absolute;-->
<!--      bottom:10px;-->
<!--      left:50%;-->
<!--      transform:translateX(-50%);-->
<!--    }-->
<!--    .dots li{-->
<!--      display:inline-block;-->
<!--      width:15px;-->
<!--      height:15px;-->
<!--      margin:0 3px;-->
<!--      border:1px solid white;-->
<!--      border-radius:50%;-->
<!--      background-color:#333;-->
<!--      cursor:pointer;-->
<!--    }-->
<!--    .dots .dotted{-->
<!--      background-color:orange;-->
<!--    }-->
<!--    .mask-div{-->
<!--      width: 100vw;-->
<!--      height: 100vh;-->
<!--      background-color: rgba(0,0,0,.7);-->
<!--      position: fixed;-->
<!--      top: 0;-->
<!--      left: 0;-->
<!--      .mask-img{-->
<!--        margin-top: calc(50vh - 200px);-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--</style>-->


