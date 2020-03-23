import {
  Institution,
  Video,
  Activity
} from '../../utils/api'

//获取应用实例
const app = getApp()
const host = app.globalData.host
Page({

  /**
   * 页面的初始数据
   */
  data: {
    id: null,
    insid:'',
    love: 0,
    host : app.globalData.host,
    info: {
      name: '',
      avatar: '',
      address: '',
      phone: '',
      isCollected: false,
      collect: 0,
      like: 0,
      num:0,
      
    },
    videos: [],
    activitys:'',
    admin:false,
    reload: false // 从播放页面返回时用于判断是否需要刷新数据
  },
  //图片预览
  bigImg(e){
    console.log(e.currentTarget.dataset.src)
    let src = e.currentTarget.dataset.src
    wx.previewImage({
      current: src, // 当前显示图片的http链接
      urls: [src] ,// 需要预览的图片http链接列表
      success(e){
        console.log(e)
      },
      fail(e){
        console.log(e)
      }
    })
  },
  //删除活动弄
  deleteactivity:function(e){
    var that = this
    const aid = e.currentTarget.dataset.aid
    const index = e.currentTarget.dataset.index
    wx.request({
      url: host+'/deleteactivaty/',
      method:'POST',
      data:{
        'aid':aid
      },
      success(res){
        console.log(res)
        if(res.data.status==200){
          that.data.activitys[index].status=false
          that.setData({
            activitys: that.data.activitys
          })
        }
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
   * 加载页面数据
   */
  loadInfo: function () {
    // 加载机构信息
    // Institution.getDetail(
    //   this.data.insid
    //   // 1
    // ).then(detail => {
    //   this.setData({
    //     info: detail
    //   })
    // })


    // 加载机构视频列表
    // Video.list({
    //   institution: this.data.insid
    //   // institution:1
    // }).then(videos => {
    //   this.setData({
    //     videos
    //   })
    // })

    // //机构下的所有课程
    // Activity.retrieve({
    //   id:this.data.insid
    //   // institution:1
    // }).then(activitys => {
    //   console.log(activitys)
    //   this.setData({
    //     activitys: activitys
    //   })
    // })

  },

  // gotoadress:function(){

  // },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that=this
    if(options.flag=='1'){
      that.setData({
        admin:true
      })
    }
    console.log(options)
    this.setData({
      insid: options.insid
    })
    this.loadInfo()

    wx.request({
      url: host+'/getinsinfo/?insid=' + options.insid,
      method:'GET',
      success(res){
        console.log(res)
        that.setData({
          info: res.data.insinfo,
          num:res.data.num
        })
      },fail(res){
        console.log(res)
      }
    })

    wx.request({
      url: host+'/activites/allactivity/?insid=' + options.insid,
      success(res){
        console.log(res.data)
        that.setData({
          activitys:res.data.activity
        })
      }
    })
  },
  //点击导航
  Navigation: function () {
    var _that = this
    wx.getSetting({
      success(res) {
        console.log(res.authSetting)
        if (res.authSetting['scope.userLocation'] == false) { //判断是否允许使用地理位置，允许使用直接打开地图
          console.log('用户未授权')
          wx.chooseLocation({ //不允许在此次授权
            success: function (res) {
              console.log('success')
              console.log(res)
            },
            fail: function (res) {
              console.log('fail')
              console.log(res)
              wx.showModal({
                title: '是否授权当前位置',
                content: '需要获取您的地理位置，请确认授权，否则定位功能将无法使用',
                success: function (res) {
                  if (res.confirm) {
                    wx.openSetting({
                      success: function (res) {
                        console.log(res)
                        if (res.authSetting['scope.userLocation'] == true) {
                          wx.showToast({
                            title: '授权成功',
                            icon: 'success',
                            duration: 2000
                          })
                          _that.Nav()

                        } else {
                          wx.showToast({
                            title: '授权失败',
                            icon: 'none',
                            duration: 2000
                          })
                        }
                      }
                    })
                  }
                }
              })
            }
          })
          _that.setData({
            location: '0' + "," + '0'
          })
        } else {
          _that.Nav()
          console.log('用户已授权')

        }
      }
    })
  },
  Nav: function () {
    var that = this
    console.log(that.data.info)
    // var latitude = that.data.shops.location.split(',')[0]
    // var longitude = that.data.shops.location.split(',')[1]
    let plugin = requirePlugin('routePlan');
    let key = 'BWLBZ-FGB66-YCISG-E5HHW-O7NVV-2NFRC'; //使用在腾讯位置服务申请的key
    let referer = 'BG课'; //调用插件的app的名称
    let endPoint = JSON.stringify({ //终点
      'name': that.data.info.address,
      'latitude': that.data.info.latitude,
      'longitude': that.data.info.longitude
    });
    wx.navigateTo({
      url: 'plugin://routePlan/index?key=' + key + '&referer=' + referer + '&endPoint=' + endPoint
    });
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
    const that = this
    if (wx.getStorageSync('openid')) {
      const userid = wx.getStorageSync('userid')
      wx.request({
        url: host+"/collectstatus?userid=" + userid + '&insid=' + that.data.insid,
        method: 'GET',
        success(res) {
          console.log(res)
          that.setData({
            'info.isCollected': res.data.status
          })
        }, fail(res) {
          console.log(res)
        }
      })
    }
    if (this.data.reload) {
      this.setData({
        reload: false // 清除刷新标志
      })
      this.loadInfo()
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


  /**
   * 收藏按键逻辑
   */
  bindCollect: function () {
    if (wx.getStorageSync('userInfo')) {
      var that = this
      let isCollected = that.data.info.isCollected
      let collectNumber = that.data.info.collect
      // 收藏或取消收藏
      let method = isCollected ? Institution.cancelCollect : Institution.collect
      method(that.data.insid).then(res => {
        isCollected = !isCollected // 更新执行接口调用后的状态
        collectNumber += isCollected ? 1 : -1
        that.setData({
          'info.isCollected': isCollected,
          'info.collect': collectNumber
        })
      })
      that.onShow()
    } else {
      wx.showToast({
        title: '请登录',
        icon: 'none',
        duration: 1000,
        success: function (res) {
          setTimeout(function () {
            wx.navigateTo({
              url: '/pages/accredit/accredit',
            })
          }, 1000)
        }
      })
    }
    
  },

  //进入活动详情
  activityinfo:function(e){
    console.log(e.currentTarget.dataset)
    wx.navigateTo({

      url: '/pages/activityinfo/activityinfo?activity_id=' + e.currentTarget.dataset.aid

    })
  },

  /**
   * 拨打电话
   */
  bindMakePhoneCall: function () {
    wx.makePhoneCall({
      phoneNumber: this.data.info.phone
    })
  },

  // 触摸开始时间
  touchStartTime: 0,
  // 触摸结束时间
  touchEndTime: 0,
  // 最后一次单击事件点击发生时间
  lastTapTime: 0,
  // 单击事件点击后要触发的函数
  lastTapTimeoutFunc: null,
  // 暂存上次点击的项目
  lastItem: null,

  /// 按钮触摸开始触发的事件
  touchStart: function (e) {
    this.touchStartTime = e.timeStamp
  },
  /// 按钮触摸结束触发的事件
  touchEnd: function (e) {
    this.touchEndTime = e.timeStamp
  },
  /**
   * item点击处理函数
   */
  handleTap: function (e) {
    // 控制点击事件在350ms内触发，防止长按时触发点击事件
    if (this.touchEndTime - this.touchStartTime < 350) {
      // 清除延时任务
      clearTimeout(this.lastTapTimeoutFunc)

      // 当前点击的时间
      const currentTime = e.timeStamp
      const lastTapTime = this.lastTapTime
      // 更新最后一次点击时间
      this.lastTapTime = currentTime

      // 获取item信息
      const item = e.currentTarget.dataset.item
      const lastItem = this.lastItem
      this.lastItem = item

      // 如果两次点击时间在300毫秒内，则认为是双击事件; 同时双击目标得是同一个item
      if (currentTime - lastTapTime < 300 && lastItem != null && lastItem.id == item.id) {
        // 成功触发双击事件时，取消单击事件的执行
        this.data.videos.forEach((value, index) => {
          if (item.id == value.id) {
            let isLike = item.isLike
            let like = item.like
            let institutionLike = this.data.info.like
            // 点赞或取消点赞
            let method = isLike ? Video.cancelLike : Video.like
            method(item.id).then(res => {
              isLike = !isLike // 更新执行接口调用后的状态
              like += isLike ? 1 : -1
              institutionLike += isLike ? 1 : -1
              this.setData({
                ['videos[' + index + '].isLike']: isLike,
                ['videos[' + index + '].like']: like,
                'info.like': institutionLike
              })
            })
            return
          }
        })
      } else {
        // 单击事件延时300毫秒执行
        this.lastTapTimeoutFunc = setTimeout(() => {
          wx.navigateTo({
            url: '../player/player?record=true&id=' + item.id
          })
        }, 300)
      }
    }
  },
  // 报名
  onApply: function(e){
    wx.navigateTo({
      url: '/pages/apply/apply?activity_id==' + e.currentTarget.dataset.insid + ' &user_id ' + app.globalData.user_id
      
    })
  }
})






