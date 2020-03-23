<template>
  <div class="record">
    <div class="title">浏览记录</div>
    <div class="box_cont">
      <div class="box" v-for="(F,index) in boxList" :key="index">
        <div class="sinister">
          <div class="account">
          
            <span @click="goHistory(index)">{{F.history_info.chain}}</span>
          </div>
          <div class="type_time">
            <span>类型:{{F.type==0?'排行':F.type==1?"查询":'我的'}}</span>
            <span>{{F.time}}</span>
          </div>
        </div>
        <div class="dexte" @click="onDel(index)">
          <img src="../../../static/images/del.png" alt />
          <span>删除</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { historyGet,historyPut } from "../../api/api";
export default {
  data() {
    return {
       boxList: [
        // {
        //   history_id: 1,
        //  history_info: {
        //     account_hash: "fjsadflaskjflas"
        //   },
        //   type: 1,
        //   time: "2020-02-03 16:44:26"
        // }
      ]
    };
  },
  created() {
    let that = this;
    historyGet({
      params: {
        user_id: window.localStorage.getItem("user_id")
      }
    })
      .then(res => {
        console.log(res);
        that.boxList = res;
      })
      .catch(err => {
        console.log(err);
      });
  },
  methods:{
    onDel(i){
       let that = this;
      window.localStorage.getItem("user_id");
      historyPut({
        user_id: window.localStorage.getItem("user_id"),
        history_id: that.boxList[i].history_id
      }).then(res => {
        console.log(res);
        that.boxList.splice(i, 1);
      });
    },
    goHistory(index){
       let that = this;
      let his=that.boxList[index].history_info
      console.log(his)
if(his.query){
that.$store.commit("changeActiveIndexVal", his.query);
that.$router.push({path:his.path})
}else{
  that.$router.push({path:his.path})
}

    
    }
    
  }
};
</script>


<style lang="less">
.record {
  width: 1022px;
  height: 688px;
  background-color: #1e344d;
  opacity: 0.8;
  .title {
    width: 1002px;
    height: 52px;
    line-height: 52px;
    background-color: rgba(33, 59, 88, 0.47);
    margin: 0 auto;
    margin-top: 10px;
    box-sizing: border-box;
    padding-left: 10px;
    font-size: 18px;
    color: #ffffff;
  }
  .box_cont::-webkit-scrollbar {
    display: none;
  }
  .box_cont {
    width: 100%;
    height: 606px;
    box-sizing: border-box;
    padding: 0 10px 0 20px;
    overflow: auto;
    .box {
      width: 100%;
      height: 90px;
      box-sizing: border-box;
      padding: 20px 0;
      border-bottom: solid 1px #1f3e5a;
      display: flex;
      justify-content: space-between;
      .sinister {
        display: flex;
        flex-flow: column;
        justify-content: space-around;
        .account {
          display: flex;
          justify-content: flex-start;
          align-items: center;
          font-size: 14px;
          color: #42b6f6;
          .ranking{
              margin-right: 10px;
          }
          div {
            width: 32px;
            height: 18px;
            line-height: 18px;
            text-align: center;
            background-color: #ffc744;
            border-radius: 2px;
            font-size: 10px;
            color: #ffffff;
            margin-left: 10px;
          }
        }
        .type_time {
          font-size: 12px;
          color: #586c86;
          span:nth-child(1) {
            width: 85px;
            display: inline-block;
          }
        }
      }
      .dexte {
        color: #ce3835;
        font-size: 14px;
        display: flex;
        align-items: center;
        margin-right: 20px;
        img {
          width: 15px;
          height: 20px;
          margin-right: 8px;
        }
      }
    }
  }
}
</style>