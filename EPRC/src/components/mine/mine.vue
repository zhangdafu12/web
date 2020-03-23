<template>
  <div class="mine">
    <div class="navtabs">个人中心</div>
    <div class="mine_cont">
      <div class="mineTabs">
        <div class="info">
          <img :src="headimg" alt />
          <span>{{name}}</span>
        </div>
        <div class="tabs_cont">
          <div :class="num==0?'tabs active':'tabs'" @click="ontabs(0)">
            <img
              :src="num==0?'../static/images/favorite(1).png':'../static/images/favorite.png'"
              alt
            />
            <span>我的收藏</span>
          </div>
          <div :class="num==1?'tabs active':'tabs'" @click="ontabs(1)">
            <img :src="num==1?'../static/images/trace(1).png':'../static/images/trace.png'" alt />
            <span>我的追踪</span>
          </div>
          <div :class="num==2?'tabs active':'tabs'" @click="ontabs(2)">
            <img :src="num==2?'../static/images/record(1).png':'../static/images/record.png'" alt />
            <span>浏览记录</span>
          </div>
          <div :class="num==3?'tabs active':'tabs'" @click="ontabs(3)">
            <img :src="num==3?'../static/images/amend(1).png':'../static/images/amend.png'" alt />
            <span>信息修改</span>
          </div>
        </div>
        <p class="outLogin" @click="outLogin">退出登录</p>
      </div>
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // headimg: "../static/images/headimg.jpg",
      // name: "仰望星空",
    };
  },
  mounted() {
    let that = this;
    let url = this.$route.path;
     this.$store.commit('changeIndexNum',2)
    if (url == "/favorite") {
      that.$store.commit("changeMineTab", 0);
    } else if (url == "/trace") {
      that.$store.commit("changeMineTab", 1);
    } else if (url == "/record") {
      that.$store.commit("changeMineTab", 2);
    } else if (url == "/amend") {
      that.$store.commit("changeMineTab", 3);
    }
  },
  updated() {
    let that = this;
    let url = this.$route.path;
    if (url == "/favorite") {
      that.$store.commit("changeMineTab", 0);
    } else if (url == "/trace") {
      that.$store.commit("changeMineTab", 1);
    } else if (url == "/record") {
      that.$store.commit("changeMineTab", 2);
    } else if (url == "/amend") {
      that.$store.commit("changeMineTab", 3);
    }
    console.log(this.$store.state.userInfo.icon)
  },
  computed: {
    num: {
      get: function() {
        return this.$store.state.mineTab;
      },
      set: function() {}
    },

    name: {
      get: function() {
        if (this.$store.state.userInfo.username) {
          return this.$store.state.userInfo.username;
        } else {
          return this.$store.state.userInfo.tel;
        }
      },
      set: function() {}
    },

    headimg: {
      get: function() {
        return this.$store.state.userInfo.icon;
      },
      set: function() {}
    }
  },
  methods: {
    ontabs(index) {
      this.num = index;
      this.$store.commit("changeMineTab", index);
      let list = ["favorite", "trace", "record", "amend"];
      this.$router.push({ path: `/${list[index]}` });
    },
    outLogin() {
      localStorage.clear();
      this.$store.commit("changeLoginState", false);
      this.$router.push({ path: `/login` });
    }
  }
};
</script>

<style lang="less">
p {
  margin: 0;
  padding: 0;
}
.mine {
  width: 1228px;
  margin: 0 auto;
  .navtabs {
    width: 100%;
    height: 54px;
    line-height: 54px;
    background-color: #1c324a;
    opacity: 0.8;
    margin: 24px 0 20px 0;
    padding: 0 10px;
    box-sizing: border-box;
    font-size: 18px;
    color: #ffffff;
  }
  .mine_cont {
    display: flex;
    justify-content: space-between;
    .mineTabs {
      width: 185px;
      height: 688px;
      background-color: #1e344d;
      opacity: 0.8;
      .outLogin {
        color: #42b6f6;
        font-size: 14px;
        text-align: center;
        margin-top: 50px;
        cursor: pointer;
      }
      .info {
        width: 80px;
        margin: 0 auto;
        text-align: center;
        margin-bottom: 50px;
        img {
          width: 80px;
          height: 80px;
          border-radius: 50%;
          margin: 38px 0 10px 0;
        }
        span {
          font-size: 16px;
          color: #ffffff;
        }
      }
      .tabs_cont {
        font-size: 14px;

        .tabs {
          width: 100%;
          height: 58px;
          display: flex;
          justify-content: center;
          align-items: center;
          color: #42b6f6;
          border-left: 2px solid #1e344d;
          box-sizing: border-box;
          img {
            width: 20px;
            height: 20px;
            margin-right: 10px;
          }
        }
        .active {
          background-color: #1d3150;
          border-left: 2px solid #00ce7d;
          box-sizing: border-box;
          color: #00ce7d;
        }
      }
    }
  }
}
</style>
