<template>
  <div id="home">
    <div class="H_top">
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#0f152c"
        text-color="#a1a5c5"
        active-text-color="#00ce7d"
        :router="true"
      >
        <el-submenu index="1">
          <template slot="title">{{title}}</template>
          <el-menu-item index="/">公链交易量top10</el-menu-item>
          <el-submenu index="2">
            <template slot="title">交易所交易量top10</template>
            <el-menu-item index="/topTwo?id=btc">BTC</el-menu-item>
            <el-menu-item index="/topTwo?id=eth">ETH</el-menu-item>
            <el-menu-item index="/topTwo?id=bch">BCH</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">全网大额转账top10</template>
            <el-menu-item index="/topThree?id=btc">BTC</el-menu-item>
            <el-menu-item index="/topThree?id=eth">ETH</el-menu-item>
            <el-menu-item index="/topThree?id=bch">BCH</el-menu-item>
          </el-submenu>
          <el-menu-item index="/topFour">公链红榜top10</el-menu-item>
          <el-menu-item index="/topFive">公链黑榜top10</el-menu-item>
        </el-submenu>
      </el-menu>
<el-select v-if="clickI=='3'" v-model="select" :placeholder="select">
    <el-option
      v-for="item in timeList"
      @change='changeTime'
      :key="item"
      :label="item"
      :value="item">
    </el-option>
  </el-select>
      <div class="H_nav">
        <vue-seamless-scroll
          :data="listData"
          :class-option="optionSing"
          class="seamless-warp"
          id="seamless-warp"
        >
          <ul>
            <li
              ref="nav_tab"
              :data-i="i"
              class="nav_tab"
              :class="{'active':i==indexTab}"
              v-for="(item,i) in listData"
              :key="i"
            >
              <div class="nav_top">top{{i+1}}</div>
              <div v-if="clickI== '2'">
                <span class="nav_name">{{item.exchange_name}}</span>
              </div>
              <div v-else-if="clickI=='4'||clickI== '5'">
                <span class="nav_name">{{item.chain}}</span>
              </div>
              <div class="user_three" v-else-if="clickI== '3'">
                <span class="nav_name user_d">{{item.hash}}</span>
                <span class="type_tip">{{item.exchange_name}}</span>
              </div>
              <div v-else>
                <span class="nav_name">{{item.chain}}</span>
                <img class="nav_img" v-if="item.change>=0" src="/static/images/icon_up.png" alt />
                <img class="nav_img" v-else src="/static/images/icon_down.png" alt />
              </div>
              <div class="nav_other spaceAround" v-if="clickI=='2'">
                <span>交易所总持有量</span>
                <span>交易所总持有量</span>
              </div>
              <div class="nav_other spaceAround" v-if="clickI=='4'||clickI=='5'">
                <span>活跃度(24h)</span>
                <span>交易量</span>
              </div>
              <div v-if="clickI=='2'" class="spaceAround">
                <span class="nav_n_up">{{item.total_amount}}</span>
                <span class="nav_n_down">{{item.inner_amount}}</span>
              </div>
              <div v-else-if="clickI=='3'">
                <span class="nav_num">金额</span>
                <span class="nav_n_up">￥{{item.price}}</span>
              </div>
              <!-- 红榜heibang -->
              <div class="spaceAround" v-else-if="clickI=='4'||clickI=='5'">
                <div>
                  <span
                    class="nav_n_up"
                    v-if="item.activity>=0"
                  >{{item.previous_24h_activity}} ({{item.activity}})</span>
                  <span class="nav_n_down" v-else>{{item.previous_24h_activity}}</span>
                  <img class="nav_img" v-if="item.activity>0" src="/static/images/icon_up.png" alt />
                  <img
                    class="nav_img"
                    v-if="item.activity<0"
                    src="/static/images/icon_down.png"
                    alt
                  />
                </div>
                <span class="nav_n_up">{{item.total_amount}}</span>
              </div>
              <div v-else class="spaceAround">
                <span class="nav_num">{{item.total_ts}}</span>
                <span class="nav_n_up" v-if="item.change>=0">{{item.change}}</span>
                <span class="nav_n_down" v-else>{{item.change}}</span>
              </div>
            </li>
          </ul>
        </vue-seamless-scroll>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
