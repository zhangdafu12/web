// pages/bank/bank.js
const app = getApp()
const host = app.globalData.host
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isHave: false,
    action:0,
    monry:'',
  },
  onPullDownRefresh: function () {
    wx.showNavigationBarLoading()
    this.onLoad()
    setTimeout(() => {
      wx.hideNavigationBarLoading()
      wx.stopPullDownRefresh()
    }, 2000);
  },
  revisionBank: function (e) {
    const num = e.currentTarget.dataset.num
    const name = e.currentTarget.dataset.name
    const address = e.currentTarget.dataset.address
    const bid = e.currentTarget.dataset.bid
    wx.navigateTo({
      url: '/pages/bankEdit/bankEdit?have=yes&num='+num+'&name='+name+'&address='+address+'&bid='+bid
    })
  },
  
  addBank: function () {
    
    wx.navigateTo({
      url: '/pages/bankEdit/bankEdit?have=no'
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    console.log(options.action)
    that.setData({
      money:options.money
    })
    if (options.have == "yes") {
      this.setData({
        isHave: true
      })
    }
    if(options.action==1){
      this.setData({
        action:options.action
      })
    }
    wx.request({
      url: host+'/mybankcard/?user_id=' + app.globalData.user_id,
      method: 'get',
      success(res){
        console.log(res.data)
        that.setData({
          bank:res.data.cards
        })
      }
      })
  },

  choose:function(){
    wx.showModal({
      title: '提示',
      content: '敬请期待',
      success(res) {
        if (res.confirm) {
          console.log('用户点击确定')
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },



  tixian:function(){
    var that = this
    var money = parseFloat(that.data.money)
    console.log(money)
    if (money<1){
      wx.showToast({
        title: '最低提现金额1元',
        icon: 'none',
        duration: 1000
      })
    }else{
      wx.request({
        url: host + '/wechatpay/cash_withdrawal/',
        // url: 'http://192.168.3.30:8000/wechatpay/cash_withdrawal/',

        data: {
          'ins_id': app.globalData.institution_id,
          'money': that.data.money
        },
        method: 'POST',
        success: function (res) {
          if (res.data.status == 200) {
            wx.showToast({
              title: '成功',
              icon: 'success',
              duration: 1000
            })
          } else {
            wx.showToast({
              title: '失败',
              icon: 'none',
              duration: 1000
            })
          }
        },
        fail: function (res) {
          console.log(res)
        },
        complete: function (res) { },
      })
    }

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
    wx.reLaunch({
      url: "/pages/institution/institution",
    })

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