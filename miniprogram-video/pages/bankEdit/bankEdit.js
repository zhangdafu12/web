// pages/bankEdit/bankEdit.js
const app = getApp()
const host = app.globalData.host
Page({
  /**
   * 页面的初始数据
   */

  data: {
    isSave: false,
    info:[],
    num:'',
    name:'',
    address:'',
    bid:'',

  },
  onPullDownRefresh: function () {
    wx.showNavigationBarLoading()
    this.onLoad()
    setTimeout(() => {
      wx.hideNavigationBarLoading()
      wx.stopPullDownRefresh()
    }, 2000);
  },
  num:function(e){
    var that = this
    console.log(e)
    that.setData({
      num: e.detail.value
    })
    console.log(that.data.num)
  },
  name: function (e) {
    var that = this
    console.log(e)
    that.setData({
      name: e.detail.value
    })
    console.log(that.data.num)
  },
  address: function (e) {
    var that = this
    console.log(e)
    that.setData({
      address: e.detail.value
    })
    console.log(that.data.num)
  },



  saveBank:function(){
    var that = this
    wx.request({
      url:host+'/addbankcard/',
      method:'POST',
      data:{
        'num':that.data.num,
        'name': that.data.name,
        'address': that.data.address,
        'user_id': app.globalData.user_id
      },
      success(res){
        console.log(res)
        if(res.data.status===200){
          wx.navigateTo({
            url: '/pages/bank/bank?have=yes'
          })
        }else if(res.data.status===202){
          console.log('112312312313123123123')
          wx.showToast({
            title: '请确认卡号',
            icon: 'none',
            duration: 2000
          })
        }else if(res.data.status==203){
          wx.showToast({
            title: '只允许绑定一张',
            icon: 'none',
            duration: 2000
          })
        }

      }
    })

  },

  changeBank:function(){
    var that = this
    const num = that.data.num
    const name = that.data.name
    const address = that.data.address
    const bid = that.data.bid
    wx.request({
      url: host+'/changebank/',
      method:'POST',
      data:{
        'num':num,
        'name':name,
        'address':address,
        'bid':bid
      },
      success(res) {
        console.log(res)
        if (res.data.status === 200) {
          wx.navigateTo({
            url: '/pages/bank/bank?have=yes'
          })
        } if (res.data.status === 202) {
          wx.showToast({
            title: '请确认卡号',
            icon: 'none',
            duration: 2000
          })
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
if(options.have=="yes"){
  this.setData({
    isSave:true,
    num: options.num,
    name: options.name,
    address: options.address,
    bid:options.bid
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