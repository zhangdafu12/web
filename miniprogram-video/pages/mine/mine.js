import {
  Account,
  Token
} from '../../utils/api'

//获取应用实例
const app = getApp()
const host = app.globalData.host

Page({

  /**
   * 页面的初始数据
   */
  data: {
    status:false,
    userInfo: {},
    balance: 0,
    isAdmin: false,
  },
  // 登录按钮
  login:function(){
  wx.navigateTo({
    url: '/pages/accredit/accredit',
  })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log('1234546')
    console.log(app.globalData)
    console.log(wx.getStorageSync('userInfo'))
    if (wx.getStorageSync('userInfo')) {
      this.setData({
        userInfo:wx.getStorageSync('userInfo'),
        
        status:true
      })
      console.log(this.data)
    }
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
    var that=this
    that.onLoad()
    if (wx.getStorageSync('userInfo')){
        this.setData({
          balance: 500
        })
    
      Token.check().then(result => {
        console.log(result)
        app.globalData.user_id = result['user_id']
        if (result && 'institution_id' in result) {
          app.globalData.institution_id = result['institution_id']
          app.globalData.user_id = result['user_id']
          this.setData({
            isAdmin: true,
          })
        }
      })
    }else{
      this.setData({
        balance:0,
        isAdmin: false,
      })
    }

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

  onStudy: function () {
    if (wx.getStorageSync('userInfo')){
      wx.navigateTo({
        url: '/pages/course/course'
      })
    }else{
      wx.navigateTo({
        url: '/pages/accredit/accredit'
      })
    }
    
  },
  Myactivity:function(){
    
    if (wx.getStorageSync('userInfo')) {
      if (app.globalData.institution_id == -1) {
        wx.showModal({
          title: '机构审核中',
          showCancel: false
        })
      }else{
        wx.navigateTo({
          url: '/pages/details/details?insid=' + app.globalData.institution_id + '&flag=1'
        })
      }
    } else {
      wx.navigateTo({
        url: '/pages/accredit/accredit'
      })
    }
  },

  onCheck: function () {
    if (wx.getStorageSync('userInfo')) {
      wx.navigateTo({
        url: '/pages/check/check'
      })
    } else {
      wx.navigateTo({
        url: '/pages/accredit/accredit'
      })
    }
   
  },
  onOrder:function (e) {
    const flag = e.currentTarget.dataset.flag
    if (wx.getStorageSync('userInfo')) {
      wx.navigateTo({
        url: '/pages/order/order?flag=' + flag
      })
    } else {
      wx.navigateTo({
        url: '/pages/accredit/accredit'
      })
    }
  },
  showview: function () {
    this.setData({
      display: "block"
    })
  },
  hideview: function () {
    this.setData({
      display: "none"
    })
  },

  /**
   * 跳转机构配置页面
   */
  goToInstitution: function () {
    if (wx.getStorageSync('userInfo')) {
      if (app.globalData.institution_id == -1) {
        wx.showModal({
          title: '机构审核中',
          showCancel: false
        })
      } else {
        wx.navigateTo({
          url: '/pages/institution/institution',
        })
      }
    } else {
      wx.navigateTo({
        url: '/pages/accredit/accredit'
      })
    }

    
  }
})