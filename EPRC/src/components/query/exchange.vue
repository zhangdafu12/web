<template>
  <div class="exchange">
    <div class="pull_cont">
      <el-dropdown trigger="click" placement="bottom-start">
        <span :class="spanColor[0]==1?'el-dropdown-link spanColor':'el-dropdown-link'">
          {{name}}
          <i class="el-icon-caret-bottom el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown" class="onDropdown">
          <el-dropdown-item
            @click.native="onName(index)"
            v-for="(item,index) in nameList"
            :key="index"
          >{{item}}</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <!-- <el-dropdown trigger="click" placement="bottom-start">
        <span :class="spanColor[1]==1?'el-dropdown-link spanColor':'el-dropdown-link'">
          {{coin}}
          <i class="el-icon-caret-bottom el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown" class="onDropdown">
          <el-dropdown-item
            @click.native="onCoin(index)"
            v-for="(item,index) in coinList"
            :key="index"
          >{{item}}</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>-->
      <el-dropdown trigger="click" placement="bottom-start" ref="time">
        <span :class="spanColor[2]==1?'el-dropdown-link spanColor':'el-dropdown-link'">
          {{time}}
          <i class="el-icon-caret-bottom el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown" class="time">
          <div class="left">
            <p @click="onTime(0)" :class="isTime==0?'green':''">开始时间</p>
            <p @click="onTime(1)" :class="isTime==1?'green':''">结束时间</p>
          </div>
          <div class="right">
            <div v-if="isTime==0">
              <el-date-picker
                v-model="startTime"
                type="date"
                placeholder="开始时间"
                @change="TimeChange"
                value-format="yyyy-MM-dd"
              ></el-date-picker>
              <button @click="TimeInterval('startTime')">确定</button>
            </div>
            <div v-if="isTime==1">
              <el-date-picker
                v-model="endTime"
                type="date"
                placeholder="结束时间"
                @change="TimeChange"
                value-format="yyyy-MM-dd"
              ></el-date-picker>
              <button @click="TimeInterval('endTime')">确定</button>
            </div>
          </div>
        </el-dropdown-menu>
      </el-dropdown>
    </div>

    <div class="table">
      <ul class="tabs">
        <li class="one">#</li>
        <li class="two">名称</li>
        <li class="three">出入金额</li>
        <li class="four">总持有</li>
        <li class="five">时间</li>
      </ul>
      <div v-for="(item,index) in tabList" :key="index" style="position: relative;">
        <ul class="tabs_cont" :class="{'bg-g':index % 2 == 0}">
          <li class="one">{{index+1}}</li>
          <li class="two">
            <img v-if="item.cion" :src="item.coin" alt />
            <span @click="showAll(index)">
              {{item.exchange_name}}
              <i class="el-icon-caret-bottom"></i>
              <div class="showAll" v-show="item.showAll">
                <span v-for="(item,index) in HuobiList" :key="index">{{item}}</span>
              </div>
            </span>
          </li>
          <li class="three">{{item.access}}</li>
          <li class="four yellow">{{item.possession}}</li>
          <li class="five">{{item.time}}</li>
        </ul>
        <div class="boxes" v-show="item.isBoxes">
          <div @click="onBox('favorite',index)">
            <img src="../../../static/images/favorite(1).png" alt class="green" />
            <img src="../../../static/images/favorite(2).png" alt class="gray" />
            <span>收藏</span>
          </div>
          <div @click="onBox('trace',index)">
            <img src="../../../static/images/trace(1).png" alt class="green" />
            <img src="../../../static/images/trace(2).png" alt class="gray" />
            <span>追踪</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { chain } from "../../api/api";
import { Message, Loading } from "element-ui";
export default {
  data() {
    return {
      name: "eth",
      coin: "币种",
      time: " 时间",
      spanColor: [0, 0, 0],
      nameList: ["eth", "bch", "btc"],
      coinList: ["火币", "土币", "以太币", "ONT本体", "NEO小蚁"],
      isTime: 0,
      startTime: "", //时间开始
      endTime: "", //时间结束
      HuobiList: [
        // "Huobi账户",
        // "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        // "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        // "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        // "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        // "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        // "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        // "0xc97a4ed29f03fd549c4ae79086673523122d2bc5"
      ],
      // ******************************************************
      tabList: [
        // {
        //   coin: "../../../static/images/coin.png",
        //   exchange_name: "Bitcoin",
        //   access: "921.79",
        //   possession: "921.79",
        //   time: "14:50  18/04/17",
        //   isBoxes: false,
        //   showAll: false
        // }
      ]
    };
  },
  mounted() {
    this.getRank();
  },
  methods: {
    showAll(i) {
      let that = this;

      // that.tabList[i].showAll = !that.tabList[i].showAll;


      that.tabList.forEach((item,index)=>{
        if(index==i){
          item.showAll=!item.showAll
        }else{
        item.showAll=false
        }
      })


      chain.exchange_name({
        params:{
          chain_name:that.name,
          exchange_name:that.tabList[i].exchange_name
        }
      }).then(res=>{
console.log(res.data)
that.HuobiList=res.data
      })
    },
    getRank() {
      let that = this;
      chain
        .chain_exchange({
          params: {
            chain_name: that.name,
            start_time: that.startTime,
            end_time: that.endTime
          }
        })
        .then(res => {
          console.log(res.data);
          res.data.forEach(item => {
            item.showAll = false;
          });

          that.tabList = res.data;
        });
    },

    //名称下拉框
    onName(index) {
      this.name = this.nameList[index];
      this.spanColor[0] = 1;
      this.getRank();
    },
    // //币种下拉框
    // onCoin(index) {
    //   this.name = this.coinList[index];
    //   this.spanColor[1] = 1;
    // },
    //时间下拉框
    TimeInterval(index) {
      if (this.endTime == "") {
        console.log("请输入结束时间");
         Message({
          message: "请输入结束时间",
          duration: 1000,
          type: "warning"
        });
      } else if (this.startTime == "") {
        console.log("请输入开始时间");
         Message({
          message: "请输入开始时间",
          duration: 1000,
          type: "warning"
        });
      } else {
        this.time = this.startTime + "~" + this.endTime;
        this.$refs.time.hide();
        this.spanColor[2] = 1;
        this.getRank();
      }
      console.log(this.startTime, this.endTime);
    },
    TimeChange() {
      this.$refs.time.show();
      console.log(this.startTime, this.endTime);
      // that.$refs.time.hide();
    },
    onTime(i) {
      this.isTime = i;
    },
    onOmit(index) {
      this.tabList[index].isBoxes = !this.tabList[index].isBoxes;
    }
    // //收藏 追踪
    // onBox(i, index) {
    //   console.log(i);
    //   //favorite 收藏
    //   //trace 追踪
    //   this.tabList[index].isBoxes = false;
    // }
  }
};
</script>


