
import {
  Token
} from 'utils/api'

App({
  // 全局数据
  
  globalData: {
    userInfo: null,
    institution_id: null,
    user_id: null,
    // host:'http://192.168.3.199:8000',
    // host: 'http://192.168.3.43:8000',
    host: 'https://www.heiyunworld.com:8800'
  },
  // 应用加载
  onLaunch: function () {

  },
  // 登陆
  
  login: function () {
    wx.login({
      success: res => {
        // console.log(this.loginedCallback)
        // 获取 Token
        Token.obtain({
          code: res.code
        }).then(result => {
          const statusCode = result.statusCode
          if (statusCode === 201) { // 登陆成功，存储 Token
            const token = result.data.token
            const openid = result.data.openid
            
            wx.setStorage({
              key: 'token',
              data: token
            })
            wx.setStorage({
              key: 'openid',
              data: openid
            })
            var open_id = {
              'openId': openid
            }
            wx.request({
              url: this.globalData.host+'/getuserbyopenid/',
              // url: 'http://192.168.3.135:8000/getuserbyopenid/',
              header: {
                'Content-Type': 'application/x-www-form-urlencoded'
              },
              method: "POST",
              dataType: 'json',
              data: open_id,
              success: function (res) {
                console.log(res)
                wx.setStorage({
                  key: 'userid',
                  data: res.data.user_id,
                })
              },
              fail: function (res) {
                console.log(res)
              }
            })
            
            if (this.loginedCallback) {
              this.loginedCallback(result)
            }
          } else if (statusCode === 401) { // 尚未注册，跳转至注册页面
            wx.navigateTo({
              url: '/pages/register/register',
            })
          } else { // 提示错误信息
            wx.showToast({
              title: result.data.text,
              icon: 'none',
              duration: 2000
            })
          }
        })
      }
    })
  },
  // 检查 Token
  checkToken: function () {
    Token.check().then(result => {
      this.globalData.user_id = result['user_id']
    })
  }
})