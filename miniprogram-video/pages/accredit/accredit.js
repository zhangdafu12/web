// pages/accredit/accredit.js
const app = getApp()
const host = app.globalData.host
Page({

  /**
   * 页面的初始数据
   */
  data: {
    showAuthModal:false,
    statusBarHeight: app.globalData.statusBarHeight,
  },

  onPullDownRefresh: function () {
    wx.showNavigationBarLoading()
    this.onLoad()
    setTimeout(() => {
      wx.hideNavigationBarLoading()
      wx.stopPullDownRefresh()
    }, 2000);
  },
//返回上一页
  goback: function () {
    wx.navigateBack({
      delata: 1
    })
  },
  //拒绝授权
  refuse: function () {
    wx.navigateBack({
      delata: 1
    })
  },
  //允许授权
  allowed: function () {
    console.log("调起授权接口,并返回")
    const token = wx.getStorageSync('token')
    const userID = wx.getStorageSync('userID')
    if (!token | !userID) {
      console.log('无 token，尝试登陆')
      app.loginedCallback = () => {
        // 登陆后回调，加载用户信息
        app.checkToken()
        this.getUserInfo()
        // app.checkToken()
        // this.loadData()
      }
      app.login()
    } else {
      console.log('存在 token：', token)
      // 判断 token 是否有效
      app.checkToken()
      this.getUserInfo()
    }
  
  },

   getUserInfo: function () {
    console.log('this is accredit getUserInfo')
    wx.getSetting({
      success: res => {
        console.log(res)
        if (res.authSetting['scope.userInfo']) {
          wx.getUserInfo({
            lang: "zh_CN",
            success: res => {
              console.log('this is accredit wx.getUserInfo success')
              console.log(res)
              wx.setStorage({
                key: 'userInfo',
                data: res.userInfo,
              })
              this.setData({
                showAuthModal: false
              })
            }, fail: function (res) {
              console.log('this is accredit wx.getUserInfo fail')
            }
          })
        } else {
          this.setData({
            showAuthModal: true
          })
        }
      }
    })
  },

  onGotUserInfo: function (e) {
    console.log(e.detail)
    wx.setStorage({
      key: 'userInfo',
      data: e.detail.userInfo,
    })
    this.setData({
      showAuthModal: false
    })
    wx.navigateBack({
      delata: 1
    })
  },



  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // 计算 statusBarHeight 高度
    const res = wx.getSystemInfoSync()
    const statusBarHeight = res.statusBarHeight
    this.setData({
      statusBarHeight,
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})