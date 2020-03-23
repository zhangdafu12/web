<template>
  <div class="amend">
    <div class="title">
      <span>{{isShow==0?'信息修改':'手机号修改'}}</span>
      <span class="back" v-show="isShow==1" @click="ONback">返回上一级</span>
    </div>
    <div class="box_cont">
      <div class="amend_cont" v-show="isShow==0">
        <div class="amend_mage">
          <div class="define_cont define_user">
            <span class="define">用户名</span>
            <div class="username">
              <input
                type="text"
                rel="username"
                v-model="user_name"
                :placeholder="username"
                class="message"
              />
            </div>
            <span class="alter" @click="onSave ">保存</span>
          </div>
          <div class="define_cont">
            <span class="define">手机号</span>
            <span class="message">{{tel}}</span>
            <span class="alter" @click="changeNumber">修改</span>
          </div>
          <div class="define_cont">
            <span class="define">微信绑定</span>
            <span class="message">阿星</span>
            <span class="alter">解绑</span>
          </div>
        </div>
        <div class="amend_img">
          <img :src="amendImg" alt />
          <div class="alter_img">
            <span>修改头像</span>
            <input type="file" @change="amendFile" ref="amendFile" />
          </div>
        </div>
      </div>
      <div class="changeNumber_cont" v-show="isShow==1">
        <label for>旧手机号</label>
        <input type="text" :placeholder="tel" v-model="oldNumber" />
        <br />
        <label for>新手机号</label>
        <input type="text" placeholder v-model="newNumber" />
        <br />
        <input type="text" class="codeInt" v-model="code" />
        <label for class="code" v-if="!isSend" @click="send_code">发送验证码</label>
        <label for class="code" v-else>验证码已发送{{code_time}}s</label>
        <br />
        <button @click="confirm">确认</button>
      </div>
    </div>
  </div>
</template>

<script>
import { changename, changetel, icon, sendCode } from "../../api/api";
import { Message, Loading } from "element-ui";
export default {
  data() {
    return {
      isShow: 0, //0:个人信息 1：修改手机号
      name: "",
      isSend: false, //
      code_time: "59",
      oldNumber: "", //老手机号
      newNumber: "", //新手机号
      code: "", //验证码,
      user_name: ""
    };
  },
  computed: {
    username: {
      get: function() {
        if (this.$store.state.userInfo.username) {
          return this.$store.state.userInfo.username;
        } else {
          return this.$store.state.userInfo.tel;
        }
      },
      set: function() {}
    },
    amendImg: {
      get: function() {
        return this.$store.state.userInfo.icon;
      },
      set: function() {}
    },

    tel: {
      get: function() {
        return this.$store.state.userInfo.tel;
      },
      set: function() {}
    }
  },
  created() {},
  methods: {
    //保存昵称
    onSave() {
      let that = this;
      changename({
        user_id: window.localStorage.getItem("user_id"),
        user_name: this.user_name
      }).then(res => {
        that.$store.commit("changeUserInfoUsername", this.user_name);
      });
    },
    //修改头像
    amendFile(e) {
      let that = this;
      let config = {
        headers: { "Content-Type": "multipart/form-data" }
      };
      let file = e.target.files[0];
      let fileReader = new FileReader();
      fileReader.readAsDataURL(file);
      fileReader.onload = e => {
        // console.log(fileReader.result)
      };
      let param = new FormData(); //创建form对象changeIcon
      param.append("icon", file); //通过append向form对象添加数据
      param.append("user_id", window.localStorage.getItem("user_id"));
      icon(param, config).then(res => {
        console.log(res.icon);
        localStorage.setItem("icon", res.icon);
        that.$store.commit("changeUserInfoIcon", res.icon);
        console.log(this.$store.state.userInfo.icon);
      });
    },
   
    //修改手机号按钮
    changeNumber() {
      this.isShow = 1;
    },
    //返回上一级
    ONback() {
      this.isShow = 0;
    },
    //验证码发送
    send_code() {
      let that = this;
      if (
        !/^1[3456789]\d{9}$/.test(that.newNumber) &&
        !/^1[3456789]\d{9}$/.test(that.oldNumber)
      ) {
        Message({
          message: "请输入Z正确手机号码",
          duration: 1000,
          type: "warning"
        });
        return false;
      } else {
        sendCode({
          tel: that.newNumber
        }).then(res => {
          console.log(res);
          that.setTime = setInterval(function() {
            that.isSend = true;
            if (that.code_time <= 1) {
              that.code_time = 59;
              that.sendCode = "重新发送";
              that.isSend = false;
              clearInterval(that.setTime);
            } else {
              that.code_time--;
            }
          }, 1000);
        });
      }
    },
    //确定修改
    confirm() {
      let that = this;
      let list = [that.oldNumber, that.newNumber, that.code];
      this.isShow = 0;
      changetel({
        // user_id:window.localStorage.getItem('user_id'),
        tel: that.oldNumber,
        new_tel: that.newNumber,
        code: that.code
      }).then(res => {
        that.$store.commit("changeUserInfoTel", that.newNumber);
        localStorage.setItem("tel", that.newNumber);
      });
    }
  }
};
</script>


