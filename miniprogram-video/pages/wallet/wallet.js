// pages/wallet/wallet.js
const app = getApp()
const host = app.globalData.host
Page({

  /**
   * 页面的初始数据
   */
  data: {
    money:'',
  },
  //提现
  tixian:function(e){
    console.log(e)
    wx.navigateTo({
      url: '/pages/bank/bank?action=1&money=' + e.currentTarget.dataset.money,
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: host+'/mywallet/?user_id=' + app.globalData.user_id,
      method:'GET',
      success(res){
        console.log(res)
        that.setData({
          money:res.data.wallet.money
        })
      }
    })
  },
  onPullDownRefresh: function () {
    wx.showNavigationBarLoading()
    this.onLoad()
    setTimeout(() => {
      wx.hideNavigationBarLoading()
      wx.stopPullDownRefresh()
    }, 2000);
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