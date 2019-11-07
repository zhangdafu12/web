<template>
  <div class="hello2">
    <div class="add">
      <button @click="onAdd">添加员工</button>
    </div>
    <div class="box">
      <fieldset>
        <legend>共传输102个文件<button class="btn sirebtn" @click="onDelete(11,'all')">删除员工</button></legend>
        <table>
          <tbody>
            <tr v-for="(p,index) in persons" >
            <td> <input type="checkbox"  :value="index" v-model="checkedValue"></input>{{p.name}}</td>
            <td>{{p.post}}</td>
            <td>{{p.phone}}</td>
            <td>
              <button class="btn sonbtn" @click="onDelete(index,'alone')">删除员工</button>
            </td>
          </tr>
          </tbody>
        </table>
      </fieldset>
    </div>
    <div class="content1" v-if="addshow">
      <div class="add_cont">
        <p>添加员工</p>
        <img src="../../assets/remove.png" @click="onAdd">
      </div>
      <div class="add_in">
        <label>姓&#8195;名</label>
        <input type="text" v-model="newStaff.name" class="inp name"><br>
        <label>职&#8195;位</label>
        <select v-model="newStaff.post" class="inp post">
          <option value="">选择</option>
          <option value="设计师">设计师</option>
          <option value="销售">销售</option>
          <option value="设计师">摄影师</option>
        </select><br>
        <label>手机号</label>
        <input type="number" v-model="newStaff.phone" class="inp phone"><br>
        <div class="add-btn">
          <button class="affirm" @click="addNewstaff">确定添加</button>
          <button class="cancel" @click="onAdd">取&#8195;消</button>
        </div>
      </div>
    </div>
    <div class="content1" v-if="delshow">
      <div class="add_cont">
        <p>删除员工</p>
        <img src="../../assets/remove.png" @click="onDelete">
      </div>
      <div class="add_in">
        <div class="del_box">
         <div class="del_info"  v-for="(val,ind) in deleteParams">
          <p class="del1">{{val.name}}</p><br>
          <p>职&#8195;位</p>
          <p class="del">{{val.post}}</p><br>
          <p>手机号</p>
          <p class="del">{{val.phone}}</p><br>
         </div>
        </div>
        <div class="add-btn">
          <button class="affirm" style="background: red;" @click="staffRemove()">确定删除</button>
          <button class="cancel" @click="onDelete(11,cancel)">取&#8195;消</button>
        </div>
      </div>
    </div>
    <div class="shade" v-if="addshow1"></div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        checkedValue:[],//一定必须是数组不能是字符串
        answer:[],
        subscript:"",
        addshow:false,
        addshow1:false,
        delshow:false,
        persons:[
          {name:"西门吹雪", post:"设计师", phone:"15078950533"},
          {name:"常德帥", post:"销售", phone:"15878950533"},
          {name:"尤幼倩", post:"设计师", phone:"15078950533"},
          {name:"董得多", post:"设计师", phone:"15078950533"}
        ],
        newStaff:{name:'', post:'', phone:''},
        deleteParams:[],
      }

    },
    methods:{
      onclear: function(){
        this.$router.push({
          name:'clear'
        })
      },
      onAdd: function() {
        this.addshow = !this.addshow;
        this.addshow1 = !this.addshow1;
      },
      onDelete: function(i,num) {
        let _this=this;

        _this.deleteParams=[];
        _this.subscript="";



        if (num=="all"){
          if(_this.answer.length < 1){
            alert("请选择删除人员");
            return
          }
          for(let j=0;j< _this.answer.length;++j){
            _this.deleteParams.push(_this.persons[j]);
          }

        }else if(num=="alone"){
          _this.deleteParams.push(_this.persons[i]);
          _this.subscript=i;

        }else {

          // alert("取消")
        }
        _this.delshow = !_this.delshow;
        _this.addshow1 = !_this.addshow1;

      },
      addNewstaff: function () {
        if(this.newStaff.name === ''){
          alert('姓名不能为空哦');
          return;
        }
        if(this.newStaff.phone <= 0){
          alert('手机号不能为空');
          return;
        }
        this.persons.push(this.newStaff);
        this.newStaff = {name:'', post:'', phone:''}
        this.addshow = !this.addshow;
        this.addshow1 = !this.addshow1;
      },
      staffRemove() {
        let _this=this;
        if (_this.subscript!==""){
          console.log( _this.subscript)
          _this.persons.splice(_this.subscript,1);
          _this.subscript="";
        }else {
          let arr=_this.persons;


          for(let j=0;j< _this.answer.length;++j){
            delete arr[_this.answer[j]];

          }
          _this.persons=[];
          for(let j=0;j<arr.length;++j){
           if (arr[j]) {
             _this.persons.push(arr[j])
           }
          }
          _this.checkedValue=[];

        }
        this.delshow = !this.delshow;
        this.addshow1 = !this.addshow1;
      },

    },
    watch:{
      checkedValue:function(new_v,old_v){
        this.answer=this.checkedValue;
        console.log(this.answer)
        console.log(this.checkedValue)

      }
    },
  }

