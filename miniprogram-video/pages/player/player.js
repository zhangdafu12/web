import {
  User,
  Video,
  Institution,
  Comment
} from '../../utils/api'

const moment = require('../../libs/moment-with-locales.min.js')
moment.locale('zh-cn')

//获取应用实例
const app = getApp()
const host = app.globalData.host

Page({

  /**
   * 页面的初始数据
   */
  data: {
    video: {},
    institutionId: null,
    institutionAvatar: '/images/icon_mine.png',
    usersInfo: {},
    comments: [],
    isShowComments: false,
    isReply: false,
    replyUser: null,
    content: '',
  },

  timer: null, // 定时器

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.isNeedRecord = options.record
    // 通过接口获取对应 id 视频信息
    const id = options.id
    Video.retrieve(id).then(video => {
      this.setData({
        video
      })
      // 获取机构头像
      Institution.retrieve(video.institution).then(institution => {
        this.setData({
          institutionId: institution.id,
          institutionAvatar: institution.avatar
        })
        // 视频、机构信息加载完毕后，再开始加载评论相关数据
        // 通过接口加载自己的信息
        User.retrieve(app.globalData.user_id).then(user => {
          this.setData({
            ['usersInfo[' + app.globalData.user_id + ']']: user
          })
        })
        // 加载评论
        Comment.list({
          video: id
        }).then(comments => {
          comments.forEach((comment, index) => {
            // 获取用户信息
            if (!this.data.usersInfo[comment.user]) {
              // 加载期间填充空数据，防止重复加载
              this.setData({
                ['usersInfo[' + comment.user + ']']: {}
              })
              User.retrieve(comment.user).then(user => {
                this.setData({
                  ['usersInfo[' + comment.user + ']']: user
                })
              })
            }
          })
          this.setData({
            comments
          })
          // 转化时间，开启定时器
          this.getReltiveTime()
          this.timer = setInterval(this.getReltiveTime, 1000)
        })
      })
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
    if (this.isNeedRecord === 'true' && !this.isRecorded) {
      this.record()
    }
    // 清除定时器
    clearInterval(this.timer)
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
   * 转化时间
   */
  getReltiveTime: function () {
    const comments = this.data.comments
    comments.forEach(comment => {
      comment.reltiveTime = moment(comment.time).fromNow()
      comment.reply_set.forEach(reply => {
        reply.reltiveTime = moment(reply.time).fromNow()
      })
    })
    this.setData({
      comments
    })
  },

  commentIndex: null,
  replyTo: null, // 指示子回复

  /**
   * 点击评论
   */
  onReply: function (e) {
    this.commentIndex = e.currentTarget.dataset.index
    this.replyTo = e.currentTarget.dataset.reply
    let replyUser
    if (this.replyTo) {
      replyUser = this.replyTo.user
    } else {
      replyUser = this.data.comments[this.commentIndex].user
    }
    this.setData({
      isReply: true,
      replyUser
    })
  },

  /**
   * 取消回复用户
   */
  cancelReply: function () {
    this.setData({
      isReply: false
    })
  },

  /**
   * 提交评论
   */
  onComment: function (e) {
    const content = e.detail.value.content.trim()
    if (content.length > 0) {
      const data = {
        video: this.data.video.id,
        user: app.globalData.user_id,
        content
      }
      if (this.data.isReply) {
        data.reply = this.data.comments[this.commentIndex].id
        if (this.replyTo) {
          data.reply_user = this.replyTo.user
        }
      }
      Comment.create(data).then(comment => {
        const comments = this.data.comments
        if (this.data.isReply) {
          comments[this.commentIndex].reply_set.push(comment)
        } else {
          comments.push(comment)
        }
        this.setData({
          comments,
          isReply: false,
          content: ''
        })
      })
    }
  },

  isPlaying: false,
  isRecorded: false,
  countTime: 0,
  lastTime: 0,

  onPlay: function () {
    this.isPlaying = true
    this.isRecorded = false
  },

  onPause: function (e) {
    this.isPlaying = false
    if (this.isNeedRecord === 'true' && !this.isRecorded) {
      this.record()
    }
  },

  onEnded: function (e) {
    this.isPlaying = false
    if (this.isNeedRecord === 'true' && !this.isRecorded) {
      this.record()
    }
  },

  onTimeUpdate: function (e) { // TODO: 调试时视频过短时，观看时长统计不准，真机还未尝试
    const currentTime = e.detail.currentTime
    const deltaTime = currentTime - this.lastTime
    this.lastTime = currentTime
    if (this.isPlaying && deltaTime > 0 && deltaTime < 1.5) {
      this.countTime += deltaTime
    }
  },

  record: function () {
    this.isRecorded = true
    Video.record(this.data.video.id, {
      countTime: this.countTime,
      lastTime: this.lastTime
    }).then(res => {
      const reward = res.reward
      if (reward > 0) {
        wx.showToast({
          title: `观看奖励：+${reward} V币`,
          icon: 'none',
          duration: 2000
        })
      }
    })
  },

  goToInstitution: function (e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: '/pages/details/details?id=' + id
    })
  },

  /**
   * 点赞
   */
  bindLike: function (e) {
    let isLike = this.data.video.isLike
    let like = this.data.video.like
    let method = isLike ? Video.cancelLike : Video.like
    // 点赞或取消点赞
    method(this.data.video.id).then(res => {
      isLike = !isLike // 更新执行接口调用后的状态
      like += isLike ? 1 : -1
      this.setData({
        'video.isLike': isLike,
        'video.like': like
      })
      const pages = getCurrentPages()
      const prevPage = pages[pages.length - 2] //上一个页面
      //直接调用上一个页面的setData()方法，把数据存到上一个页面中去
      prevPage.setData({
        reload: true // 返回时刷新页面
      })
    })
  },

  onShowComments: function () {
    this.setData({
      isShowComments: true
    })
  },

  onHideComments: function () {
    this.setData({
      isShowComments: false
    })
  },
})