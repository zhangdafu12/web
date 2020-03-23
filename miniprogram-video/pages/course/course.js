import {
  History,
  
} from '../../utils/api'
const app = getApp()
const host = app.globalData.host
Page({

  /**
   * 页面的初始数据
   */
  data: {
    activitys:'',
    collectinfo:[],
    historyList: [],
    statusBarHeight: 0,
    contentHeight: 0,
    currentTab: 0,
    host : app.globalData.host
  },
  goback: function () {
    wx.navigateBack({
      delata: 1
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    const res = wx.getSystemInfoSync()
    const windowHeight = res.windowHeight
    const statusBarHeight = res.statusBarHeight
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
    const that=this
    if(options.insid){
      wx.request({
        url: host+'/activites/allactivity/?insid=' + options.insid,
        success(res) {
          console.log(res.data)
          that.setData({
            activitys: res.data.activity
          })
        }
      })
    }else{
      that.setData({
        activitys: []
      })
    }


    wx.request({
      url: host+'/collectinfo/?user_id=' + wx.getStorageSync('userid'),
      method: 'GET',
      success(res) {
        console.log(res)
        that.setData({
          collectinfo: res.data.collectinfo
        })
      }

    })
    History.list().then(historyList => {
      console.log(historyList)
      this.setData({
        historyList
      })
    })






  },
  /**
 * 切换导航栏
 */
  onPullDownRefresh: function () {
    wx.showNavigationBarLoading()
    this.onLoad()
    setTimeout(() => {
      wx.hideNavigationBarLoading()
      wx.stopPullDownRefresh()
    }, 2000);
  },
  onNavbarTap: function (e) {
    // const id = e.currentTarget.dataset.id
    // if (id == 1) {
    //   this.loadData()
    // }
    this.setData({
      currentTab: e.currentTarget.dataset.id
    })
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

  },

  insinfo:function(e){
    const insid = e.currentTarget.dataset.insid
    wx.navigateTo({
      url: '../details/details?insid=' + insid,
    })
  }

})