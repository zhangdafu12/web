<template>
  <div class="H_content_one">
    <div class="C_left">
      <div class="C_tittle">
        <div class="C_t_cont">
          <img class="C_logo" src="/static/images/icon_logo.png" alt />
          <div class="C_C_cont">
            <div>
              <span class="C_t_name">{{data.chain}}</span>
              <span class="C_t_rank">TOP {{index+1}}</span>
              <!-- <span class="C_t_up">{{this.$route.query[0].previous_24h_activity}}</span> -->
              <div class="spaceAround">
                <span class="C_t_up" v-if="data.change>=0">{{data.change}}</span>
                <span class="nav_n_down" v-else>{{data.change}}</span>
              </div>
              <!-- <img class="C_t_upI" src="/static/images/icon_up.png" alt /> -->
            </div>
            <div>
              <span class="C_t_pay">交易量：{{data.total_ts}}</span>
              <span class="C_t_time">截止时间：{{data.time}}</span>
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
    <div class="C_right">
      <div class="C_R_tit">{{data.chain}}实时转账记录</div>
      <div class="C_R_tab">
        <span>交易账户</span>
        <span>交易账户</span>
        <span>金额</span>
        <span>时间</span>
      </div>
      <div class="overFlowBox">
        <div
          v-for="(item,index) in transferList"
          :key="index"
          class="cont_det"
          :class="item.risk==1?'cont_det error':'cont_det'"
        >
          <div v-if="item.risk==0" class="det_type">真实交易</div>
          <div v-if="item.risk==1" class="det_type">虚假交易</div>
          <div class="det_detail">
            <div>
              <span class="user_d">{{item.account_1}}</span>
              <span v-if="item.type=='output'" class="green">转出</span>
              <span v-else class="orang">转入</span>
              <span class="user_d">{{item.account_2}}</span>
              <span class="type_tip">{{item.exchange}}</span>
            </div>
            <div class="time_money">
              <span v-if="item.type=='output'" class="green">{{item.price}}</span>
              <span v-else class="orang">{{item.price}}</span>
              <span>{{item.time}}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { chain } from "../../api/api";
