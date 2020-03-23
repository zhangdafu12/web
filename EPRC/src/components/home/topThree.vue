<template>
  <div class="H_content_Three">
    <div class="C_left" :data-select="select">
      <div v-show="isEmpty" class="C_Chart" id="Echarts" ref="sum" :data-index="index"></div>
    </div>
  </div>
</template>

<script>
import { chain } from "../../api/api";
import { Message, Loading } from "element-ui";
export default {
  name: "home",
  data() {
    return {
      dataList: [],
      isEmpty: true
    };
  },

  mounted() {
    let that = this;
    that.getlargetsRank({
      chain_name: that.$store.state.activeIndexVal,
      time_range: this.$parent.select
    });
  },
  updated() {
    let that = this;
    let index = parseInt(this.$parent.indexTab);
    console.log("updated");
    
    that.getlargetsRank({
      chain_name: that.$store.state.activeIndexVal,
      time_range: this.$parent.select
    });
  },
  computed: {
    index() {
      return parseInt(this.$parent.indexTab);
    },
    select() {
      return this.$parent.select;
    }
  },
  methods: {
    changeTimeType(i) {
      this.timeType = i;
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
          console.log(res);
          let data = [];
          for (let i in res) {
            data.push(res[i].table_data);
          }

          if (data.length == 0) {
            that.isEmpty = false;
            Message({
              message: "暂无数据！",
              duration: 1000,
              type: "warning"
            });
          } else {
            that.isEmpty = true;
            that.dataList = data;
            let index = parseInt(this.$parent.indexTab);
            that.loadEchart(index);
          }
        });
    },
    //加载图数据
    loadEchart(index) {
      let that = this;
      let obj = {};
      let datas = [];
      let links = [];
      that.dataList[index].Data1.forEach((item, index) => {
        console.log(item);
        obj = {};
        obj.id = item.id;
        obj.name = item.hash;
        obj.value = item.access;
        obj.symbolSize = 60;
        obj.draggable = true;
        obj.category = item.type;
        datas.push(obj);
        console.log(item.type);
      });
      links = that.dataList[index].links;
      that.list = datas;
      console.log(datas);
      console.log(that.dataList[index].links);
      this.echartRun(datas, links);
    },
    //图表
    echartRun(datas, links) {
      let that = this;
      //  let dom = this.$refs.sum;
      let dom = document.getElementById("Echarts");
      // 基于准备好的dom，初始化echarts实例 写在 mounted（）里面
      let myChart = that.$echarts.init(dom);
      myChart.setOption({
        tooltip: {},
        color: ["#00ce7d", "#e86df1", "#c2c271", "#7479ff"],
        legend: [
          {
            formatter: function(name) {
              return that.$echarts.format.truncateText(
                name,
                40,
                "14px Microsoft Yahei",
                "…"
              );
            },
            tooltip: {
              show: true
            },
            selectedMode: "true",
            bottom: 20
          }
        ],
        toolbox: {
          show: false,
          feature: {
            dataView: {
              show: true,
              readOnly: true
            },
            restore: {
              show: true
            },
            saveAsImage: {
              show: true
            }
          }
        },
        animationDuration: 1000,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "交易记录",
            type: "graph",
            layout: "force",

            force: {
              repulsion: 500,
              edgeLength: 120
            },

            data: datas,
            links: links,
            categories: [
              {
                name: "output"
              },
              {
                name: "input"
              },
              {
                name: ""
              }
            ],
            focusNodeAdjacency: true,
            roam: true,
            label: {
              normal: {
                show: true,
                position: "top"
              }
            },
            lineStyle: {
              normal: {
                color: "source",
                curveness: 0.8,
                type: "solid"
              }
            }
          }
        ]
      });
    },
    //写在methods方法里面封装然后在，在mounted()里面调用个人比较喜欢这种的写法，方便封装

    drawLine(name) {
      let that = this;
      let option = {
        tooltip: {},
        legend: [
          {
            formatter: function(name) {
              return that.$echarts.format.truncateText(
                name,
                40,
                "14px Microsoft Yahei",
                "…"
              );
            },
            tooltip: {
              show: true
            },
            selectedMode: "true",
            bottom: 20
            // data: ['招标倾向性', '装饰装修项目', '房建项目', '园林绿化项目', '其他项目', '市政项目', '园林绿化项目']
          }
        ],
        toolbox: {
          show: false,
          feature: {
            dataView: {
              show: true,
              readOnly: true
            },
            restore: {
              show: true
            },
            saveAsImage: {
              show: true
            }
          }
        },
        animationDuration: 1000,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "招标倾向性分析",
            type: "graph",
            layout: "force",
            force: {
              repulsion: 500,
              edgeLength: 120
            },
            data: [
              {
                id: 0,
                name: "招标倾向性",
                // "x": 0,
                // y: 0,
                symbolSize: [60, 60],
                draggable: "false",
                category: "父节点",
                value: 200
              },
              {
                id: 1,
                name: "房建项目",
                value: 25,
                symbolSize: 40,
                category: "项目类型",
                draggable: "true"
              },
              {
                id: 2,
                name: "市政项目",
                symbolSize: 32,
                category: "项目类型",
                draggable: "true",
                value: 15
              },
              {
                id: 3,
                name: "装饰装修项目",
                symbolSize: 40,
                category: "项目类型",
                draggable: "true",
                value: 15
              },
              {
                id: 4,
                name: "园林绿化项目",
                symbolSize: 40,
                category: "项目类型",
                draggable: "true",
                value: 15
              },
              {
                id: 5,
                name: "其他项目",
                symbolSize: 40,
                category: "项目类型",
                draggable: "true",
                value: 15
              },
              {
                id: 6,
                name: "定性评审法",
                symbolSize: 53,
                category: "评标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 7,
                name: "抽签定标法",
                symbolSize: 26,
                category: "评标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 8,
                name: "其他",
                symbolSize: 45,
                category: "评标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 9,
                name: "综合评估法",
                symbolSize: 45,
                category: "评标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 10,
                name: "综合定性评审法",
                symbolSize: 45,
                category: "评标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 11,
                name: "抽签定标法",
                symbolSize: 45,
                category: "评标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 12,
                name: "低价法",
                symbolSize: 45,
                category: "评标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 13,
                name: "抽签定标法",
                symbolSize: 26,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 14,
                name: "票决抽签",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 15,
                name: "直接票决",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 16,
                name: "逐轮票决",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 17,
                name: "直接定标",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 18,
                name: "随机抽取",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 19,
                name: "先评后抽",
                symbolSize: 26,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 20,
                name: "集体议事法",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 21,
                name: "价格法",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 22,
                name: "价格竞争法",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 23,
                name: "价格偏离法",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 24,
                name: "其他",
                symbolSize: 45,
                category: "定标办法",
                draggable: "true",
                value: 10
              },
              {
                id: 25,
                name: "特级",
                symbolSize: 45,
                category: "中标企业",
                draggable: "true",
                value: 10
              },
              {
                id: 26,
                name: "一级",
                symbolSize: 30,
                category: "中标企业",
                draggable: "true",
                value: 10
              },
              {
                id: 27,
                name: "二级",
                symbolSize: 25,
                category: "中标企业",
                draggable: "true",
                value: 10
              },
              {
                id: 28,
                name: "三级",
                symbolSize: 20,
                category: "中标企业",
                draggable: "true",
                value: 10
              },
              {
                id: 29,
                name: "其他",
                symbolSize: 45,
                category: "中标企业",
                draggable: "true",
                value: 10
              }
            ],
            links: [
              {
                source: "0",
                target: "1"
              },
              {
                source: "0",
                target: "2"
              },
              {
                source: "0",
                target: "3"
              },
              {
                source: "0",
                target: "4"
              },
              {
                source: "0",
                target: "5"
              },
              {
                source: "1",
                target: "6"
              },
              {
                source: "1",
                target: "7"
              },
              {
                source: "1",
                target: "8"
              },
              {
                source: "2",
                target: "9"
              },
              {
                source: "2",
                target: "10"
              },
              {
                source: "2",
                target: "11"
              },
              {
                source: "3",
                target: "12"
              },
              {
                source: "6",
                target: "13"
              },
              {
                source: "6",
                target: "14"
              },
              {
                source: "6",
                target: "15"
              },
              {
                source: "7",
                target: "16"
              },
              {
                source: "7",
                target: "17"
              },
              {
                source: "8",
                target: "18"
              },
              {
                source: "9",
                target: "19"
              },
              {
                source: "9",
                target: "20"
              },
              {
                source: "10",
                target: "21"
              },
              {
                source: "10",
                target: "22"
              },
              {
                source: "11",
                target: "23"
              },
              {
                source: "12",
                target: "24"
              },
              {
                source: "14",
                target: "25"
              },
              {
                source: "14",
                target: "26"
              },
              {
                source: "14",
                target: "27"
              },
              {
                source: "14",
                target: "28"
              },
              {
                source: "14",
                target: "29"
              }
            ],
            categories: [
              {
                name: "项目类型"
              },
              {
                name: "评标办法"
              },
              {
                name: "父节点"
              },
              {
                name: "定标办法"
              },
              {
                name: "中标企业"
              }
            ],
            focusNodeAdjacency: true,
            roam: true,
            label: {
              normal: {
                show: true,
                position: "top"
              }
            },
            lineStyle: {
              normal: {
                color: "source",
                curveness: 0.4,
                type: "solid"
              }
            }
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
.H_content_Three {
  width: 100%;
  height: 608px;
  display: flex;
  justify-content: space-between;
  .C_left {
    width: 100%;
    height: 608px;
    //   background-color: #1e344d;
    opacity: 0.8;
    padding-top: 20px;
    // margin-right: 20px;
    box-sizing: border-box;

    .C_Chart {
      width: 100%;
      height: 500px;
      margin-top: 15px;
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
