// pages/apply/apply.js
const app = getApp()
const host = app.globalData.host
import {
  Activity,
  ApplyRecord,
} from '../../utils/api'


Page({
  /**
   * 页面的初始数据
   */
  data: {
    statusBarHeight: '',
    contentHeight: '',
    imgUrls: [
      "/images/print.jpg",
      'https://images.unsplash.com/photo-1551214012-84f95e060dee?w=640',
      'https://images.unsplash.com/photo-1551446591-142875a901a1?w=640'
    ],
    indicatorDots: true,
    autoplay: false,
    interval: 1000,
    duration: 1000,
    circular: true,
    beforeColor: "white",
    afterColor: "#3bb1ff",
    remainPlaces: "", // 剩余名额
    courseName: "", // 活动课程名称
    deposit: "", // 定金
    activityPriceDeposit: "", // 活动价定金
    all_in_cost:'',//总价
    remainFee: "", // 剩余费用
    activityId: "",
    shareUserId: "",

    status: 1, //进入方式
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    const res = wx.getSystemInfoSync()
    const windowHeight = res.windowHeight
    const statusBarHeight = res.statusBarHeight
    console.log(options.status)
    this.status = options.status;
    let query = wx.createSelectorQuery().in(this);
    query.select('.navbar').boundingClientRect(); // 查询头部导航栏getUserInfo
    query.exec((res) => {
      let navbarHeight = res[0].height;
      let contentHeight = windowHeight - statusBarHeight - navbarHeight;
      this.setData({
        statusBarHeight,
        contentHeight
      });
    });
    if (!app.globalData.user_id) {
      const token = wx.getStorageSync('token')
      if (!token) {
        console.dir('无 token，尝试登陆')
        app.loginedCallback = () => {
          // 登陆后回调，加载用户信息
          this.getUserInfo()
          app.checkToken()
        }
        app.login()
      } else {
        console.log('存在 token：', token)
        // 判断 token 是否有效
        app.checkToken()
      }
      this.getUserInfo()
    }
    var activity_id = options.activity_id
    // var user_id = 70
    // var activity_id = 240

    console.log(activity_id)
    if (activity_id) {
      Activity.retrieve(activity_id).then(result => {
        console.log(result)
        console.log(parseFloat(result.all_in_cost))
        console.log(parseFloat(parseFloat(result.deposit)))
        console.log(parseFloat(result.all_in_cost) - parseFloat(result.deposit).toFixed(2))
        this.setData({
          all_in_cost: result.all_in_cost,
          remainPlaces: result.remain_place,
          courseName: result.course_name,
          deposit: result.deposit,
          activityPriceDeposit: result.activity_price_deposit,
          remainFee: (parseFloat(result.all_in_cost) - parseFloat(result.deposit)).toFixed(2),
          activityId: options.activity_id,
          shareUserId: options.share_userid,
          imgUrls: result.photo_urls,
        })
      })
    } else {
      console.log('111111111111111111111111')
      wx.switchTab({
        url: '/pages/index/index',
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

  getUserInfo: function() {
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          wx.getUserInfo({
            lang: "zh_CN",
            success: res => {
              app.globalData.userInfo = res.userInfo
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

  goback: function() {
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
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function(options) {
    console.log(wx.getLaunchOptionsSync())
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

  saveForm:function(e){
    var that = this
    const student_name = e.detail.value.name
    const student_age = e.detail.value.age
    const phone = e.detail.value.phone
    if(!student_name){
      wx.showModal({
        title: '提示',
        content: '请填写姓名',
      })
    }else if(!student_age){
      wx.showModal({
        title: '提示',
        content: '请填写年龄',
      })
    }else if(!phone){
      wx.showModal({
        title: '提示',
        content: '请填写联系方式',
      })
    }else{
      console.log(that.data.activityId)
      console.log(wx.getStorageSync('userid'))
      if (wx.getStorageSync('userid')) {
        wx.request({
          url: host+'/activites/activityview/',
          method: 'post',
          data: {
            "student_name": e.detail.value.name,
            "student_age": e.detail.value.age,
            "phone": e.detail.value.phone,
            "activity_id": that.data.activityId,
            // "activity": '240',
            "shareUserId": that.data.shareUserId,
            "user_id": wx.getStorageSync('userid'),
            // "user": '71',
          }, success(res) {
            console.log(res.data)
            if (res.data.status == 203) {
              wx.showToast({
                title: '抱歉，您已经申请过了!',
                icon: 'none',
                duration: 1000,
              })
              setTimeout(function () {
                wx.navigateTo({
                  url: '/pages/order/order?flag=0',
                })
              }, 1000)
            } else if (res.data.status == 200) {
              console.log('111111111111111111111111111111111222222222222222222222')
              var time = res.data.appyrecord.datetime
              var applyrecord_id = res.data.appyrecord.id
              console.log(time)
              var orderid = ''
              const openid = wx.getStorageSync('openid')
              wx.request({
                url: host+'/wechatpay/signup_order/',
                method: 'post',
                data: {
                  'openid': openid,
                  "activity": that.data.activityId,
                  'share_userid': that.data.shareUserId
                },
                success: function (res) {
                  console.log(res)
                  orderid = res.data.orderid
                  // console.log(res)

                    wx.navigateTo({
                      url: '/pages/alipay/alipay?activity_id=' + that.data.activityId + "&apply_record_id=" + applyrecord_id + "&order_id=" + orderid + "&flag=" + '0' + "&time=" + time,
                      // url: '/pages/alipay/alipay?activity_id=' + "1" + "&time=" + time,
                    })
                  

                }, fail(res) {
                  console.log(res)
                }
              })
            } else if (res.data.status == 202) {
              console.log(res.data)
            }
          }, fail(res) {
            console.log(res)
          }
        })
      } else {
        wx.navigateTo({
          url: '/pages/accredit/accredit'
        })
      }
    }
    
  },



  changeName: function(e) {
    console.log(e.detail.value, e.currentTarget.dataset.index)
    let index = e.currentTarget.dataset.index;
    let val = e.detail.value;
    if (index == 0) {
      this.setData({
        valueTotal: val
      })
    } else if (index == 1) {
      this.setData({
        valueTotal: val
      })
    } else {
      this.setData({
        valueTotal: val
      })
    }

  },
})