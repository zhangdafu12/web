import {
  Institution,
  Video
} from '../../utils/api'

import {
  getCity,
} from "../../utils/util"

//获取应用实例
const app = getApp()
const host = app.globalData.host

Page({

  /**
   * 页面的初始数据
   */
  data: {
    statusBarHeight: 0,
    contentHeight: 0,
    searchText: '',
    institutionList: [],
    showAuthModal: false,
    isShowCancel: false,
    reload: false // 从播放页面返回时用于判断是否需要刷新数据
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    this.setData({
      searchText:options.search_name
    })
    this.loadData()
    // 计算 scrollView 高度，scrollView 无法用 flex: 1 撑满页面
    const res = wx.getSystemInfoSync()
    const windowHeight = res.windowHeight
    const statusBarHeight = res.statusBarHeight
    let query = wx.createSelectorQuery().in(this);
    query.select('.navbar').boundingClientRect(); // 查询头部导航栏
    query.exec((res) => {

      let contentHeight = windowHeight - statusBarHeight;
      this.setData({
        statusBarHeight,
        contentHeight
      });
    });

    // 用户身份认证
    const token = wx.getStorageSync('token')
    if (!token) {
      console.log('无 token，尝试登陆')
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


  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    if (this.data.reload) {
      this.setData({
        reload: false // 清除刷新标志
      })
      this.loadData()
    }
  },
  
  insinfo: function (e) {
    let insid = e.currentTarget.dataset.insid
    console.log(insid)
    wx.navigateTo({
      url: '../details/details?insid=' + insid,

    })
  },
  /**
   * 获取用户信息
   */
  getUserInfo: function () {
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

  getDistance: function (lat1, lng1, lat2, lng2) {

    var radLat1 = lat1 * Math.PI / 180.0;
    var radLat2 = lat2 * Math.PI / 180.0;
    var a = radLat1 - radLat2;
    var b = lng1 * Math.PI / 180.0 - lng2 * Math.PI / 180.0;
    var s = 2 * Math.asin(Math.sqrt(Math.pow(Math.sin(a / 2), 2) +
      Math.cos(radLat1) * Math.cos(radLat2) * Math.pow(Math.sin(b / 2), 2)));
    s = s * 6378.137;// EARTH_RADIUS;
    s = Math.round(s * 10000) / 10000;
    return s;
  },

  /**
   * 获取到用户信息
   */
  onGotUserInfo: function (e) {
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      showAuthModal: false
    })
  },

  /**
   * 加载数据
   */
  loadData: function () {
    // 加载机构列表
    Institution.list({name:this.data.searchText}).then(institutionList => {
      this.setData({
        institutionList:institutionList
      })
      institutionList.forEach((institution, index) => {
        console.log(institution)
        console.log(app.globalData.latitude, app.globalData.longitude)
        let distance = ''
        distance = this.getDistance(app.globalData.latitude, app.globalData.longitude, parseFloat(institution.latitude), parseFloat(institution.longitude))
        institution.distance = distance
        // 获取机构视频列表
        Video.list({
          institution: institution.id
        }).then(videoList => {
          this.setData({
            ['institutionList[' + index + '].videos']: videoList,
            ['institution[' + index + '].id']: institution
          })
        })
      })

      institutionList.sort(this.sortBy("distance"));
      console.log(institutionList)

      this.setData({
        institutionList
      })
      console.log(this.data.institutionList)
      })
  },


  //根据数组中对象的属性排序
  sortBy: function (props) {
    return function (a, b) {
      return a[props] - b[props];
    }
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

      const institution_index = e.currentTarget.dataset.index

      // 如果两次点击时间在300毫秒内，则认为是双击事件; 同时双击目标得是同一个item
      if (currentTime - lastTapTime < 300 && lastItem != null && lastItem.id == item.id) {
        // 成功触发双击事件时，取消单击事件的执行
        this.data.institutionList.forEach((institution) => {
          institution.videos.forEach((value, index) => {
            if (item.id == value.id) {
              let isLike = item.isLike
              let like = item.like
              // 点赞或取消点赞
              let method = isLike ? Video.cancelLike : Video.like
              method(item.id).then(res => {
                isLike = !isLike // 更新执行接口调用后的状态
                like += isLike ? 1 : -1
                this.setData({
                  ['institutionList[' + institution_index + '].videos[' + index + '].isLike']: isLike,
                  ['institutionList[' + institution_index + '].videos[' + index + '].like']: like
                })
              })
              return
            }
          })
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
  onShareAppMessage: function (res) {
    return {
      title: 'BG课',
      path: '/pages/index/index',
      // imageUrl: 'http://static.e-mallchina.com/pic/product/brand/detail/hgds.jpg'//自定义图片路径，可以是本地文件路径、代码包文件路径或者网络图片路径。支持PNG及JPG。显示图片长宽比是 5:4。
    }
  }
})