const app = getApp()
const host = app.globalData.host
Page({

  /**
   * 页面的初始数据
   */
  data: {
    order_id:'',
    host : app.globalData.host,
    deposit_order:[],
    tail_order:[],
    activity:'',
    ins:false,
  },
  goback: function () {
    wx.navigateBack({
      delata: 1
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
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    console.log(options)
    if(options.to == 'ins'){
      that.setData({
        ins:true
      })
    }
    that.setData({
      order_id: options.order_id,
    })
    wx.request({
      url: host +'/wechatpay/getinfobyorderid/',
      method:'POST',
      data:{
        order_id:that.data.order_id
      },
      success(res){
        console.log(res.data)
        that.setData({
          activity: res.data.activity,
          deposit_order: res.data.deposit_order,
          tail_order: res.data.tail_order
        })
      }
    })
  },
//分享链接
  goShareLink(){
    console.log(111111111111111)
    let that = this
    let activity_id = that.data.activity.activity_id
    let scene = String(activity_id + ',' + app.globalData.user_id)
      wx.navigateTo({
        url: '/pages/scan/scan?flag=1&scene=' + scene,
      })
  },

////支付尾款
  gotopaydepositprice:function(){
    const that =this
    wx.navigateTo({
      url: '/pages/alipay/alipay?activity_id=' + that.data.activity.activity_id + "&apply_record_id=" + that.data.activity.applyrecord_id + "&order_id=" + that.data.activity.order_id + "&flag=" + '0' + "&time=" + that.data.activity.time,
  })
  },

  gotopaytailprice:function() {
    const that = this
    wx.navigateTo({
      url: '/pages/alipay/alipay?activity_id=' + that.data.activity.activity_id + "&apply_record_id=" + that.data.activity.applyrecord_id + "&order_id=" + that.data.activity.order_id + "&flag=" + '1' + "&time=" + that.data.activity.time,
    })
  },

  /**
   * 跳转核销
   */
  onHandleOrder: function () {
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