import { chain } from "../../api/api";
export default {
  name: "home",
  data() {
    return {
      typeChain: "eth",
      clickI: "1",
      indexTab: 0,
      select:'12h',
      timeList:["1h", "6h", "12h", "24h", "3d", "week", "month", "year"],
      listData: [
        // {
        //   chain: "Fatbtc",
        //   change: "-399",
        //   total_ts: "6,553,39",
        //   time: "2020-03-07 19:53:40"
        // }
      ],
      // listData2: [
      //   {
      //     name: "Fatbtc",
      //     number: "6,553,39",
      //     downNum: "-2,73 (5,51%)"
      //   }
      // ],
      // listData3: [
      //   {
      //     name: "Fatbtc",
      //     number: "金额",
      //     upNum: "444444"
      //   }
      // ],
      // listData4: [
      //   {
      //     chain: "Fatbtc",
      //     activity: 5,
      //     total_amount: "6,553,39",
      //     previous_24h_activity: "+3,90 (0,25%)"
      //   }
      // ],
      // listData5: [
      //   {
      //     chain: "Fatbtc",
      //     activity: 5,
      //     total_amount: "6,553,39",
      //     previous_24h_activity: "+3,90 (0,25%)",
      //     fake_amount: "8136"
      //   }
      // ]
    };
  },
  computed: {
    optionSing() {
      return {
        step: 0.7, // 数值越大速度滚动越快
        limitMoveNum: 3, // 开始无缝滚动的数据量 this.dataList.length
        hoverStop: true, // 是否开启鼠标悬停stop
        direction: 2, // 0向下 1向上 2向左 3向右
        openWatch: true, // 开启数据实时监控刷新dom
        singleHeight: 0, // 单步运动停止的高度(默认值0是无缝不停止的滚动) direction => 0/1
        singleWidth: 204, // 单步运动停止的宽度(默认值0是无缝不停止的滚动) direction => 2/3
        waitTime: 100 // 单步运动停止的时间(默认值1000ms)
      };
    },

    activeIndex() {
      return this.$store.state.activeIndex;
    },
    title() {
      return this.$store.state.indexTab;
    }
  },

  created() {
    let that = this;
    let url = this.$route.path;
    let activeI = this.$store.state.activeIndex;
    let val = that.$store.state.activeIndexVal;
    console.log(url);
    if (url == "/") {
      that.getTradRank();
      that.clickI = 1;
      that.$store.commit("changeIndexTab", "公链交易量top10");
    } else if (url == "/topTwo") {
      that.getExchangeRank(val);
      that.$store.commit("changeIndexTab", "交易所交易量top10");
      that.clickI = 2;
    } else if (url == "/topThree") {
      that.clickI = 3;
      that.$store.commit("changeIndexTab", "全网大额转账top10");
      that.getlargetsRank({ chain_name: val });
    } else if (url == "/topFour") {
      that.clickI = 4;
      that.$store.commit("changeIndexTab", "公链红榜top10");
      that.getRedRank();
    } else if (url == "/topFive") {
      that.clickI = 5;
      that.$store.commit("changeIndexTab", "公链黑榜top10");
      that.getBlackRank();
    }
  },
  mounted() {
    this.$store.commit('changeIndexNum',0)
    this.navTabChange();
  },

  methods: {
    //时间选择
    changeTime(){
    },
    // tab选卡
    handleSelect(key, keyPath, e) {
      let that = this;
      that.indexTab = 0;

      this.$store.commit("changeActiveIndex", keyPath[1]);

      console.log(key, keyPath, e);
      if (keyPath[1] == "/") {
        that.clickI = 1;
        that.$store.commit("changeIndexTab", "公链交易量top10");
        that.$store.commit("changeActiveIndexVal", "");
        that.getTradRank();
      } else if (keyPath[1] == "2") {
        that.clickI = 2;
        let ind = keyPath[2].split("=");
        console.log(ind[1]);
        that.typeChain = ind[1];
        that.$store.commit("changeActiveIndexVal", ind[1]);
        that.getExchangeRank(ind[1]);
        that.$store.commit("changeIndexTab", "交易所交易量top10");
      } else if (keyPath[1] == "3") {
        that.clickI = 3;
        let ind = keyPath[2].split("=");
        console.log(ind[1]);
        that.typeChain = ind[1];
        that.$store.commit("changeActiveIndexVal", ind[1]);
        that.getlargetsRank({ chain_name: ind[1] });
        that.$store.commit("changeIndexTab", "全网大额转账top10");
      } else if (keyPath[1] == "/topFour") {
        that.clickI = 4;
        that.$store.commit("changeIndexTab", "公链红榜top10");
        that.$store.commit("changeActiveIndexVal", "");
        that.getRedRank();
      } else if (keyPath[1] == "/topFive") {
        that.clickI = 5;
        that.$store.commit("changeActiveIndexVal", "");

        that.$store.commit("changeIndexTab", "公链黑榜top10");
        that.getBlackRank();
      }
      console.log(this.title);
    },
    //交易量top10
    getTradRank() {
      let that = this;
      chain.getheardform().then(res => {
        that.listData = res.headerform;
      });
    },

    //交易所交易量top10
    getExchangeRank(link) {
      let that = this;
      chain
        .getexchangetop10Get({
          params: {
            chain_name: link
          }
        })
        .then(res => {
          console.log(res.exchange, 2);
          that.listData = res.exchange;
        });
    },
    //大额转账top10
    getlargetsRank({ chain_name = "btc", time_range = "12h" }) {
      let that = this;
      chain
        .getlargetstop10Get({
          params: {
            chain_name: chain_name,
            time_range: time_range
          }
        })
        .then(res => {
          let data = [];
          for (let i in res) {
            data.push(res[i].transactions_info[0]);
          }
          console.log(data, "-0---------------------------");
          that.listData = data;
          console.log(that.listData);
        })
        .catch(err => {
          console.log(err);
        });
    },
    // 红榜
    getRedRank() {
      let that = this;
      chain.getactiveredrank().then(res => {
        that.listData = res;
      });
    },

    //黑帮
    getBlackRank() {
      let that = this;
      chain.getactiveblackrank().then(res => {
        that.listData = res;
      });
    },

    navTabChange() {
      let that = this;
      let div = document.getElementById("seamless-warp");
      console.log(div);
      div.addEventListener("click", function(e) {
        let _this = e.target;
        let data = _this.getAttribute("data-i");
        let other = _this.parentNode.parentNode.parentNode.childNodes;
        let dom = e.target.tagName.toLowerCase();
        let listOther = Array.from(other);
        if (dom === "li") {
          listOther.splice(1, 1);
          let allList = Array.from(listOther[0].childNodes[0].childNodes);
          allList = allList.concat(
            Array.from(listOther[1].childNodes[0].childNodes)
          );
          allList.forEach(item => {
            let index = item.getAttribute("data-i");
            if (data == index) {
              item.classList.add("active");
            } else {
              item.classList.remove("active");
            }
          });
          that.indexTab = data;
        }
      });
    }
  }
};
</script>


