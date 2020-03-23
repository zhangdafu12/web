<template>
  <div id="app">
    <div class="head">
      <div class="head_cont">
        <div class="title">
          <span>EPRC</span>
          <span>全球公链实时分析</span>
        </div>
        <div class="headTab">
          <p
            v-for="(item,index) in tabList"
            :key="index"
            :class="{'active':indexNum==index}"
            @click="onTab(index)"
          >{{item}}</p>
          <img :src="userImg" alt />
        </div>
      </div>
    </div>

    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      tabList: ["排行榜", "查询", "我的"]
    };
  },
  created() {
    //在页面加载时读取sessionStorage里的状态信息
    if (sessionStorage.getItem("store")) {
      this.$store.replaceState(
        Object.assign(
          {},
          this.$store.state,
          JSON.parse(sessionStorage.getItem("store"))
        )
      );
      sessionStorage.removeItem("store");
    }
    //在页面刷新时将vuex里的信息保存到sessionStorage里
    window.addEventListener("beforeunload", () => {
      sessionStorage.setItem("store", JSON.stringify(this.$store.state));
    });
    let that = this;
  },
  computed: {
    indexNum() {
      return this.$store.state.indexNum;
    },
    userImg: {
      get: function() {
        if(this.$store.state.userInfo.icon){
              return this.$store.state.userInfo.icon
        }else{
          return require('../static/images/icon_login.png')
        }
        
      },
      set: function() {}
    },
  },
  updated(){
    console.log(this.$store.state.userInfo.icon)
  },
  methods: {
    onTab(index) {
      let that = this;
      let indexNum = that.$store.state.indexNum;
      if (index != indexNum) {
        that.$store.commit("changeMineTab", 0);
        that.$store.commit("changeIndexTab", "公链交易量top10");
        that.$store.commit("changeActiveIndex", 1);
        that.$store.commit("queryIndex", 0);
        that.$store.commit("changeQueryTitle", '单一账户查询');
        console.log(that.$store.state.queryTitle)
      }
      that.$store.commit("changeIndexNum", index);
      let list = ["", "query", "mine"];
      that.$router.push({ path: `/${list[index]}` });
    }
  }
};
</script>

<style lang="less">
body {
  margin: 0;
  padding: 0;
  background: url("../static/images/backimg.png");
}
#app {
  .head {
    border-bottom: solid 1px #1f3e5a;
    .head_cont {
      width: 1360px;
      height: 70px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;

      .title {
        font-size: 26px;
        color: #00ce7d;
        font-family: KaiTi;
      }
      .headTab {
        display: flex;
        justify-content: flex-end;
        align-items: center;

        p {
          text-align: center;
          font-size: 14px;
          color: #586c86;
          margin-right: 50px;
        }
        .active {
          color: #ffffff;
        }
        img {
          width: 40px;
          height: 40px;
          border-radius: 50%;
        }
      }
    }
  }
}
</style>