export default {
  name: "home",
  data() {
    return {
      isEr: 2,
      timeType: 0,
      timeTList: ["1H", "6H", "12H", "24H", "3D", "1W", "1M", "1Y"],
      transferList: [
        // {
        //   id: 1,
        //   time: "2020-03-03 19:04:10",
        //   hash: "asdasdasdasd",
        //   account_1: "wqeqweqwe",
        //   account_2: "qweqweqweqweqw",
        //   type: "output",
        //   price: 9858,
        //   exchange: "okcoin", //交易所
        //   note: "None", //备注
        //   risk: "0" //0假 1真
        // }
      ]
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
    that.getData({});
    setTimeout(() => {
      chain
        .getchaintransactions({
          params: {
            chain_name: this.$parent.listData[this.$parent.indexTab].chain
          }
        })
        .then(res => {
          console.log(res,'---------------------------')
          that.transferList = res.transactions;
        });
    }, 1500);
  },
  updated() {
    let that=this
    let time = ["1h", "6h", "12h", "24h", "3d", "week", "month", "year"];
    let index = this.$parent.indexTab;
    let data = this.$parent.listData[index];
    console.log(data, index);
    this.getData({ name: data.chain, time_range: time[this.timeType] });
     setTimeout(() => {
        console.log(this.$parent.listData[this.$parent.indexTab].chain,'---------------------------')
      chain
        .getchaintransactions({
          params: {
            chain_name: this.$parent.listData[this.$parent.indexTab].chain
          }
        })
        .then(res => {
          console.log(res,'---------------------------')
          that.transferList = res.transactions;
        });
    }, 1500);
  },
  methods: {
    changeTimeType(i) {
      let index = this.$parent.indexTab;
      let data = this.$parent.listData[index];
      this.timeType = i;
      let time = ["1h", "6h", "12h", "24h", "3d", "week", "month", "year"];
      this.getData({ name: data.chain, time_range: time[i] });
    },

    //写在methods方法里面封装然后在，在mounted()里面调用个人比较喜欢这种的写法，方便封装
    getData({ name = "bch", time_range = "1h" }) {
      let that = this;
      let Edata = [];
      let time = [];
      chain
        .getbodyform({
          params: {
            chain_name: name,
            time_range: time_range
          }
        })
        .then(res => {
          console.log(res.bodyform, 1111111111111);
          res.bodyform.forEach(item => {
            Edata.push(item.total_amount);
            time.push(item.end_time);
          });
          // ----------
          let obj = this.$refs.sum;
          // 基于准备好的dom，初始化echarts实例 写在 mounted（）里面
          let sum_earnings = that.$echarts.init(obj);
          that.drawLine1(sum_earnings, Edata, time);
          // 需要在mounted（）方法里面初始化echarts实例之后调用
          window.onresize = function() {
            sum_earnings.resize();
          };
        });
    },
    drawLine1(name, Edata, time) {
      let that = this;
      var charts = {
        unit: "交易量",
        names: ["新增交易量"],
        lineX: time,
        value: Edata
      };
      var color = ["rgba(98, 101, 105"];
      var lineY = [];

      for (var i = 0; i < charts.names.length; i++) {
        var x = i;
        if (x > color.length - 1) {
          x = color.length - 1;
        }
        var data = {
          name: charts.names[i],
          type: "line",
          color: color[x] + ")",
          smooth: true,
          areaStyle: {
            normal: {
              color: new that.$echarts.graphic.LinearGradient(
                0,
                0,
                0,
                1,
                [
                  {
                    offset: 0,
                    color: color[x] + ", 0.3)"
                  },
                  {
                    offset: 0.8,
                    color: color[x] + ", 0)"
                  }
                ],
                false
              ),
              shadowColor: "rgba(0, 0, 0, 0.1)",
              shadowBlur: 10
            }
          },
          symbol: "circle",
          symbolSize: 5,
          data: charts.value
        };

        lineY.push(data);
      }

      lineY[0].markLine = {
        silent: true,
        data: [
          {
            yAxis: 2500
          },
          {
            yAxis: 3500
          },
          {
            yAxis: 4500
          }
        ]
      };
      console.log(lineY, charts);
      var option = {
        backgroundColor: "#1b2d46",
        tooltip: {
          trigger: "axis"
        },
        legend: {
          show: false,
          data: charts.names,
          textStyle: {
            fontSize: 12,
            color: "rgb(0,253,255,0.6)"
          },
          right: "4%"
        },
        grid: {
          top: "14%",
          left: "4%",
          right: "4%",
          bottom: "12%",
          containLabel: true
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: charts.lineX,
          axisLabel: {
            textStyle: {
              color: "rgb(0,253,255,0.6)"
            },
            formatter: function(params) {
              return params.split(" ")[0];
            }
          }
        },
        yAxis: {
          name: charts.unit,
          type: "value",
          position: "right",
          axisLabel: {
            formatter: "{value}",
            textStyle: {
              color: "rgb(0,253,255,0.6)"
            }
          },
          splitLine: {
            lineStyle: {
              color: "rgb(23,255,243,0.3)"
            }
          },
          axisLine: {
            lineStyle: {
              color: "#264766"
            }
          }
        },
        series: lineY
      };

      // 绘制图表
      name.setOption(option);
    }
  }
};
</script>


<style lang="less">
.H_content_one {
  width: 100%;
  height: 608px;
  display: flex;
  justify-content: space-between;
  .C_left {
    width: 732px;
    height: 608px;
    position: relative;
    background-color: #1e344d;
    opacity: 0.8;
    padding-top: 20px;
    box-sizing: border-box;
    .C_tittle {
      width: calc(100% - 20px);
      height: 71px;
      background-color: #213b58;
      box-sizing: border-box;
      margin: 0 10px;
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
            .nav_n_down {
              font-size: 12px;
              color: #e55541;
              line-height: 20px;
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
  .C_right {
    width: 471px;
    height: 608px;
    background-color: rgba(25, 42, 66, 0.7);
    opacity: 0.7;
    padding: 14px 10px;
    box-sizing: border-box;
    .C_R_tit {
      font-size: 18px;
      color: #fff;
      text-align: center;
      margin-bottom: 10px;
    }
    .C_R_tab {
      width: 100%;
      display: flex;
      justify-content: space-around;
      color: #586c86;
      border-bottom: solid 1px #586c86;
      height: 32px;
      margin-bottom: 10px;
    }
    .overFlowBox {
      width: 100%;
      height: 516px;
      overflow-y: scroll;
      overflow-x: hidden;
      padding-bottom: 10px;
      box-sizing: border-box;
    }
    .overFlowBox::-webkit-scrollbar {
      width: 6px;
      background: slategray;
      border-radius: 2px;
    }
    .overFlowBox::-webkit-scrollbar-thumb {
      background: rgb(147, 196, 245);
    }
    .cont_det {
      width: 100%;
      height: 78px;
      border-radius: 5px;
      overflow: hidden;
      margin-top: 12px;
      .det_type {
        width: 100%;
        height: 20px;
        background-color: #0f2033;
        font-size: 10px;
        color: #ffffff;
        text-indent: 4px;
      }
      .det_detail {
        width: 100%;
        height: 68px;
        background: rgb(46, 70, 104);
        display: flex;
        font-size: 14px;
        justify-content: space-around;
        padding-left: 10px;
        box-sizing: border-box;
        color: #42b6f6;

        .time_money {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding-left: 4px;
          box-sizing: border-box;

          span:last-child {
            color: #a1a5c5;
          }
        }
        div {
          width: 100%;
          display: flex;
          align-items: center;
          span {
            margin-right: 10px;
          }
          .green {
            color: #06d514;
            font-size: 10px;
            white-space: nowrap; /*强制span不换行*/
          }
          .orang {
            color: #ff8921;
            font-size: 10px;
            white-space: nowrap; /*强制span不换行*/
          }
          .user_d {
            display: inline-block;
            width: 58px;
            overflow: hidden;
            white-space: nowrap;
          }
          .type_tip {
            margin-right: 2px;
            height: 18px;
            line-height: 18px;
            background: #ff9f0e;
            display: inline-block;
            font-size: 8px;
            color: #ffffff;
            border-radius: 2px;
            padding: 2px;
          }
        }
      }
    }
    .error {
      .det_type {
        background-color: rgba(255, 68, 68, 1);
      }
      .det_detail {
        background: #76495f;
      }
    }
  }
}
</style>
