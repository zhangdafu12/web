import {
  register
} from '../../utils/api'

//获取应用实例
const app = getApp()
const host = app.globalData.host

Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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

  },
  bindGetUserInfo: function (e) {
    console.log(e.detail)
    const encryptedData = e.detail.encryptedData
    const iv = e.detail.iv
    wx.login({
      success: res => {
        console.log(res)
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        const code = res.code
        register({
          code,
          encryptedData,
          iv
        }).then(result => {
          console.log(result)
          const statusCode = result.statusCode
          if (statusCode === 201) { // 注册成功
            wx.showToast({
              title: '注册成功',
              icon: 'success'
            })
            app.login()
            app.globalData.userInfo = e.detail.userInfo
            console.log(e.detail)
            console.log(e.detail.userInfo)
            wx.setStorage({
              key: 'userInfo',
              data: e.detail.userInfo,
            })
            
              wx.navigateBack({
                delta: 2,
              })

          } else if (statusCode === 400) { // 注册失败
            wx.showToast({
              title: '用户已注册',
              icon: 'error'
            })
          } else { // 提示错误信息
            wx.showToast({
              title: res.data,
              icon: 'error',
              duration: 2000
            })
          }
        })
      }
    })
  }




})