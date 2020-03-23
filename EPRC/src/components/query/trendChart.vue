<template>
  <div class="trendChart">
    <div class="trend" v-show="trendChart==0">
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
          <!-- <el-dropdown trigger="click" placement="bottom-start" ref="sum">
            <span :class="spanColor[1]?'el-dropdown-link spanColor':'el-dropdown-link'">
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
          </el-dropdown>-->
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
        </div>-->
      </div>
      <div class="trend_cont">
        <div class="title">
          <div class="sinister">
            <img src="../../../static/images/fat.png" alt class="coinImg" />
            <div class="trend_mess">
              <p>{{infoData.chain_name}}</p>
              <div>
                <span @click="trendRecord(0,0)">总交易量：{{infoData.total_amounts}}</span>
                <span @click="trendRecord(0,1)">真实交易量：{{infoData.real_amounts}}</span>
                <span @click="trendRecord(0,2)">虚假交易量：{{infoData.fake_amounts}}</span>
                <span>截止时间：{{infoData.last_time}}</span>
              </div>
            </div>
          </div>
          <div class="dexter">
            <img src="../../../static/images/omit.png" alt class="omit" />
            <img src="../../../static/images/download.png" alt class="download" />
          </div>
        </div>
        <div class="timeType">
          <span
            @click="changeTimeType(index)"
            v-for="(item,index) in timeTList"
            :key="index"
            :class="{'active':timeType==index}"
          >{{item}}</span>
        </div>
        <div class="chart" ref="chart"></div>
      </div>
    </div>
    <div class="record" v-show="trendChart==1">
      <div class="title">
        <span v-if="tabChart==0">总交易记录</span>
        <span v-else-if="tabChart==1">真实交易记录</span>
        <span v-else-if="tabChart==2">虚假交易记录</span>
        <span class="back" @click="trendRecord(1,3)">返回上一级</span>
      </div>
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
        <!-- <img src="../../../static/images/omit.png" alt /> -->
      </div>
      <div class="table">
        <ul class="tabs">
          <li class="one">交易账户</li>
          <li class="two">交易账户</li>
          <li class="three">金额</li>
          <li class="four">时间</li>
        </ul>
        <div v-for="(item,index) in tabList" :key="index">
          <ul class="tabs_cont" :class="index % 2 == 0?'bg-g':''">
            <li class="one">{{item.account_1}}</li>
            <li class="two">
              <img
                :src="item.type=='input'?'../../../static/images/enter.png':'../../../static/images/exit.png'"
                alt
              />
            </li>
            <li class="three">{{item.account_2}}</li>
            <li class="four">{{item.price}}</li>
            <li class="five">{{item.time}}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  chain,
  collectPost,
  trackGet,
  selectr,
  trackPost
} from "../../api/api";
import { Message, Loading } from "element-ui";
export default {
  data() {
    return {
      infoData: "",
      trendChart: 0,
      tabChart: 0,
      name: "bch",
      sum: "金额",
      rank: "排序",
      time: " 时间",
      boult: "",
      isBoult: false,
      spanColor: [0, 0, 0, 0],
      nameList: ["eth", "bch", "btc"],
      rankList: [
        {
          txt: "时间",
          grayImgs: "../../../static/images/gray.png",
          greenImgs: "../../../static/images/green.png"
        },
        {
          txt: "时间",
          grayImgs: "../../../static/images/gray(1).png",
          greenImgs: "../../../static/images/green(1).png"
        },
        {
          txt: "金额",
          grayImgs: "../../../static/images/gray.png",
          greenImgs: "../../../static/images/green.png"
        },
        {
          txt: "金额",
          grayImgs: "../../../static/images/gray(1).png",
          greenImgs: "../../../static/images/green(1).png"
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
        //   type: "input",
        //   account_1: "0xc97a4ed29f03fd549c4ae79086673523122d2bc5",
        //   account_2: "0xc97a4ed29f03fd549c4ae79086673523122d2bc7",
        //   price: "921.79",
        //   time: "14:50  18/04/17"
        // }
      ],
      timeType: 0,
      timeTList: ["1h", "6h", "12h", "24h", "3D", "1W", "1M", "1Y"]
    };
  },
  mounted() {
    let that = this;
    that.getHearData({});
  },
  methods: {
    //获取表头
    getHearData({ chainName = "bch", time = "1h" }) {
      let that = this;
      chain
        .chain_volume({
          params: {
            chain_name: chainName
          }
        })
        .then(res => {
          console.log(res.data);
          that.infoData = res.data;
          that.getChartData({ chain_name: chainName, time: time });
        });
    },
    //获取图
    getChartData({ chain_name = "bch", time = "1h" }) {
      let that = this;
      chain
        .time_data({
          params: {
            chain_name: chain_name,
            time: time
          }
        })
        .then(res => {
          console.log(res); //data1真 data2假 data3总
          // that.infoData=res.data;
          let real = res.data1;
          let fake = res.data2;
          let total = res.data3;
          let time = [];
          let realData = [];
          let fakeData = [];
          let totalData = [];
          real.forEach(item => {
            time.push(item.end_time);
            realData.push(item.real_amount);
          });
          fake.forEach(item => {
            fakeData.push(item.fake_amount);
          });
          total.forEach(item => {
            totalData.push(item.total_amount);
          });

          let that = this;

          // ----------
          let obj = this.$refs.chart;
          console.log(obj);
          // 基于准备好的dom，初始化echarts实例 写在 mounted（）里面
          let sum_earnings = that.$echarts.init(obj);
          that.drawLine(sum_earnings, realData, fakeData, totalData, time);
          // 需要在mounted（）方法里面初始化echarts实例之后调用
          window.onresize = function() {
            sum_earnings.resize();
          };
        });
    },
    //名称下拉框
    onName(index) {
      this.name = this.nameList[index];
      this.spanColor[0] = 1;
      let time = this.timeTList[this.timeType];
      this.getHearData({ chainName: this.name, time: time });
      this.getAllInfo();
    },
    //金额下拉框
    sunConfirm(i) {
      let that = this;

      if (i == "specified") {
        that.sum = that.specified;
        that.startInterval = "";
        that.endInterval = "";
        if (parseFloat(that.specified).toString() == "NaN") {
          Message({
            message: "金额为数字",
            duration: 1000,
            type: "warning"
          });
            
        } else {
           that.sum = that.specified;
          this.getAllInfo();
        }
      } else {
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
          this.getAllInfo();
        }
      }

      that.$refs.sum.hide();
    },
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
        // console.log()
        this.getAllInfo();
      }
      console.log(this.startTime, this.endTime);
    },
    TimeChange() {
      this.$refs.time.show();
      console.log(this.startTime, this.endTime);
      // that.$refs.time.hide();
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
      // this.spanColor = 1;
    },
    onTime(i) {
      this.isTime = i;
    },
    onOmit(index) {
      this.tabList[index].isBoxes = !this.tabList[index].isBoxes;
    },
    //收藏 追踪
    onBox(type, index) {
      console.log(type);
      let that = this;
      //favorite 收藏
      //trace 追踪collectPost, trackGet, selectr, trackPost
      let collect_info = {};
      let track_info = {};
      collect_info.chain = that.name;
      collect_info.id = that.tabList[index].id;
      collect_info.account1 = that.tabList[index].account1;
      collect_info.account2 = that.tabList[index].account2;
      collect_info.type = that.tabList[index].type;
      collect_info.price = that.tabList[index].price;
      collect_info.record = {
        path: that.$route.path,
        chain: that.name,
        price: that.specified,
        start_price: that.startInterval,
        end_price: that.endInterval,
        start_time: that.startTime,
        end_time: that.endTime
      };
      track_info = collect_info;
      if (type == "favorite") {
        collectPost({
          user_id: window.localStorage.getItem("user_id"),
          type: 4,
          collect_info: collect_info
        }).then(res => {
          console.log(res);
          Message({
            message: "收藏成功",
            duration: 1000,
            type: "success"
          });
        });
      } else {
        trackPost({
          user_id: window.localStorage.getItem("user_id"),
          type: 4,
          track_info: track_info
        }).then(res => {
          console.log(res);
          Message({
            message: "追踪成功",
            duration: 1000,
            type: "success"
          });
        });
      }

      this.tabList[index].isBoxes = false;
    },
    //真 假  总详细
    getAllInfo() {
      let that = this;
      let data = {};

      if (that.specified == "") {
        data.params = {
          chain_name: that.name,
          assign_price: that.specified,
          start_time: that.startTime,
          end_time: that.endTime
        };
      } else {
        data.params = {
          chain_name: that.name,
          start_money: that.startInterval,
          end_money: that.endInterval,
          start_time: that.startTime,
          end_time: that.endTime
        };
      }
      if (that.tabChart == 0) {
        // total_recoding

        chain.total_recoding(data).then(res => {
          that.tabList = res.data;
        });
      } else if (that.tabChart == 1) {
        // real_recoding
        chain.real_recoding(data).then(res => {
          that.tabList = res.data;
        });
      } else {
        // fake_recoding
        chain.fake_recoding(data).then(res => {
          that.tabList = res.data;
        });
      }
    },

    trendRecord(i, type) {
      let that = this;
      if (i == 0) {
        this.trendChart = 1;
        this.tabChart = type;
        //type;0总 1真 2假
        //根据type修改tabList
        that.getAllInfo();
      } else {
        this.trendChart = 0;
      }
    },
    changeTimeType(i) {
      this.timeType = i;
      let time = this.timeTList[this.timeType];
      this.getHearData({ chainName: this.name, time: time });
    },

    //写在methods方法里面封装然后在，在mounted()里面调用个人比较喜欢这种的写法，方便封装

    drawLine(name, realData, fakeData, totalData, time) {
      let option = {
        tooltip: {
          trigger: "axis"
        },
        color: ["#00ce7d", "#fcc352", "#ff4444"],
        legend: {
          icon: "roundRect",
          right: 4,
          itemHeight: 2,
          itemWidth: 10,
          data: ["总交易量", "真实交易", "虚假交易"],
          textStyle: {
            color: "#376691"
          }
        },
        grid: {
          top: 40,
          bottom: 20,
          left: 10,
          right: 0,
          containLabel: true
        },

        xAxis: {
          axisLabel: { color: "#274868" }, // x轴字体颜色

          axisLine: {
            lineStyle: { color: "#274868" } // x轴坐标轴颜色
          },

          axisTick: {
            lineStyle: { color: "#274868" } // x轴刻度的颜色
          },
          type: "category",
          boundaryGap: false,
          data: time,
          splitLine: {
            //网格线
            show: true,
            lineStyle: { color: "#274868" } // x轴坐标轴颜色
          }
        },
        yAxis: {
          axisLabel: { color: "#274868" }, // x轴字体颜色

          axisLine: {
            lineStyle: { color: "#274868" } // x轴坐标轴颜色
          },

          //   axisTick: {
          //     lineStyle: { color: "rgb(150,150,150)" } // x轴刻度的颜色
          //   },
          type: "value",
          position: "right",
          axisTick: {
            //y轴刻度线
            show: true,
            lineStyle: { color: "#274868" } // x轴坐标轴颜色
          },
          splitLine: {
            //网格线
            show: true,
            lineStyle: { color: "#274868" } // x轴坐标轴颜色
          }
        },
        series: [
          {
            name: "总交易量",
            type: "line",
            stack: "总量",
            data: totalData,
            smooth: true,
            markLine: {
              silent: true,
              data: [
                {
                  yAxis: 5
                },
                {
                  yAxis: 100
                },
                {
                  yAxis: 150
                }
              ]
            }
          },
          {
            name: "真实交易",
            type: "line",
            stack: "总量",
            data: realData,
            smooth: true
          },
          {
            name: "虚假交易",
            type: "line",
            stack: "总量",
            data: fakeData,
            smooth: true
          }
        ]
      };

      // 绘制图表
      name.setOption(option);
    }
  }
};
</script>


