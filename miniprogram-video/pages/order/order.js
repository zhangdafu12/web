// pages/order/order.js
import {
  Order
} from '../../utils/api'

const app = getApp()
const host = app.globalData.host
Page({

  /**
   * 页面的初始数据
   */
  data: {
    data_list:[],
    flag:'',
    order_list:[],
    host : app.globalData.host
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    var flag=options.flag
    var user_id = app.globalData.user_id
    console.log(app.globalData)
    console.log(user_id)
    var insid = app.globalData.institution_id
    // var user_id = 1
    var that = this
    that.setData({
      flag:flag
    })
    const data = {
      'user_id':user_id
      // 'user_id': 1
    }
    if(flag=='0'){
      wx.request({
        url: host + '/wechatpay/alluserorder/',
        method:'POST',
        data: data,
        success(res){
          console.log(res)
          that.setData({
            order_list: res.data.order
          })

        }
      })
    }if(flag=='1'){
      wx.request({
        url: host+'/wechatpay/allinsorder/',
        method:'POST',
        data:{
          'insid':insid
        },
        success(res){
          console.log(res.data)
          that.setData({
            order_list: res.data.order
          })
        }
      })
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

  re_order:function(event){
    const activity_id = event.target.dataset.activity_id
    wx.navigateTo({
      // url: '../bargain/bargain?id=' + e.currentTarget.dataset.id + "&flag=" + e.currentTarget.dataset.flag + "&bargain=" + e.currentTarget.dataset.bargain,
      // url: '/pages/apply/apply?user_id='+app.globalData.user_id+'&activity_id=' + activity_id,
      url: '/pages/apply/apply?user_id=' + '1' + '&activity_id=' + activity_id,
    })
  },

  to_pay:function(res){
    const activity_id = res.target.dataset.activity_id
    const order_id = res.target.dataset.order_id
    const applyrecord_id = res.target.dataset.applyrecord_id
    const flag=res.target.dataset.flag
    wx.navigateTo({
      url: '/pages/alipay/alipay?activity_id=' + activity_id + "&apply_record_id=" + applyrecord_id + "&order_id=" + order_id + "&flag=" + flag,
      // url: '/pages/alipay/alipay?activity_id=' + "1" + "&time=" + time,
    })
  },

  lookinfo:function(){

  },

  onParticulars:function(res){
    const order_id = res.target.dataset.order_id
    console.log(order_id)
    wx.navigateTo({
      url: '/pages/particulars/particulars?orderid=' + order_id,
    })
  },

  oninsorder:function(e){
    console.log(e)
    var that = this
    const order_id = e.currentTarget.dataset.order_id
    if(that.data.flag=='1'){
      wx.navigateTo({
        url: '/pages/orderInfo/orderInfo?order_id=' + order_id + '&to=ins'
      })
    }else{
      wx.navigateTo({
        url: '/pages/orderInfo/orderInfo?order_id=' + order_id
      })
    }

  }
  
})