<style lang="less">
.el-select-dropdown{
  background-color: #0c1123;
   border: 0;
  }
  .el-input__inner{
    background-color:#1c324a;
    border: 0;
    color:#ffffff
  }
  .el-select-dropdown__item.hover, .el-select-dropdown__item:hover{
    background-color:#213b58;
  }
  .el-select{
    position: absolute;
    top: 94px;
    left: 255px;
    width: 100px;
  }
#home {
  width: 1228px;
  height: 100%;
  margin: 0 auto;
  font-size: 14px;
  

  
  .H_top {
    width: 100%;
    height: 170px;
    margin: 22px 0;
    background: #1c324a;
    overflow: hidden;
    .H_nav::-webkit-scrollbar {
      display: none;
    }
    .H_nav {
      width: 1218px;
      height: 90px;
      margin-left: 10px;
      overflow-y: hidden;
      overflow-x: initial;
      white-space: nowrap;
      background: #213b58;
      ul {
        margin: 0;
        padding: 0;
      }
      .nav_tab {
        width: 200px;
        height: 90px;
        display: inline-block;
        border-right: solid 1px #192d46;
        border-left: solid 1px #192d46;
        padding-left: 22px;
        padding-right: 12px;
        .type_tip {
          margin-right: 0px;
          height: 18px;
          line-height: 18px;
          background: #ff9f0e;
          display: inline-block;
          font-size: 8px;
          color: #ffffff;
          border-radius: 2px;
          padding: 2px;
        }
        div {
          margin-bottom: 4px;
        }
        .user_three {
          display: flex;
          align-items: center;
        }
        .spaceAround {
          display: flex;
          justify-content: space-around;
        }

        .nav_top {
          font-size: 12px;
          color: #cece00;
          text-align: end;
        }
        .nav_other {
          font-size: 12px;
          color: #586c86;
        }
        .nav_name {
          font-size: 16px;
          color: #ffffff;
          margin-right: 12px;
          // line-height: 40px;
        }
        .user_d {
          display: inline-block;
          width: 120px;
          overflow: hidden;
          white-space: nowrap;
        }
        .nav_img {
          width: 8px;
          height: 10px;
        }
        .nav_num {
          font-size: 14px;
          color: #586c86;
          margin-right: 6px;
        }
        .nav_n_up {
          font-size: 12px;
          color: #00ce7d;
          line-height: 20px;
          margin-right: 6px;
        }
        .nav_n_down {
          font-size: 12px;
          color: #e55541;
          line-height: 20px;
        }
      }
      .active {
        background: #1a2f46;
        border-bottom: solid 2px #42b6f6;
        box-sizing: border-box;
      }
    }
    .el-menu.el-menu--horizontal {
      border: 0;
      background: transparent !important;
    }
    .el-menu--horizontal > .el-submenu .el-submenu__title {
      height: 40px;
      line-height: 40px;
      border: 0;
      background-color: transparent !important;
      color: #ffffff !important;
    }
  }
  .H_content {
    width: 100%;
    height: 608px;
    display: flex;
    justify-content: space-between;
    .C_left {
      width: 732px;
      height: 608px;
      background-color: #1e344d;
      opacity: 0.8;
      padding-top: 20px;
      // margin-right: 20px;
      box-sizing: border-box;
      .C_tittle {
        width: 712px;
        height: 71px;
        background-color: #213b58;
        box-sizing: border-box;
        padding: 0 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        .ic_down {
          width: 22px;
          height: 22px;
        }
        .C_t_cont {
          display: flex;
          justify-content: flex-start;
          align-items: center;
          .C_logo {
            width: 32px;
            height: 32px;
            margin-right: 10px;
          }
          .C_C_cont {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            div {
              display: flex;
              align-items: center;
              .C_t_name {
                font-size: 20px;
                color: #ffffff;
                margin-right: 10px;
              }
              .C_t_rank {
                font-size: 12px;
                color: #cece00;
                margin-right: 10px;
              }
              .C_t_up {
                font-size: 12px;
                color: #00ce7d;
                margin-right: 10px;
              }
              .C_t_upI {
                width: 7px;
                height: 10px;
              }
              .C_t_pay {
                font-size: 14px;
                color: #bc821c;
                margin-right: 20px;
              }
              .C_t_time {
                font-size: 14px;
                color: #586c86;
              }
            }
          }
        }
      }
      .C_Chart {
        width: 100%;
        height: 500px;
        margin-top: 15px;
      }
    }
    .C_right {
      width: 471px;
      height: 608px;
      background-color: #1e344d;
      opacity: 0.7;
    }
  }
}
</style>