<style lang="less">
ul,
li {
  margin: 0;
  padding: 0;
  list-style: none;
}
.onDropdown {
  width: 338px;
}
.time {
  width: 414px;
  height: 200px;
  font-size: 14px;
  background-color: #0f152c;
  color: #a1a5c5;
  display: flex;
  justify-content: flex-start;
  .left {
    width: 126px;
    height: 200px;
    box-sizing: border-box;
    box-shadow: 0px 3px 6px 0px rgba(0, 0, 0, 0.16);
    p {
      padding: 18px 0;
      text-align: center;
    }
    .green {
      color: #00ce7d;
    }
  }
  .right {
    width: 288px;
    box-shadow: 0px 3px 6px 0px rgba(0, 0, 0, 0.16);
    padding: 22px 0 0 22px;
    box-sizing: border-box;
    input {
      border: none;
      background-color: #1b2d49;
    }
    button {
      width: 124px;
      height: 34px;
      background-color: #ff8a24;
      border-radius: 5px;
      border: none;
      font-size: 14px;
      color: #ffffff;
      margin: 40px 48px;
    }
  }
}
.exchange {
  width: 1228px;
  min-height: 688px;
  margin-top: 20px;
  background-color: #1e344d;
  opacity: 0.8;
  .pull_cont {
    height: 40px;
    margin: 0 10px 0 20px;
    box-sizing: border-box;
    padding-right: 15px;
    border-bottom: solid 1px #1f3e5a;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    .el-dropdown {
      margin-right: 100px;
      font-size: 14px;
      color: #42b6f6;
      span {
        display: flex;
        align-items: center;
      }
      .spanColor {
        color: #00ce7d;
      }
    }
    .iscolor {
      color: #00ce7d;
    }
  }
  .table {
    padding: 0 10px;
    box-sizing: border-box;
    .tabs {
      height: 48px;
      line-height: 48px;
      width: 100%;
      padding: 0 15px 0 10px;
      box-sizing: border-box;
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      color: #586c86;
      .one {
        width: 10%;
      }
      .two {
        width: 30%;
      }
      .three {
        width: 25%;
      }
      .four {
        width: 25%;
      }
      .five {
        width: 10%;
        white-space: nowrap;
      }
    }
    .tabs_cont {
      height: 48px;
      line-height: 48px;
      width: 100%;
      padding: 0 15px 0 10px;
      box-sizing: border-box;
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      color: #42b6f6;
      .one {
        width: 10%;
      }
      .showAll::-webkit-scrollbar {
        width: 4px;
        background-color: #1b2e47;
      }
      .showAll {
        width: 380px;
        height: 350px;
        position: absolute;
        top: 30px;
        left: 130px;
        background-color: #0f152c;
        box-shadow: 0px 3px 6px 0px rgba(0, 0, 0, 0.16);
        border-radius: 5px;
        overflow-y: scroll;
        overflow-x: hidden;
        span {
          width: 100%;
          height: 58px;
          display: inline-block;
          border-bottom: solid 1px #1f3e59;
          line-height: 58px;
          text-indent: 20px;
        }
      }
      .two {
        width: 30%;
        display: flex;
        align-items: center;
        position: relative;
        span {
          z-index: 10;
        }
        img {
          width: 16px;
          height: 16px;
          margin-right: 5px;
        }
      }
      .three {
        width: 25%;
        color: #06d514;
      }
      .four {
        width: 25%;
        color: #ff8921;
      }
      .five {
        width: 10%;
          white-space: nowrap;
      }
    }
    .bg-g {
      background-color: rgba(24, 43, 65, 0.32);
    }
    .boxes {
      width: 100px;
      height: 112px;
      background-color: #0f152c;
      box-shadow: 0px 0px 6px 0px rgba(0, 0, 0, 0.16);
      border-radius: 5px;
      position: absolute;
      right: 15px;
      top: 40px;
      z-index: 200;
      div {
        height: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        color: #a1a5c5;
        img {
          width: 20px;
          height: 20px;
          margin-right: 5px;
        }
        .green {
          display: none;
        }
      }
      div:first-child {
        border-bottom: solid 1px #162843;
      }
      div:hover {
        color: #00ce7d;
      }
      div:hover > .green {
        display: block;
      }
      div:hover > .gray {
        display: none;
      }
    }
  }
}
</style>
