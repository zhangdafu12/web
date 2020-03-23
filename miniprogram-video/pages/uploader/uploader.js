import {
  Video
} from "../../utils/api";

//获取应用实例
const app = getApp()
const host = app.globalData.host

Page({

  /**
   * 页面的初始数据
   */
  data: {
    length: 0,
    maxLength: 200,
    text: '',
    title: '',
    video: '',
    play: false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.videoContext = wx.createVideoContext('video')
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

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  /**
   * 输入标题
   */
  onTitleInput: function (e) {
    const title = e.detail.value
    this.setData({
      title
    })
  },

  /**
   * 统计输入字数
   */
  handleInput: function (e) {
    const text = e.detail.value
    this.setData({
      text,
      'length': text.length
    })
  },

  /**
   * 选择视频
   */
  bindChooseVideo: function () {
    wx.chooseVideo({
      sourceType: ['album', 'camera'],
      maxDuration: 60,
      camera: 'back',
      success: (res) => {
        this.setData({
          video: res.tempFilePath
        })
      }
    })
  },

  /**
   * 删除视频
   */
  bindDeleteVideo: function (e) {
    this.setData({
      video: ''
    })
  },

  /**
   * 点击播放
   */
  bindPlay: function (e) {
    const videoContext = this.videoContext
    videoContext.requestFullScreen({
      direction: 0
    })
    videoContext.seek(0)
    videoContext.play()
  },

  /**
   * 全屏状态变化
   */
  bindFullScreenChange: function (e) {
    let play = false
    if (e.detail.fullScreen) {
      play = true
    } else {
      this.videoContext.stop()
    }
    this.setData({
      play
    })
  },

  /**
   * 保存
   */
  bindSave: function () {
    const title = this.data.title
    const text = this.data.text
    const video = this.data.video

    if (!title) {
      wx.showToast({
        title: '请输入标题',
        image: '/images/icon_warning.png',
        duration: 2000
      })
      return
    }

    if (!text) {
      wx.showToast({
        title: '请输入文本内容',
        image: '/images/icon_warning.png',
        duration: 2000
      })
      return
    }

    if (!video) {
      wx.showToast({
        title: '请选择视频',
        image: '/images/icon_warning.png',
        duration: 2000
      })
      return
    }

    Video.create('video', video, {
      title,
      content: text,
      institution: app.globalData.institution_id,
    }).then(result => {
      const pages = getCurrentPages()
      const prevPage = pages[pages.length - 2]
      prevPage.setData({
        uploaded: true
      })
      wx.navigateBack({
        delta: 1
      })
    })
  }
})