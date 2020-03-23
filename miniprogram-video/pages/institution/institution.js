import {
  Institution,
  InstitutionImage,
  Video
} from '../../utils/api'

//获取应用实例
const app = getApp()
const host = app.globalData.host

Page({

  /**
   * 页面的初始数据
   */
  data: {
    address:'地址',
    latitude:'',
    longitude:'',
    imagelist:[],
    uploadimgList: [],
    uploadimgNum: 0,
    statusBarHeight: 0,
    contentHeight: 0,
    info: {},
    videos: [],
    uploaded: false,
    isAdmin: false,
    // 模态框数据项
    modalKey: null,
    // 模态框输入比例值、抵扣值的暂存
    scale: 1,
    maxDeduction: 100,
    // 用于模态框提示
    dict: {
      'name': '机构名称',
      'avatar': '机构头像',
      'address': '地址',
      'phone': '电话',
      'license': '营业执照',
      'scale': 'R币比例值',
      'maxDeduction': '最多抵扣值'
    },
    deleteBtn:true,
    host : app.globalData.host
  },

  goback: function () {
    wx.switchTab({
      url: '/pages/mine/mine'
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

  showActivity:function(){
    wx.navigateTo({
      url: '/pages/upload/upload'
    })
  },
  showPlayRegulate: function () {
    wx.navigateTo({
      url: '/pages/control/control'
    })
  },
  myBank: function () {
    wx.navigateTo({
      url: '/pages/bank/bank'
    })
  },
  myWallet:function(){
    wx.navigateTo({
      url: '/pages/wallet/wallet'
    })
  },

//选择地址
  changeAddress:function(){
    let that=this;
    wx.chooseLocation({
      success: function (res) {
        console.info(res);
        console.info(res.address);
        console.info(res.name);
        that.setData({
          address:res.address,
          'info.address': res.address,
          'info.latitude':res.latitude,
          'info.longitude':res.longitude
        })
      },
    })
  },

  // 图片上传
  photoList:[],
  upload: function (e) {
    const maxlen = 5;
    var that = this;
    console.log(e)
    wx.chooseImage({
      count: maxlen - this.data.uploadimgNum,
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 指定图片来源是相册还是相机， 默认二者都有
      success: function (res) {
        const filePath = res.tempFilePaths[0]
        console.log(res.tempFilePaths)
        console.log(res)
        const temp = res.tempFilePaths;
        const uploadimgList = that.data.uploadimgList.concat(temp);  // 页面显示图片列表
        that.photoList = that.photoList.concat(res.tempFiles);
        console.log(that.photoList,'1111111111111111111111111111111111111')
        that.setData({
          uploadimgList: uploadimgList,
          uploadimgNum: uploadimgList.length,
          imagePath: uploadimgList[0]
        })
        that.photoList.forEach(photo => {
          if (typeof (photo.id) == "undefined") {
            console.log(photo.path, app.globalData.institution_id)
            wx.uploadFile({
              url: host+'/institutionimage/',
              filePath: photo.path,
              name: 'img',
              header: {
                "Content-Type": "multipart/form-data",
                'accept': 'application/json',
              },
              formData: { 'insid':app.globalData.institution_id},
              success(res){
                console.log(res)
                that.onLoad()
              },fail(res){
                console.log(res)
              }
            })
          }
        })
      },
    })
    that.photoList.splice(0, that.photoList.length)
    
  },


  // 活动图片删除
  deleteImg: function (e) {
    var that = this
    let number = e.currentTarget.dataset.num
    // ActivityPhoto.delete(delphoto.id).then(result => {
    wx.request({
      url: host+'/DeleteInsImage/',
      method:'POST',
      data:{
        'imgid':e.currentTarget.dataset.imgid
      }
      ,success(res){
        console.log(res)
        if(res.data.status==203){
          that.onLoad()
        }
      }
    })
     
      
    // })

    this.data.uploadimgList.splice(number, 1)
    this.data.uploadimgNum -= 1
    this.setData({
      uploadimgList: this.data.uploadimgList,
      uploadimgNum: this.data.uploadimgNum
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
      var that = this
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

    if (app.globalData.institution_id != null) {
      // 加载机构信息
      Institution.retrieve(
          app.globalData.institution_id
        ).then(info => {
          this.setData({
            info,
            isAdmin: true,
            scale: info.scale,
            maxDeduction: info.maxDeduction
          })
        }),
        // 加载机构视频列表
        Video.list({
          institution: app.globalData.institution_id
        }).then(videos => {
          this.setData({
            videos
          })
        }),
        //加载机构图片
       wx.request({
        url: host+'/AllInsIMage/?insid='+app.globalData.institution_id,
        method:'GET',
        success(res){
          console.log(res)
          that.setData({
            imagelist:res.data.images
          })
        }
       })
    }
  },


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
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    if (this.data.uploaded) {
      this.setData({
        uploaded: true
      })
      // 上传成功后，重新加载机构视频列表
      Video.list({
        institution: app.globalData.institution_id
      }).then(videos => {
        this.setData({
          videos
        })
        wx.showToast({
          title: '上传成功',
          duration: 2000
        })
      })
    }
  },

  /**
   * 修改头像
   */
  bindChangeAvatar: function () {
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const filePath = res.tempFilePaths[0]
        if (this.data.isAdmin) {
          wx.showModal({
            title: '确认修改机构头像',
            success: (res) => {
              if (res.confirm) {
                Institution.uploadAvatar(app.globalData.institution_id, 'avatar', filePath).then(result => {
                  const info = this.data.info
                  info['avatar'] = result.avatar
                  this.setData({
                    info
                  })
                })
              } else if (res.cancel) {}
            }
          })
        } else {
          this.setData({
            'info.avatar': filePath,
          })
        }
      }
    })
  },

  /**
   * 保存修改
   */
  handleSave: function (e) {
    const id = e.currentTarget.dataset.id
    const value = e.detail.value.trim()
    if (this.data.isAdmin) {
      const isChanged = value != this.data.info[id]
      if (isChanged) {
        wx.showModal({
          title: '保存修改',
          content: `确认【${this.data.dict[id]}】修改为：${value}`,
          success: (res) => {
            const info = this.data.info // 暂存设置
            if (res.confirm) { // 提交修改
              info[id] = value
              Institution.update(app.globalData.institution_id, info).then(result => {
                this.setData({
                  info
                })
              })
            } else if (res.cancel) { // 恢复设置
              this.setData({
                info
              })
            }
          }
        })
      }
    } else {
      const info = this.data.info
      info[id] = value
      this.setData({
        info
      })
    }
  },

  /**
   * 显示自定义模态框
   */
  showModal: function (e) {
    const id = e.currentTarget.dataset.id
    this.setData({
      modalKey: id
    })
  },

  /**
   * 模态框输入暂存
   */
  modalInput: function (e) {
    const value = e.detail.value.trim()
    this.setData({
      [this.data.modalKey]: value
    })
  },

  /**
   * 模态框取消
   */
  modalCancel: function () {
    this.setData({
      modalKey: null
    })
  },

  /**
   * 模态框确认
   */
  modalConfirm: function () {
    this.setData({
      ['info.' + this.data.modalKey]: this.data[this.data.modalKey],
      modalKey: null
    })
    if (this.data.isAdmin) {
      Institution.update(app.globalData.institution_id, this.data.info).then(result => {})
    }
  },

  /**
   * 提交机构入驻申请
   */
  submit: function () {
    for (let key in this.data.dict) {
      if (!(key in this.data.info)) {
        wx.showModal({
          title: `请输入${this.data.dict[key]}`,
          showCancel: false
        })
        return
      }
    }
    Institution.create(this.data.info).then(institution => {
      Institution.uploadAvatar(institution.id, 'avatar', this.data.info.avatar).then(result => {
        wx.showModal({
          title: '入驻申请已提交',
          content: '请等待审核通过',
          showCancel: false,
          success: (res) => {
            wx.navigateBack({
              delta: 1
            })
          }
        })
      })
    })
  },


  /**
   * 播放视频
  //  */
  // bindPlay: function (e) {
  //   const item = e.currentTarget.dataset.item
  //   wx.navigateTo({
  //     url: '../player/player?record=false&id=' + item.id
  //   })
  // },

  /**
   * 长按操作
   */
  bindDelete:function(e){
    console.log(this.data.videos)
    console.log(e.target.dataset.item)
    const num = e.target.dataset.item
    const videos = this.data.videos
   videos.splice(num, 1)
    this.setData({
      uploadimgList: videos
    })

  }
})