<style lang="less">
ul,
li,
p {
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
.trendChart {
  width: 1228px;
  margin-top: 20px;
  .trend {
    .pull_cont {
      height: 40px;
      box-sizing: border-box;
      padding: 0 25px 0 20px;
      margin-bottom: 2px;
      display: flex;
      justify-content: space-between;
      background-color: #1e344d;
      opacity: 0.8;
      .sinister {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        box-sizing: border-box;
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
    }
    .trend_cont {
      height: 610px;
      background-color: #1e344d;
      opacity: 0.8;
      box-sizing: border-box;
      padding-top: 20px;
      position: relative;
      .timeType {
        display: flex;
        font-size: 12px;
        color: #376691;
        align-items: center;
        padding: 10px 10px;
        padding-bottom: 0px;
        position: absolute;
        top: 100px;
        left: 10px;
        z-index: 100;
        span {
          margin-right: 24px;
          cursor: pointer;
        }
        .active {
          color: #42b6f6;
        }
      }
      .title {
        width: 1208px;
        height: 70px;
        background-color: #213b58;
        margin: 0 10px;
        box-sizing: border-box;
        padding: 0 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        .sinister {
          display: flex;
          justify-content: flex-start;
          align-items: center;
          .coinImg {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            margin-right: 10px;
          }
          p {
            font-size: 20px;
            color: #ffffff;
          }
          .trend_mess {
            font-size: 14px;
            span {
              margin-right: 20px;
            }
            span:nth-child(1) {
              color: #00ce7d;
            }
            span:nth-child(2) {
              color: #fcc352;
            }
            span:nth-child(3) {
              color: #ff4444;
            }
            span:nth-child(4) {
              color: #586c86;
            }
          }
        }
        .dexter {
          display: flex;
          align-items: center;
          .omit {
            width: 24px;
            height: 16px;
            margin-right: 20px;
          }
          .download {
            width: 22px;
            height: 22px;
          }
        }
      }
      .chart {
        height: 520px;
      }
    }
  }
  .record {
    min-height: 674px;
    background-color: #1e344d;
    opacity: 0.8;
    box-sizing: border-box;
    padding-top: 20px;
    .title {
      width: 1208px;
      height: 52px;
      background-color: #213b58;
      margin: 0 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 20px 0 10px;
      box-sizing: border-box;
      font-size: 18px;
      color: #ffffff;
      .back {
        font-size: 14px;
        color: #42b6f6;
      }
    }
    .pull_cont {
      margin: 0 10px 0 20px;
      padding: 25px 20px 10px 0;
      box-sizing: border-box;
      border-bottom: solid 1px #1f3e5a;
      display: flex;
      justify-content: space-between;
      .sinister {
        display: flex;
        justify-content: flex-start;
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
      img {
        width: 24px;
        height: 16px;
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
        padding: 0 10px;
        box-sizing: border-box;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: #586c86;
        .one {
          width: 40%;
        }
        .two {
          width: 34%;
        }
        .three,
        .four {
          width: 13%;
        }
      }
      .tabs_cont {
        height: 48px;
        line-height: 48px;
        width: 100%;
        padding: 0 10px;
        box-sizing: border-box;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: #42b6f6;
        .one {
          width: 30%;
        }
        .two {
          width: 10%;
          text-align: center;
          margin-right: 10px;
          img {
            width: 28px;
            height: 16px;
          }
        }
        .three {
          width: 34%;
        }
        .four {
          width: 13%;
          color: #06d514;
        }
        .five {
          width: 13%;
          white-space: nowrap;
        }

        .yellow {
          color: #ff8921;
        }
      }
      .bg-g {
        background-color: rgba(24, 43, 65, 0.32);
      }
    }
  }
}
</style>
