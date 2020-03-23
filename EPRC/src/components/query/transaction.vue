<template>
  <div class="transaction">
    <div class="pull_cont">
      <div class="sinister">
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
        <el-dropdown trigger="click" placement="bottom-start" ref="sum">
          <span :class="spanColor[1]==1?'el-dropdown-link spanColor':'el-dropdown-link'">
            {{sum}}
            <i class="el-icon-caret-bottom el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown" class="sum">
            <div class="left">
              <p @click="onSum(0)" :class="isSum==0?'green':''">指定金额</p>
              <p @click="onSum(1)" :class="isSum==1?'green':''">区间金额</p>
            </div>
            <div class="right">
              <div v-if="isSum==0">
                <input type="text" placeholder="￥0.00" v-model="specified" />
                <button class="onebtn" @click="sunConfirm('specified')">确定</button>
              </div>
              <div v-if="isSum==1">
                <input type="text" placeholder="￥0.00" v-model="startInterval" />
                <span>~</span>
                <input type="text" placeholder="￥0.00" v-model="endInterval" />
                <button class="twobtn" @click="sunConfirm('interval')">确定</button>
              </div>
            </div>
          </el-dropdown-menu>
        </el-dropdown>
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
        <el-dropdown trigger="click" placement="bottom-start">
          <span :class="spanColor[3]==1?'el-dropdown-link spanColor':'el-dropdown-link'">
            {{rank}}
            <img :src="boult" v-if="isBoult" class="boult" />
            <i class="el-icon-caret-bottom el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown" class="sort">
            <el-dropdown-item
              @click.native="onRank(index)"
              v-for="(item,index) in rankList"
              :key="index"
            >
              {{item.txt}}
              <img :src="item.grayImgs" class="gray" />
              <img :src="item.greenImgs" class="green" />
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <!-- <div class="main">
        <div>
          <img src="../../../static/images/favorite.png" alt />
          <span>收藏</span>
        </div>
        <div>
          <img src="../../../static/images/trace.png" alt />
          <span>追踪</span>
        </div>
      </div> -->
    </div>
    <div class="table">
      <ul class="tabs">
        <li class="one">交易账户</li>
        <li class="two">金额</li>
        <li class="three">时间</li>
      </ul>
      <div v-for="(item,index) in tabList" :key="index" style="position: relative;">
        <ul class="tabs_cont bg-g" v-if="index % 2 == 0">
          <li class="one">{{item.hash}}</li>
          <li class="two">{{item.price}}</li>
          <li class="three">{{item.time}}</li>
          <li class="four">
            <img src="../../../static/images/omit.png" alt @click="onOmit(index)" />
          </li>
        </ul>
        <ul class="tabs_cont" v-else>
          <li class="one">{{item.account}}</li>
          <li class="two yellow">{{item.money}}</li>
          <li class="three">{{item.time}}</li>
          <li class="four">
            <img src="../../../static/images/omit.png" alt @click="onOmit(index)" />
          </li>
        </ul>
        <div class="boxes" v-if="item.isBoxes">
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
import { collectPost, trackPost } from "../../api/api";
export default {
  data() {
    return {
      name: "btc",
      sum: "金额",
      rank: "排序",
      time: " 时间",
      boult: "",
      isBoult: false,
      spanColor: [0, 0, 0, 0],
      nameList:["eth", "bch", "btc"],
      rankList: [
        {
          txt: "时间",
          grayImgs: "../../../static/images/gray(1).png",
          greenImgs: "../../../static/images/green(1).png"
        },
        {
          txt: "时间",
          grayImgs: "../../../static/images/gray.png",
          greenImgs: "../../../static/images/green.png"
        },
        {
          txt: "金额",
          grayImgs: "../../../static/images/gray(1).png",
          greenImgs: "../../../static/images/green(1).png"
        },
        {
          txt: "金额",
          grayImgs: "../../../static/images/gray.png",
          greenImgs: "../../../static/images/green.png"
        }
      ],
      isSum: 0,
      isTime: 0,
      specified: "", //指定金额
      startInterval: "", //区间金额 开始
      endInterval: "", //区间金额 结束
      startTime: "", //时间开始
      endTime: "", //时间结束
      // *****************************************************
      tabList: [
        // {
        //   hash: "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        //   price: "920.79",
        //   time: "14:50  18/04/16",
        //   isBoxes: false
        // }
      ]
    };
  },
  mounted(){
  let that = this;
let url = this.$route.path;
    let query = this.$route.query;
  if(JSON.stringify(query) !== '{}'){
    console.log(query);
    that.name = query.chain;
    that.specified = query.record.price;
    that.startInterval = query.record.start_price;
    that.endInterval = query.record.end_price;
    that.startTime = query.record.end_time;
    that.endTime = query.record.end_time;
  }
    




 this.getChangeInfo();
  },
  methods: {
    //名称下拉框
    onName(index) {
      this.name = this.nameList[index];
      this.spanColor[0] = 1;
      console.log(this.name);
      this.getChangeInfo();
    },

    getChangeInfo() {
      let that = this;
      if (that.specified == "") {
        chain.Query({
            params: {
              chain_name: that.name,
              start_money: that.startInterval,
              end_money: that.endInterval,
              start_time1: that.startTime,
              end_time1: that.endTime
            }
          })
          .then(res => {
            console.log(res.data);
res.data.forEach(item => {
  item.isBoxes=false
});


that.tabList=res.data
          });
      } else {
        chain.Query({
            params: {
              chain_name: that.name,
               Specified_amount: that.specified,
              start_time1: that.startTime,
              end_time1: that.endTime,
             
            }
          })
          .then(res => {
            console.log(res);
            res.data.forEach(item => {
              item.isBoxes=false
            });
            that.tabList=res.data
          });
      }
    },

    //金额下拉框
    sunConfirm(i) {
      let that = this;
      if (i == "specified") {
      
        that.spanColor[1] = 1;
         that.startInterval = "";
        that.endInterval = "";
        that.$refs.sum.hide();
        if (parseFloat(that.specified).toString() == "NaN") {
          Message({
            message: "金额为数字",
            duration: 1000,
            type: "warning"
          });
         
        } else {
            that.sum = that.specified;
           that.getChangeInfo();
        }

      } else {
      
        that.spanColor[1] = 1;
        that.$refs.sum.hide();
        that.specified = "";
        if (
          parseFloat(that.startInterval).toString() == "NaN" &&
          parseFloat(that.endInterval).toString() == "NaN"
        ) {
          Message({
            message: "金额为数字",
            duration: 1000,
            type: "warning"
          });
         
        } else {
            that.sum = that.startInterval + "~" + that.endInterval;
          that.getChangeInfo();
        }
        
      }
    },
    //时间下拉框
    TimeInterval(index) {
      let that = this;
      if (this.endTime == "") {
        Message({
          message: "请输入结束时间",
          duration: 1000,
          type: "warning"
        });
      } else if (this.startTime == "") {
        Message({
          message: "请输入开始时间",
          duration: 1000,
          type: "warning"
        });
      } else {
        this.time = this.startTime + "~" + this.endTime;
        this.$refs.time.hide();
        this.spanColor[2] = 1;
 that.getChangeInfo();
      }
      console.log(this.startTime, this.endTime);
    },
    TimeChange() {
      this.$refs.time.show();
      console.log(this.startTime, this.endTime);
    },

    //排序下拉框
    onRank(index) {
      let that = this;
      this.isBoult = true;
      this.rank = this.rankList[index].txt;
      this.boult = this.rankList[index].greenImgs;
      this.spanColor[3] = 1;
      console.log(index);
      if (index == 0) {
        that.tabList.sort((a, b) => {
          return a.time < b.time ? 1 : -1;
        });
      } else if (index == 1) {
        that.tabList.sort((a, b) => {
          return a.time > b.time ? 1 : -1;
        });
      } else if (index == 2) {
        that.tabList.sort((a, b) => {
          return a.price < b.price ? 1 : -1;
        });
      } else {
        that.tabList.sort((a, b) => {
          return a.price > b.price ? 1 : -1;
        });
      }

      console.log(that.tabList);
    },
    onSum(i) {
      this.isSum = i;
    },
    onTime(i) {
      this.isTime = i;
    },
    onOmit(index) {
      this.tabList[index].isBoxes = !this.tabList[index].isBoxes;
    },
    //收藏 追踪
   //收藏 追踪
    onBox(type, index) {
      console.log(type);
      let that = this;
      //favorite 收藏
      //trace 追踪collectPost, trackGet, selectr, trackPost
      let collect_info = {};
      let track_info = {};
       collect_info.chain= that.name;
      collect_info.id = that.tabList[index].id;
      collect_info.account1 = that.tabList[index].account1;
      collect_info.account2 = that.tabList[index].account2;
      collect_info.type = that.tabList[index].type;
      collect_info.price = that.tabList[index].price;
      collect_info.record={
            path:that.$route.path,
            chain:that.name,
            price:that.specified,
            start_price:that.startInterval,
            end_price:that.endInterval,
            start_time:that.startTime,
            end_time:that.endTime,
      }
      track_info = collect_info;
      if (type == "favorite") {
        collectPost({
          user_id: window.localStorage.getItem("user_id"),
          type: 4,
          collect_info: collect_info
        }).then(res => {
          console.log(res);
         
        });
      } else {
        trackPost({
          user_id: window.localStorage.getItem("user_id"),
          type: 4,
          track_info: track_info
        }).then(res => {
          console.log(res);
         
        });
      }

      this.tabList[index].isBoxes = false;
    },
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
.sum {
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
      width: 108px;
      height: 34px;
      background-color: #1b2d49;
      border-radius: 5px;
      border: none;
      padding: 0 10px;
      box-sizing: border-box;
      color: #fff;
    }
    span {
      margin: 0 8px;
    }
    ::placeholder {
      color: #a1a5c5;
    }
    button {
      width: 124px;
      height: 34px;
      background-color: #ff8a24;
      border-radius: 5px;
      border: none;
      font-size: 14px;
      color: #ffffff;
    }
    .onebtn {
      margin-left: 10px;
    }
    .twobtn {
      margin: 30px 82px 0 60px;
    }
  }
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
.sort {
  width: 274px;
  .el-dropdown-menu__item {
    height: 56px;
    display: flex;
    align-items: center;
    img {
      width: 10px;
      height: 14px;
      margin-left: 6px;
    }
    .green {
      display: none;
    }
  }
  .el-dropdown-menu__item:not(.is-disabled):hover > .green {
    display: block;
  }
  .el-dropdown-menu__item:not(.is-disabled):hover > .gray {
    display: none;
  }
  .el-icon-top,
  .el-icon-bottom {
    font-size: 16px;
    margin-left: 10px;
  }
}
.transaction {
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
    justify-content: space-between;
    .sinister {
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
    .main {
      display: flex;
      justify-content: flex-end;
      div {
        margin-left: 20px;
        font-size: 14px;
        color: #42b6f6;
        display: flex;
        align-items: center;
        img {
          width: 20px;
          height: 20px;
          margin-right: 5px;
        }
      }
    }
    .boult {
      width: 10px;
      height: 14px;
      margin-left: 6px;
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
        width: 50%;
      }
      .two {
        width: 20%;
      }
      .three {
        width: 30%;
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
        width: 50%;
      }
      .two {
        width: 20%;
        color: #06d514;
      }
      .three {
        width: 27%;
      }
      .four {
        width: 3%;
        text-align: right;
        img {
          width: 23px;
          height: 16px;
        }
      }

      .yellow {
        color: #ff8921;
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