<style lang="less">
.amend {
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
    font-size: 18px;
    color: #ffffff;
    display: flex;
    justify-content: space-between;
    span {
      margin: 0 20px 0 10px;
    }
    .back {
      font-size: 14px;
      color: #42b6f6;
    }
  }
  .box_cont {
    width: 100%;
    height: 606px;
    box-sizing: border-box;
    padding: 45px 20px;
    .amend_cont {
      display: flex;
      justify-content: flex-start;
      span {
        display: inline-block;
      }
      .define_cont {
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        .define {
          width: 56px;

          font-size: 12px;
          color: #586c86;
        }
        .message {
          font-size: 14px;
          color: #42b6f6;
          padding: 0 20px 0 10px;
          box-sizing: border-box;
        }
        .alter {
          font-size: 12px;
          color: #00ce7d;
        }
      }
      .define_user {
        height: 40px;
        font-size: 14px;
        .username {
          width: 140px;
          height: 40px;
          margin-right: 20px;
          position: relative;
          input.message {
            width: 140px;
            height: 40px;
            background-color: #101b2d;
            border-radius: 5px;
            outline: none;
            border: none;
            color: #42b6f6;
            padding: 0 10px;
          }
        }
      }
      .amend_img {
        width: 80px;
        margin-left: 100px;
        text-align: center;
        img {
          width: 80px;
          height: 80px;
          border-radius: 50%;
          margin-bottom: 5px;
        }
        .alter_img {
          width: 48px;
          height: 18px;
          font-size: 12px;
          color: #00ce7d;
          position: relative;
          margin: 0 auto;
          input {
            width: 48px;
            height: 18px;
            position: absolute;
            top: 0;
            left: calc(50% - 24px);
            opacity: 0;
          }
        }
      }
    }
    .changeNumber_cont {
      input {
        width: 160px;
        height: 40px;
        background-color: #101b2d;
        border-radius: 5px;
        border: none;
        text-indent: 12px;
        margin-bottom: 20px;
        font-size: 14px;
        color: #42b6f6;
      }
      .codeInt {
        width: 90px;
      }
      ::placeholder {
        color: #42b6f6;
      }
      label {
        font-size: 12px;
        color: #586c86;
        margin-right: 10px;
      }
      .code {
        margin-left: 10px;
        color: #42b6f6;
      }
      button {
        width: 123px;
        height: 34px;
        background-color: #ff8a24;
        border-radius: 5px;
        border: none;
        outline: none;
        font-size: 14px;
        color: #ffffff;
        margin-top: 10px;
      }
    }
  }
}
</style>