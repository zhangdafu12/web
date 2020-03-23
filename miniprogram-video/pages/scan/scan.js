// pages/scan/scan.js
import {
  Activity,
} from "../../utils/api.js"

const app = getApp()


Page({
  /**
   * 页面的初始数据
   */

  data: {
    imagePaths: ["/images/share_bg2.jpg"],
    indicatorDots: true,
    autoplay: true,
    interval: 5000,
    duration: 1000,
    circular: true,
    beforeColor: "white",
    afterColor: "#3bb1ff",
    result:'',
    windowHeight: 0,
    contentHeight:0,
    share_user_id:'',
    backprice:'',
    price_deposit:'',
  },

  /**
   * 生命周期函数--监听页面加载
   */

  onLoad: function (options) {
    if (wx.getStorageSync('userid')) {
      var that = this
      console.log(options)
      // 计算 scrollView 高度，scrollView 无法用 flex: 1 撑满页面
      const res = wx.getSystemInfoSync()
      const windowHeight = res.windowHeight;//窗口可视高
      const statusBarHeight = res.statusBarHeight
      let query = wx.createSelectorQuery().in(this);
      if(options.flag=='1'){
        var scene = options.scene.replace(',','&')
        console.log(scene)
      }else{
        var scene = decodeURIComponent(options.scene)
      }
      let activity_id = scene.split("&")[0];
      console.log(activity_id)
      console.log(scene,1111)
      let user_id = scene.split('&')[1];
      query.select('.navbar').boundingClientRect(); // 查询头部导航栏
      query.exec((res) => {
        let navbarHeight = res[0].height;
        let contentHeight = windowHeight - statusBarHeight - navbarHeight;
        that.setData({
          windowHeight,
          statusBarHeight,
          contentHeight
        })
      });

      //..........
      // const activity_id = decodeURIComponent(options.scene).split("&")[0]
      // const user_id = decodeURIComponent(options.scene).split("&")[1]
      // const activity_id = 149
      // const user_id = 1

      Activity.retrieve(activity_id).then(result => {
        const photo_urls = result.photo_urls
        console.log(result)
        this.data.result = result;
        const activity_price_deposit = parseFloat(result.activity_price_deposit)
        const activity_price_deposit_1 = activity_price_deposit - (activity_price_deposit * 0.006)
        const activity_price_deposit_2 = activity_price_deposit_1 / 2
        const backprice = (activity_price_deposit_2).toFixed(2)
        that.setData({
          imagePaths: result.photo_urls,
          result: result,
          share_user_id: user_id,
          backprice: backprice,
          price_deposit: activity_price_deposit
        })
      })
    }else{
      wx.navigateTo({
        url: '/pages/accredit/accredit',
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

  goback: function () {
    if (this.status == 0) {
      wx.navigateBack({
        delata: 1
      })
    } else {
      wx.switchTab({
        url: '/pages/index/index',
      })
    }

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function (option) {
      console.log(app.globalData.user_id)
      let that = this;
      console.log(that.data.result)
      console.log(option)
    if (option.target.dataset.way=='0'){
      const share_userid = wx.getStorageSync('userid')
    }else{
      const share_userid = '0'
    }
      return {
        title: that.data.result.course_name, // 转发后 所显示的title
        path: '/pages/apply/apply?share_userid=' + wx.getStorageSync('userid') + '&activity_id=' + that.data.result.id, // user_id 发起分享的用户 activity_id：机构的活动id
        success: (res) => {    // 成功后要做的事情
          console.log(111)
          console.log(res.shareTickets[0])
          wx.getShareInfo({
            shareTicket: res.shareTickets[0],
            success: (res) => {
              that.setData({
                isShow: true
              })
              console.log(that.setData.isShow)
            },
            fail: function (res) { console.log(res, 33) },
            complete: function (res) {
              console.log(res, 22)
            }
          })
        },
        fail: function (res) {
          // 分享失败
          console.log(res, 666)
        }
      }
  }
})