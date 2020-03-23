// pages/alipay/alipay.js
const app = getApp()
const host = app.globalData.host
import {
  Activity,
} from "../../utils/api.js"


Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgUrl: "",
    courseName: "",
    deposit: "",//定金
    activityPriceDeposit: "",//定金活动价
    institutionName: "",
    activity_id:"",
    order_id:"",
    clock: '',
    price: '',//定金
    all_in_cost:'',//全款
    last_price:'',
    flag:'',
    deposit_order_id:'',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    var that = this
    var apply_record_id = options.apply_record_id
    var time = new Date(options.time).getTime() + 15 * 60 * 1000
    console.log(time)
    var activity_id = options.activity_id
    var order_id = options.order_id
    console.log(that.data.order_id)
    that.setData({
      order_id:order_id
    })
    var flag = options.flag
    
   
    this.product(time)

    Activity.retrieve(activity_id).then(result => {

      console.log(result)
      this.setData({
        all_in_cost:result.all_in_cost,
        last_price: (parseFloat(result.all_in_cost) - parseFloat(result.deposit)).toFixed(2),
        courseName: result.course_name,
        deposit: result.deposit,
        activityPriceDeposit: result.deposit,
        imgUrl: result.photo_urls[0].photo_url,
        institutionName: result.institution_name,
        activity_id:activity_id,
        order_id:order_id,
        flag:flag,
        price: result.activity_price_deposit


      })
    })
  },

  product: function(endTime) {
    var that = this;
    var interval = setInterval(function() {
      //将时间传如 调用
      var now = new Date().getTime();
      this.setData({ //正常倒计时        
        clock: endTime - now > 0 ? that.convert(endTime - now) : "已结束"
      });
    }.bind(this), 1000);
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function() {

  },



  // 将时间戳转为 倒计时时间
  convert: function(micro_second) {
    var second = micro_second / 1000;
    // 分钟
    var min = Math.floor(second / 60 % 60);
    var minStr = min.toString();
    if (minStr.length == 1) minStr = '0' + minStr;

    // 秒位  
    var sec = Math.floor(second % 60);
    var secStr = sec.toString();
    if (secStr.length == 1) secStr = '0' + secStr;
    return minStr + ":" + secStr;
  },
  onPullDownRefresh: function () {
    wx.showNavigationBarLoading()
    this.onLoad()
    setTimeout(() => {
      wx.hideNavigationBarLoading()
      wx.stopPullDownRefresh()
    }, 2000);
  },


//////////////支付//////////////////
  pay: function () {
    if (wx.getStorageSync('openid')){
      const that = this
      const openid = wx.getStorageSync('openid')
      const order_id = that.data.order_id
      const activity_id = that.data.activity_id
      const flag = that.data.flag
      console.log(activity_id)
      console.log(order_id)
      var that = this
      const header = {}
      var url = ''
      var backurl = ''
      var closeurl=''
      var data={}
      const url1 = host+'/wechatpay/pay/'
      const url2 = host+'/wechatpay/pay_tail/'
      const backurl1 = host+'/wechatpay/payback/'
      // const backurl2 = host+'/wechatpay/tailback/'
      const backurl2 = host+'/wechatpay/tailback/'

      const closeurl1 = host + '/wechatpay/closedepositorder/'
      const closeurl2 = host + '/wechatpay/closetailorder/'
      if (flag == '0') {
        url = url1
        backurl = backurl1
        closeurl = closeurl1

      } else if (flag == '1') {
        url = url2
        backurl = backurl2
        closeurl = closeurl2

      }

      wx.request({
        url: url,
        data : {
          'openid': openid,
          'order_id': order_id,
          'activity_id': activity_id,
        },
        // header: header,
        method: 'post',
        success: function (result) {
          console.log(result)
          that.setData({
            deposit_order_id: result.data.deposit_order_id
          })
          wx.requestPayment({
            timeStamp: result.data.timeStamp,
            nonceStr: result.data.nonceStr,
            package: result.data.package,
            signType: 'MD5',
            paySign: result.data.paySign,
            success: function (result) {
              console.log(result, '1111111111')
              wx.request({
                // header: header,
                method: 'post',
                url: backurl,
                data:{
                  'result':result,
                  'order_id': that.data.deposit_order_id
                },success(res){
                    console.log(res)
                  if (res.data.msg=='SUCCESS'){
                    wx.showModal({
                      title: '支付成功',
                      content: '是否前往订单页',
                      success(res) {
                        if (res.confirm) {
                          console.log('用户点击确定')
                          wx.navigateTo({
                            url: '/pages/order/order?flag=0',
                          })
                        } else if (res.cancel) {
                          console.log('用户点击取消')
                        }
                      }
                    })
                  }
                },fail(res){
                  console.log(res)
                }
              })
            },
            fail: function (result) {
              console.log(result)
              // wx.request({
              //   url: closeurl,
              //   method: 'post',
              //   data: { 'order_id': order_id },

              // })
            }
          })
        }
      })
    // this.setData({
    //   finalPay: false,
    // })
    }else{
      wx.navigateTo({
        url: '/pages/accredit/accredit'
      })
    }
  },
  

})