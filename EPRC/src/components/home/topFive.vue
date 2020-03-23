<template>
  <div class="H_content_Five">
    <div class="C_left">
      <div class="C_tittle">
        <div class="C_t_cont">
          <img class="C_logo" src="/static/images/icon_logo.png" alt />
          <div class="C_C_cont">
            <div>
              <span class="C_t_name">{{data.chain}}</span>
              <span class="C_t_rank">TOP {{index+1}}</span>
            </div>
            <div>
              <span class="C_t_up">活跃度(24h)：{{data.previous_24h_activity}}</span>
              <img class="C_t_upI" src="/static/images/icon_up.png" alt />
              <span class="C_t_pay">内部交易总量：{{data.total_amount}}</span>
              <span class="C_t_time">截止时间：{{data.update_time}}</span>
            </div>
          </div>
        </div>
        <img class="ic_down" src="/static/images/icon_download.png" alt />
      </div>
      <div class="timeType">
        <span
          @click="changeTimeType(index)"
          v-for="(item,index) in timeTList"
          :key="index"
          :class="{'active':timeType==index}"
        >{{item}}</span>
      </div>
      <div class="C_Chart" ref="sum"></div>
    </div>
  </div>
</template>

<script>
import { chain } from "../../api/api";
export default {
  name: "home",
  data() {
    return {
      timeType: 0,
      timeTList: ["1h", "6h", "12h", "24h", "3d", "1w", "1m", "1y"]
    };
  },
  computed: {
    index() {
      let index = parseInt(this.$parent.indexTab);
      return index;
    },
    data() {
      let data = this.$parent.listData[this.$parent.indexTab];
      return data;
    }
  },
  mounted() {
    let that = this;
    this.getchain({});
  },
  updated() {
    let index = this.$parent.indexTab;
    let data = this.$parent.listData[index];
      let time = ["1h", "6h", "12h", "24h", "3d", "week", "month", "year"];
    this.getchain({ name: data.chain, time_unit: time[this.timeType] });
  },
  methods: {
    changeTimeType(i) {
     let index = this.$parent.indexTab;
      let data = this.$parent.listData[index];
      this.timeType = i;
      let time = ["1h", "6h", "12h", "24h", "3d", "week", "month", "year"];
      this.getchain({ name: data.chain, time_unit: time[i] });
      // this.getchain({ time_unit: time[i] });
    },
    //写在methods方法里面封装然后在，在mounted()里面调用个人比较喜欢这种的写法，方便封装{a,b=2,c}

    getchain({ name = "bch", time_unit = "1h" }) {
      let that = this;
      let data1 = [];
      let data2 = [];
      let time = [];
      let params = that.$store.state.params;
      chain
        .getchainactive({
          params: {
            chain: name,
            time_unit: time_unit
          }
        })
        .then(res => {
          res.forEach(item => {
            data1.push(item.active_account);
            data2.push(item.total_account);
            time.push(item.end_time);
          });

          // ----------
          let obj = this.$refs.sum;
          // 基于准备好的dom，初始化echarts实例 写在 mounted（）里面
          let sum_earnings = that.$echarts.init(obj);
          that.drawLine(sum_earnings, data1, data2, time);
          // 需要在mounted（）方法里面初始化echarts实例之后调用
          window.onresize = function() {
            sum_earnings.resize();
          };
        });
    },

    drawLine(name, data1, data2, time) {
      let option = {
        tooltip: {
          trigger: "axis"
        },
        color: ["#00ce7d", "#fcc352"],
        legend: {
          icon: "roundRect",
          right: 4,
          itemHeight: 2,
          itemWidth: 10,
          data: ["日活账户", "总账户"],
          textStyle: {
            fontSize: 12,
            color: "rgb(0,253,255,0.6)"
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
            name: "日活账户",
            type: "line",
            stack: "总量",
            data: data1,
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
            name: "总账户",
            type: "line",
            stack: "总量",
            data: data2,
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
.H_content_Five {
  width: 100%;
  height: 608px;
  display: flex;
  justify-content: space-between;
  .C_left {
    width: 100%;
    height: 608px;
    background-color: #1e344d;
    opacity: 0.8;
    padding-top: 20px;
    position: relative;
    box-sizing: border-box;
    .C_tittle {
      width: calc(100% - 20px);
      height: 71px;
      background-color: #213b58;
      box-sizing: border-box;
      margin: 0 10px;
      display: flex;
      padding: 0 20px;
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
            }
            .C_t_upI {
              width: 7px;
              height: 10px;
              margin-right: 20px;
            }
            .C_t_pay {
              font-size: 14px;
              color: #ff625d;
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
  }
  // .C_right {
  //   width: 471px;
  //   height: 608px;
  //   background-color: #1e344d;
  //   opacity: 0.7;
  // }
}
</style>