</script>

<style scoped>
  *{
    box-sizing:border-box;
  }

  p{
    margin: 0;
    padding: 0;
  }
  .hello2{
    position: relative;
    width: 100%;
  }
  .shade{
    width: 100%;
    height: 877px;
    background-color: #000000;
    opacity: 0.35;
    position: absolute;
    top:0;
    left: 0;
    z-index: 100;
  }
  .add{
    /*width: 100%;*/
    height: 76px;
    border-bottom: solid 1px #e0e0e0;
    line-height: 76px;
    padding: 0 40px;
  }
  .add button{
    width: 100px;
    height: 36px;
    background-color: #3d97ff;
    border-radius: 5px;
    border: 0;
    color: #ffffff;
    font-size: 15px;
    outline: none;
  }
  .box{
    /*width: 100%;*/
    padding: 40px 40px 0 40px;
  }
  fieldset{
    border: none;
    margin: 0;
    padding: 0;
  }
  legend{
    width: 100%;
    height: 54px;
    background-color: #f0f0f0;
    line-height: 54px;
    padding: 0 16px;
    font-weight: 600;
    font-size: 17px;
  }
  .btn{
    border: none;
    background: none;
    color: #5b5b5b;
    font-size: 15px;
    outline: none;
  }
  .sirebtn{
    color: #3d97ff;
    margin-left: 15px;
  }
  .sonbtn:hover{
    color:#3d97ff;
  }
  table,tbody{
    width: 100%;
  }
  tr{
    height: 54px;
    line-height: 54px;
    display: flex;
    justify-content: space-between;
    border-bottom:solid 1px #e9e9e9;
    color: #9b9b9b;
    font-size: 12px;
  }
  tr td{
    width: 30%;

  }
  tr td:first-child{
    margin-left: 10px;
    color: #000;
    font-size: 14px;
  }
  tr td:last-child{
    width:6%;
  }
  .content1{
    width: 800px;
    height: 400px;
    background-color: #fff;
    border-radius: 5px;
    position: absolute;
    top:25%;
    left: calc(50% - 400px);
    z-index: 200;
  }
  .add_cont{
    width: 100%;
    height: 77px;
    line-height: 77px;
    border-bottom: solid 1px #e0e0e0;
    padding: 0 23px;
    position: relative;
  }
  .add_cont img{
    width: 15px;
    height: 16px;
    position: absolute;
    right: 23px;
    top:23px;
  }
  .add_in{
    width: 100%;
    height: 323px;
    padding: 20px 23px 0 23px;
    position: relative;
  }
  .add_in:after {
    clear:both;
    content:'';
    display:block;
    width:0;
    height:0;
    visibility:hidden;
  }
  .add_in .del_box{
    width: 100%;
    height: 230px;
    overflow-y: auto;
    overflow-x: hidden;
  }
  ::-webkit-scrollbar
  {display:none}
  .add_in .del_info{
   float: left;
    margin-right: 60px;
    margin-top: 20px;

  }

  .add_in label{
    font-size: 15px;
    color: #323232;
    margin-right: 5px;
  }
  .add_in .inp{
    width: 120px;
    height: 36px;
    background-color: #f0f0f0;
    border-radius: 5px;
    border: none;
    margin-bottom: 15px;
    outline: none;
    padding-left: 15px;
  }
  .post{
    text-align: center;
  }
  .add-btn{
    width: 100%;
    text-align: center;
    position: absolute;
    bottom: 30px;
  }
  .cancel,.affirm{
    width: 100px;
    height: 36px;
    background-color: #3d97ff;
    border-radius: 5px;
    border: none;
    outline: none;
    color: #ffffff;
  }
  .cancel{
    background-color: #9b9b9b;
    margin-left: 10px;
  }
  .add_in p{
    display: inline-block;
    font-size: 15px;
    margin-bottom: 15px;
    padding-left: 10px;
  }
  .del{
    width: 120px;
    height: 36px;
    line-height: 36px;
    background-color: #f0f0f0;
    margin-bottom: 15px;
    padding-left: 15px;
    border-radius: 5px;
  }
</style>
