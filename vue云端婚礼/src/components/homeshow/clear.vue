<template>
    <div class="list-cont">
      <div class="list">共传输102个文件<button class="btn list_btn" @click="onElect">清除记录</button><button class="btn list_btn" @click="onAll">清除全部记录</button></div>
      <table>
        <tbody>
        <tr v-for="(p,index) in persons" >
          <td> <input type="checkbox" :value="index" v-model="checkedIds"></input><img src="../../assets/技术文档.png">{{p.type}}</td>
          <td>{{p.omen}}</td>
          <td>{{p.time}}</td>
          <td>{{p.upload}}</td>
          <td>{{p.finish}}</td>
          <td>{{p.record}}</td>
          <td>
            <button class="btn clear_btn" @click="onCancel(index)">清除记录</button>
          </td>
          <td>
            <img src="../../assets/search.png">
          </td>
        </tr>
        </tbody>
      </table>
    </div>
</template>

<script>
  var persons =[
    {id:0, type:"新娘.jpg",omen:"15.4M", time:"2019/06/12 14:22:01", upload:"上传人:阿星", finish:"上传完成"},
    {id:1, type:"新娘.jpg",omen:"15.4M", time:"2019/06/12 14:22:01", upload:"上传人:阿星", finish:"上传99%"},
    {id:2, type:"新娘.jpg",omen:"15.4M", time:"2019/06/12 14:22:01", upload:"上传人:阿星", finish:"上传完成"},
    {id:3, type:"新娘.jpg",omen:"15.4M", time:"2019/06/12 14:22:01", upload:"上传人:阿星", finish:"上传12%"},
  ];
    export default {
        name: "clear",
        data(){
          return{
            persons:persons,
            checkedIds:[],
          }
        },
      methods:{
        onCancel: function (index) {
          this.persons.splice(index,1);
        },

        onElect: function () {
          var arr = [];
          var len = this.persons.length;
          for(var i=0;i<len;i++){
            if(this.checkedIds.indexOf(i)>=0){
            }else {
              arr.push(persons[i]);
            }
          }
          this.persons = arr;
          this.checkedIds = [];
        },
        onAll: function () {
          this.persons.splice(persons);
          // return []
        }
      }

    }

</script>

<style scoped>
  *{
    box-sizing: border-box;
  }
 .list-cont button{
    margin: 0;
    padding: 0;
  }
  .list-cont{
    padding: 40px 40px 0 40px;
  }
  .list-cont .list{
    width: 100%;
    height: 54px;
    background-color: #f0f0f0;
    line-height: 54px;
    padding: 0 16px;
    font-weight: 600;
    font-size: 17px;
  }
  .list-cont .btn{
    border: none;
    background: none;
    color: #5b5b5b;
    font-size: 15px;
    outline: none;

  }
  .list-cont .list_btn{
    margin-left: 20px;
  }
  .list-cont .list_btn:last-child{
    color: #3d97ff;
  }
  .list-cont .clear_btn:hover{
    color:#3d97ff;
  }
  .list-cont table,tbody{
    width: 100%;
  }
  .list-cont tr{
    height: 54px;
    line-height: 54px;
    display: flex;
    justify-content: space-between;
    border-bottom:solid 1px #e9e9e9;
    color: #9b9b9b;
    font-size: 12px;
  }
  .list-cont tr td:first-child{
    margin-left: 10px;
    color: #000;
    font-size: 14px;
  }
  .list-cont tr td:first-child img{
    width: 19px;
    height: 22px;
    margin: 0 10px;
  }

</style>
