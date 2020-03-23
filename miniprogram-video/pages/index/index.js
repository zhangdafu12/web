import {
  Institution,
  Video,
  
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
    url:'',
    distance:'',
    photolist:[],
    statusBarHeight: 0,
    contentHeight: 0,
    currentTab: 0,
    city: '获取中',
    searchText: '',
    institutionList: [],
    institution:'',
    showAuthModal: false,
    isShowCancel: false,
    reload: false, // 从播放页面返回时用于判断是否需要刷新数据
    host :app.globalData.host,
    indicatorDots: true,
    vertical: false,
    autoplay: false,
    interval: 2000,
    duration: 500
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
    // 计算 scrollView 高度，scrollView 无法用 flex: 1 撑满页面
    const res = wx.getSystemInfoSync()
    const windowHeight = res.windowHeight
    const statusBarHeight = res.statusBarHeight
    let query = wx.createSelectorQuery().in(this);
    query.select('.navbar').boundingClientRect(); // 查询头部导航栏
    query.exec((res) => {
      let navbarHeight = res[0].height;
      let contentHeight = windowHeight - statusBarHeight - navbarHeight;
      this.setData({
        statusBarHeight,
        contentHeight
      });
    });

    ////获取首页图片
    const that=this
    wx.request({
      url: host+'/getindeximage/',
      method:'GET',
      success(res){
        that.setData({
          url:res.data.url
        })
      }
    })
    // 定位
    wx.getLocation({
      type: 'gcj02',
      success: (result) => {
        app.globalData.latitude = result.latitude
        app.globalData.longitude = result.longitude
        // 获取定位城市
        getCity(result.latitude, result.longitude).then(city => {
          this.setData({
            city
          })
        })
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
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    var that = this
    if (this.data.reload) {
      this.setData({
        reload: false // 清除刷新标志
      })
      this.loadData()
    }
    wx.request({
      url: host+'/AllInsIMage/',
      method: 'GET',
      success(res) {
        console.log(res)
        that.setData({
          photolist:res.data.images
        })
        
      }
    })
  },

  /**
   * 加载数据
   */
  //图片预览
  bigImg(e) {
    console.log(e.currentTarget.dataset.src)
    let src = e.currentTarget.dataset.src
    wx.previewImage({
      current: src, // 当前显示图片的http链接
      urls: [src],// 需要预览的图片http链接列表
      success(e) {
        console.log(e)
      },
      fail(e) {
        console.log(e)
      }
    })
  },
  //计算距离
  // 方法定义 lat,lng 
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
  loadData: function () {
    // 加载机构列表
    Institution.list().then(institutionList => {

      institutionList.forEach((institution, index) => {
        console.log(institution)
        console.log(app.globalData.latitude, app.globalData.longitude,)
        let distance = ''
        distance = this.getDistance(app.globalData.latitude, app.globalData.longitude,   parseFloat(institution.latitude), parseFloat(institution.longitude))
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

  insinfo: function (e) {
    let insid = e.currentTarget.dataset.insid
    console.log(insid)
    wx.navigateTo({
      url: '../details/details?insid='+ insid,
      
    })
  },

  /**
   * 切换导航栏
   */
  onNavbarTap: function (e) {
    const id = e.currentTarget.dataset.id
    if (id == 1) {
      this.loadData()
    }
    this.setData({
      currentTab: e.currentTarget.dataset.id
    })
  },

  /**
   * 处理搜索框输入
   */
  handleSearchInput: function (e) {
    const searchText = e.detail.value
    let isShowCancel = false
    if (searchText.length > 0) {
      isShowCancel = true
    }
    this.setData({
      searchText,
      isShowCancel
    })
  },

  /**
   * 取消搜索
   */
  onCancelSearch: function () {
    this.setData({
      searchText: '',
      isShowCancel: false
    })
  },

  /**
   * 点击首页评论
   */
  onTapComment: function () {
    console.log('comment')
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



  test: function (event) {
        wx.navigateTo({
          url: '/pages/apply/apply?user_id=' + app.globalData.user_id + '&activity_id=' + '1',
        // })
      // }
    })
    // const activity_id = event.target.dataset.activity_id
    
  },






  /**
   * item点击处理函数
   */
  // handleTap: function (e) {
  //   // 控制点击事件在350ms内触发，防止长按时触发点击事件
  //   if (this.touchEndTime - this.touchStartTime < 350) {
  //     // 清除延时任务
  //     clearTimeout(this.lastTapTimeoutFunc)

  //     // 当前点击的时间
  //     const currentTime = e.timeStamp
  //     const lastTapTime = this.lastTapTime
  //     // 更新最后一次点击时间
  //     this.lastTapTime = currentTime

  //     // 获取item信息
  //     const item = e.currentTarget.dataset.item
  //     const lastItem = this.lastItem
  //     this.lastItem = item

  //     const institution_index = e.currentTarget.dataset.index

  //     // 如果两次点击时间在300毫秒内，则认为是双击事件; 同时双击目标得是同一个item
  //     if (currentTime - lastTapTime < 300 && lastItem != null && lastItem.id == item.id) {
  //       // 成功触发双击事件时，取消单击事件的执行
  //       this.data.institutionList.forEach((institution) => {
  //         institution.videos.forEach((value, index) => {
  //           if (item.id == value.id) {
  //             let isLike = item.isLike
  //             let like = item.like
  //             // 点赞或取消点赞
  //             let method = isLike ? Video.cancelLike : Video.like
  //             method(item.id).then(res => {
  //               isLike = !isLike // 更新执行接口调用后的状态
  //               like += isLike ? 1 : -1
  //               this.setData({
  //                 ['institutionList[' + institution_index + '].videos[' + index + '].isLike']: isLike,
  //                 ['institutionList[' + institution_index + '].videos[' + index + '].like']: like
  //               })
  //             })
  //             return
  //           }
  //         })
  //       })
  //     } else {
  //       // 单击事件延时300毫秒执行
  //       this.lastTapTimeoutFunc = setTimeout(() => {
  //         wx.navigateTo({
  //           url: '../player/player?record=true&id=' + item.id
  //         })
  //       }, 300)
  //     }
  //   }
  // },
  onShareAppMessage: function (res) {
    return {
      title: 'BG课',
      path: '/pages/index/index',
      // imageUrl: 'http://static.e-mallchina.com/pic/product/brand/detail/hgds.jpg'//自定义图片路径，可以是本地文件路径、代码包文件路径或者网络图片路径。支持PNG及JPG。显示图片长宽比是 5:4。
    }
  },
  search:function(e){
    var search_name = this.data.searchText
    wx.navigateTo({
      url: '../search/search?search_name=' + search_name
    })
  }
})