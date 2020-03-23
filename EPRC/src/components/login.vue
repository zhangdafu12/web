<template>
  <div class="login">
    <p>登录</p>
    <input type="text" placeholder="手机号" v-model="phone" />
    <div class="login_code">
      <input type="text" placeholder="验证码" v-model="code" />
      <div class="send_code">
        <span v-if="!isSend" @click="send_code">{{sendCode}}</span>
        <span v-else>已发送{{code_time}}s</span>
      </div>
    </div>
    <button class="submit" @click="login">注册/登录</button>
  </div>
</template>

<script>
import { login, sendCode } from "../api/api";
import { Message, Loading } from "element-ui";
export default {
  data() {
    return {
      phone: "", //手机号
      code: "",
      isSend: false, //是否已发送验证码
      sendCode: "发送验证码",
      code_time: 59,
      query: ""
    };
  },
  mounted() {
    let url = this.$route.query;
    console.log(url.redirect);
    this.query = url.redirect;
  },
  methods: {
    //验证码发送
    send_code() {
      let that = this;
      if (!/^1[3456789]\d{9}$/.test(that.phone)) {
        Message({
          message: "手机号码有误，请重填",
          duration: 1000,
          type: "warning"
        });
        return false;
      } else {
        sendCode({
          tel: that.phone
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
    //注册登录
    login() {
      let that = this;
      let list = [that.phone, that.code];
      if (!/^1[3456789]\d{9}$/.test(that.phone)) {
        Message({
          message: "手机号码有误，请重填",
          duration: 1000,
          type: "warning"
        });
        return false;
      } else if (that.code.length != 6) {
        Message({
          message: "验证码格式错误，请重填",
          duration: 1000,
          type: "warning"
        });
        return false;
      } else {
        login({
          tel: that.phone,
          code: that.code
        }).then(res => {
          console.log(res);

          if (res.code == 402) {
            Message({
              message: "验证码过期，请重填",
              duration: 1000,
              type: "warning"
            });
          } else {
            window.localStorage.setItem("token", res.token);
            window.localStorage.setItem("user_id", res.user_id);
            window.localStorage.setItem("tel", res.tel);
            window.localStorage.setItem("user_name", res.user_name);
            window.localStorage.setItem("icon", res.icon);
            that.$store.commit("changeLoginState", true);
            that.$store.commit("changeIndexNum", 0);
                 that.$store.commit("changeMineTab", 0);
        that.$store.commit("changeIndexTab", "公链交易量top10");
        that.$store.commit("changeActiveIndex", 1);
        that.$store.commit("queryIndex", 0);
        that.$store.commit("changeQueryTitle", '单一账户查询');
           that.$store.commit('changeUserInfoUsername', res.user_name)
             that.$store.commit('changeUserInfoIcon',res.icon)
              that.$store.commit('changeUserInfoTel',res.tel)
            if (!that.query) {
              that.$router.push({
                path: "/"
              });
            } else {
              that.$router.push({
                path: that.query
              });
            }
          }
        });
      }
    }
  }
};
</script>

<style lang="less">
p {
  margin: 0;
  padding: 0;
}
.login {
  width: 322px;
  height: 48px;
  margin: 230px auto;
  p {
    margin-bottom: 35px;
    font-size: 16px;
    color: #42b6f6;
    text-align: center;
  }
  input {
    width: 322px;
    height: 48px;
    background-color: #192c44;
    border-radius: 5px;
    border: none;
    padding: 0 15px;
    box-sizing: border-box;
    color: #fff;
    font-size: 14px;
    margin-bottom: 15px;
  }
  ::placeholder {
    font-size: 14px;
    color: #42b6f6;
  }
  .login_code {
    display: flex;
    input {
      width: 242px;
      margin-bottom: 40px;
    }
    .send_code {
      width: 80px;
      height: 48px;
      line-height: 48px;
      font-size: 14px;
      color: #42b6f6;
      text-align: right;
    }
  }
  button {
    width: 322px;
    height: 48px;
    background-color: #00ce7d;
    border-radius: 5px;
    border: none;
    font-size: 14px;
    color: #ffffff;
  }
}
</style>
