// pages/upload/upload.js
const app = getApp()
const host = app.globalData.host
import {
  canvas,
  promisify,
} from "../../utils/util.js";

import {
  Activity,
  ActivityPhoto,
  RaplyRecord,
} from "../../utils/api.js"

Page({
  /**
   * 页面的初始数据
   */
  data: {
    activity:'',
    num:'',
    disabled:true,
    flag: true,
    flag1: true,
    flag2: true,
    item: ['砍价', '竞拍'],
    currentTab: 0,
    isShow: true,
    backprice:'',
    uploadimgList: [],
    uploadimgNum: 0,
    uploadvList: [],
    uploadvNum: 0,

    nocancel: false,

    hiddenName: true,
    hiddenTotal: true,
    hiddenPrice: true,
    hiddenNumber: true,
    hiddenActivity: true,
    hiddenAstrict: true,


    valueName: "",
    valueTotal: "",
    valuePrice: "",
    valueActivity: "",
    valueAstrict: "",
    windowHeight: 0,
    windowWidth: 0,

    imageBG: "/images/bg_fff.png",
    imagePortrait: "/images/icon_like.png",
    chargeStatement: "",

    imagePath: "/images/share_bg2.jpg",   // 活动图片
    imageEwm: "",    // 二维码图片

    title_name: "BG课",
    discount: "折扣",
    course_name: '',
    price: '',
    activity_tips: "长按识别生成活动小程序",
    showCanvas: true,
  },
  onPullDownRefresh: function () {
    wx.showNavigationBarLoading()
    this.onLoad()
    setTimeout(() => {
      wx.hideNavigationBarLoading()
      wx.stopPullDownRefresh()
    }, 2000);
  },

  // 平台规则
  regulationAll: function () {
    console.log('111')
    wx.showModal({
      title: '平台规则',
      content: '这里是平台规则',
    })
  },

//分享收益说明
  goShareTips:function(){
    wx.navigateTo({//incomeStatement

      url: '/pages/incomeStatement/incomeStatement',
})
  },
  //名称
  onName: function (e) {
    let that = this;
    this.setData({
      hiddenName: !that.data.hiddenName
    })
  },
  changName: function (e) {

    this.setData({
      valueName: e.detail.value,
      course_name: e.detail.value
    })
  },

  cancelName: function () {
    let that = this;
    this.setData({
      hiddenName: !this.data.hiddenName
    })
  },
  confirmName: function () {
    let that = this;
    this.setData({
      hiddenName: !this.data.hiddenName
    })
  },
  // 
  totalPrice: function (e) {
    let that = this;
    console.log(111)
    this.setData({
      hiddenTotal: !that.data.hiddenTotal
    })
  },
  changTotal: function (e) {
    console.log(e.detail.value)
    this.setData({
      valueTotal: e.detail.value
    })
  },

  apply:function(e){
    if (wx.getStorageSync('userInfo')) {
      wx.navigateTo({
        url: '/pages/apply/apply?user_id=' + app.globalData.user_id + '&activity_id=' + e.currentTarget.dataset.aid+"&status=0",
      })
    } else {
      wx.navigateTo({
        url: '/pages/accredit/accredit'
      })
    }

  },

  cancelTotal: function () {
    let that = this;
    this.setData({
      hiddenTotal: !this.data.hiddenTotal
    })
  },
  confirmTotal: function () {
    let that = this;
    this.setData({
      hiddenTotal: !this.data.hiddenTotal
    })
  },


  //价格
  shopPrice: function (e) {
    let that = this;
    console.log(111)
    this.setData({
      hiddenPrice: !that.data.hiddenPrice
    })
  },
  changPrice: function (e) {
    console.log(e.detail.value)
    this.setData({
      valuePrice: e.detail.value,
      price: e.detail.value
    })
  },

  cancelPrice: function () {
    let that = this;
    this.setData({
      hiddenPrice: !this.data.hiddenPrice
    })
  },
  confirmPrice: function () {
    let that = this;
    this.setData({
      hiddenPrice: !this.data.hiddenPrice
    })
  },
  // 
  shopActivity: function (e) {
    let that = this;
    console.log(111)
    this.setData({
      hiddenActivity: !that.data.hiddenActivity
    })
  },
  cancelActivity: function () {
    let that = this;
    this.setData({
      hiddenActivity: !this.data.hiddenActivity
    })
  },
  changActivity: function (e) {
    console.log(e.detail.value)
    this.setData({
      valueActivity: e.detail.value
    })
  },
  confirmActivity: function () {
    let that = this;
    this.setData({
      hiddenActivity: !this.data.hiddenActivity
    })
  },
  // 
  astrict: function (e) {
    let that = this;
    console.log(111)
    this.setData({
      hiddenAstrict: !that.data.hiddenAstrict
    })
  },
  changAstrict: function (e) {
    console.log(e.detail.value)
    this.setData({
      valueAstrict: e.detail.value
    })
  },

  cancelAstrict: function () {
    let that = this;
    this.setData({
      hiddenAstrict: !this.data.hiddenAstrict
    })
  },
  confirmAstrict: function () {
    let that = this;
    this.setData({
      hiddenAstrict: !this.data.hiddenAstrict
    })
  },

  // 获取testarea的值
  csInput: function (e) {
    this.setData({
      chargeStatement: e.detail.value
    })
  },

  // 机构新创建活动
  new_submit: function () {
    var that = this
    const photos = []
    this.photoList.forEach(photo => {
      if (typeof (photo.id) != "undefined") {
        photos.push(photo.id)
      }
    })
    const data = {
      "photos": photos,  // 活动照片
      "course_name": this.data.valueName,  // 课程名称
      "all_in_cost": this.data.valueTotal,  // 课程总费用
      "deposit": this.data.valuePrice,  // 报名定金
      "activity_price_deposit": this.data.valueActivity,  // 报名定金活动价
      "upper_limit": this.data.valueAstrict,  // 报名人数上限
      "statement": this.data.chargeStatement,  // 课程收费说明
      "institution": app.globalData.institution_id,  // 机构id
    }
    console.log(data)
    Activity.create(data).then(result => {
      console.log(result.id)
      var activity_id = result.id
      console.log(activity_id);
      console.log(")))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))0")
      that.qrcode(that, activity_id)
    })
  },


  // 向微信后台请求二维码
  qrcode: function (that, activity_id) {
    wx.request({
      url: 'http://heiyunworld.com:12123/wechat/token?type=access_token&secret=1234567890',
      header: {
        "Content-type": "application/json"
      },
      dataType: "json",
      success(res) {
        var token = res.data.access_token
        console.log(token)
        const data = {
          page: "pages/scan/scan",
          scene: String(activity_id + '&' + app.globalData.user_id),
        }
        console.log(data)
        console.log(activity_id)
        console.log(app.globalData.user_id)
        wx.request({
          url: 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=' + token,
          data: data,
          dataType: "json",
          method: "POST",
          responseType: "arraybuffer",
          success(qrcode) {

            const filePath = `${wx.env.USER_DATA_PATH}/aaaa.jpg`;
            wx.getFileSystemManager().writeFile({
              filePath,
              data: qrcode.data,
              encoding: 'binary',
              success() {
                wx.getImageInfo({
                  src: filePath,
                  success: function (res) {
                    console.log(res.width)
                    console.log(res.height)
                    console.log(res.path)
                    that.setData({
                      imageEwm: res.path
                    })
                    console.log(that.data.windowHeight, that.data.windowWidth);
                    that.createCanvas(that);

                  },
                  fail: function (e) {
                    console.log(e, 111)
                  }
                })
              },
              fail() {
              },
            });
          },
          fail(e) {
            console.log(e)
          }
        })
      }
    })
  },

  photoList: [],
  // 活动图片上传
  upload: function (e) {
    const maxlen = 5;
    var that = this;
    console.log(e)
    wx.chooseImage({
      count: maxlen - this.data.uploadimgNum,
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 指定图片来源是相册还是相机， 默认二者都有
      success: function (res) {
        console.log(res.tempFilePaths)
        const temp = res.tempFilePaths;
        const uploadimgList = that.data.uploadimgList.concat(temp);  // 页面显示图片列表
        that.photoList = that.photoList.concat(res.tempFiles);

        that.setData({
          uploadimgList: uploadimgList,
          uploadimgNum: uploadimgList.length,
          imagePath: uploadimgList[0]
        })

        that.photoList.forEach(photo => {
          if (typeof (photo.id) == "undefined") {
            console.log(photo.path)
            ActivityPhoto.create("photo", photo.path).then(result => {
              photo.id = result.id
            })
          }
        })
      },
    })
  },


  // 活动图片删除
  deleteImg: function (e) {
    console.log(this.photoList)
    let number = e.currentTarget.dataset.num
    let delphoto = this.photoList[number]
    ActivityPhoto.delete(delphoto.id).then(result => {
      this.data.uploadimgList.splice(number, 1)
      this.photoList.splice(number, 1)
      this.data.uploadimgNum -= 1
      this.setData({
        uploadimgList: this.data.uploadimgList,
        uploadimgNum: this.data.uploadimgNum
      })
    })
  },


  // 二维码生成图片
  // createCanvas: function (that) {

  //   const ctx = wx.createCanvasContext('shareCanvas')

  //   let canWidth = that.data.windowWidth - 40;
  //   let canHeight = that.data.windowHeight * 0.8 - 30;

  //   console.log(canWidth, canHeight)
  //   ctx.drawImage(that.data.imageBG, 0, 0, canWidth, canHeight)//白背景
  //   ctx.drawImage(that.data.imagePath, 15, canHeight * 0.1, canWidth - 30, canHeight * 0.4)//主题
  //   ctx.drawImage(that.data.imageEwm, canWidth * 0.35, canHeight * 0.67, canWidth * 0.32, canHeight * 0.23)//二维码
  //   ctx.drawImage(that.data.imagePortrait, canWidth * 0.029, canWidth * 0.029, canWidth * 0.08, canWidth * 0.08)
  //   ctx.setTextAlign('center') // 文字居中
  //   ctx.setFillStyle('#000000') // 文字颜色：黑色
  //   ctx.setFontSize(16) // 文字字号：16px
  //   ctx.fillText(that.data.title_name, canWidth * 0.18, canWidth * 0.09)
  //   ctx.stroke()
  //   ctx.rect(15, canHeight * 0.58, 28, 20)
  //   ctx.setFillStyle('#3bb1ff')
  //   ctx.fill()
  //   ctx.setTextAlign('center') // 文字居中
  //   ctx.setFillStyle('#000000') // 文字颜色：黑色
  //   ctx.setFontSize(12) // 文字字号：16px
  //   ctx.fillText(that.data.discount, 30, canHeight * 0.61)
  //   ctx.setTextAlign('center') // 文字居中
  //   ctx.setFillStyle('#000000') // 文字颜色：黑色
  //   ctx.setFontSize(16) // 文字字号：16px
  //   ctx.fillText(that.data.course_name, canWidth * 0.38, canHeight * 0.615)
  //   ctx.setTextAlign('center') // 文字居中
  //   ctx.setFillStyle('#000000') // 文字颜色：黑色
  //   ctx.setFontSize(10) // 文字字号：16px
  //   ctx.fillText("活动优惠价", canWidth * 0.87, canHeight * 0.60)
  //   ctx.setTextAlign('center') // 文字居中
  //   ctx.setFillStyle('red') // 文字颜色：黑色
  //   ctx.setFontSize(16) // 文字字号：16px
  //   ctx.setLineWidth(10)
  //   ctx.fillText("￥" + that.data.price, canWidth * 0.84, canHeight * 0.65)
  //   ctx.setTextAlign('center') // 文字居中
  //   ctx.setFillStyle('#000000') // 文字颜色：黑色
  //   ctx.setFontSize(14) // 文字字号：16px
  //   ctx.fillText(that.data.activity_tips, canWidth * 0.5, canHeight * 0.94)
  //   ctx.draw()
  //   that.setData({
  //     showCanvas: false
  //   })
  // },
  createCanvas: function (that) {

    const ctx = wx.createCanvasContext('shareCanvas')

    let canWidth = that.data.windowWidth - 40;
    let canHeight = that.data.windowHeight * 0.8 - 30;

    console.log(canWidth, canHeight)
    ctx.drawImage(that.data.imageBG, 0, 0, canWidth, canHeight)//白背景
    ctx.drawImage(that.data.imagePath, 15, canHeight * 0.1, canWidth - 30, canHeight * 0.4)//主题
    ctx.drawImage(that.data.imageEwm, canWidth * 0.35, canHeight * 0.62, canWidth * 0.32, canWidth * 0.32)//二维码
    // ctx.drawImage(that.data.imageEwm, canWidth * 0.35, canHeight * 0.65)//二维码
    ctx.drawImage(that.data.imagePortrait, canWidth * 0.029, canWidth * 0.029, canWidth * 0.08, canWidth * 0.08)
    ctx.setTextAlign('center') // 文字居中
    ctx.setFillStyle('#000000') // 文字颜色：黑色
    ctx.setFontSize(16) // 文字字号：16px
    ctx.fillText(that.data.title_name, canWidth * 0.18, canWidth * 0.09)
    ctx.stroke()
    ctx.rect(15, canHeight * 0.54, 28, 20)
    ctx.setFillStyle('#3bb1ff')
    ctx.fill()
    ctx.setTextAlign('center') // 文字居中
    ctx.setFillStyle('#000000') // 文字颜色：黑色
    ctx.setFontSize(12) // 文字字号：16px
    ctx.fillText(that.data.discount, 30, canHeight * 0.57)
    ctx.setTextAlign('center') // 文字居中
    ctx.setFillStyle('#000000') // 文字颜色：黑色
    ctx.setFontSize(16) // 文字字号：16px
    ctx.fillText(that.data.course_name, canWidth * 0.38, canHeight * 0.575)
    ctx.setTextAlign('center') // 文字居中
    ctx.setFillStyle('#000000') // 文字颜色：黑色
    ctx.setFontSize(10) // 文字字号：16px
    ctx.fillText("活动优惠价", canWidth * 0.87, canHeight * 0.56)
    ctx.setTextAlign('center') // 文字居中
    ctx.setFillStyle('red') // 文字颜色：黑色
    ctx.setFontSize(16) // 文字字号：16px
    ctx.setLineWidth(10)
    ctx.fillText("￥" + that.data.valueActivity, canWidth * 0.84, canHeight * 0.61)
    ctx.setTextAlign('center') // 文字居中
    ctx.setFillStyle('#000000') // 文字颜色：黑色
    ctx.setFontSize(14) // 文字字号：16px
    ctx.fillText(that.data.activity_tips, canWidth * 0.5, canHeight * 0.90)
    ctx.draw()
    that.setData({
      showCanvas: false
    })
  },

  // 取消按钮
  hideCanvas: function () {
    this.setData({
      showCanvas: true
    })
  },

  //保存图片
  saveImg: function () {
    const wxCanvasToTempFilePath = this.promisify(wx.canvasToTempFilePath)
    const wxSaveImageToPhotosAlbum = this.promisify(wx.saveImageToPhotosAlbum)

    wxCanvasToTempFilePath({
      canvasId: 'shareCanvas'
    }, this).then(res => {
      return wxSaveImageToPhotosAlbum({
        filePath: res.tempFilePath
      })
    }).then(res => {
      wx.showToast({
        title: '已保存到相册'
      })
    })
  },



  promisify: api => {
    return (options, ...params) => {
      return new Promise((resolve, reject) => {
        const extras = {
          success: resolve,
          fail: reject
        }
        api({
          ...options,
          ...extras
        }, ...params)
      })
    }
  },


  //生成图片
  showCanvas: function () {
    this.new_submit();
    this.setData({
      showCanvas: false
    })
  },


  // 取消按钮
  hideCanvas: function () {
    this.setData({
      showCanvas: true
    })
  },
  //保存图片
  saveImg: function () {
    const wxCanvasToTempFilePath = this.promisify(wx.canvasToTempFilePath)
    const wxSaveImageToPhotosAlbum = this.promisify(wx.saveImageToPhotosAlbum)

    wxCanvasToTempFilePath({
      canvasId: 'shareCanvas'
    }, this).then(res => {
      return wxSaveImageToPhotosAlbum({
        filePath: res.tempFilePath
      })
    }).then(res => {
      wx.showToast({
        title: '已保存到相册'
      })
      wx.navigateBack({
        delata: 1
      })
    })
  },
  //返回
  goback: function () {
    
      wx.navigateBack({
        delata: 1
      })
    
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // 计算 scrollView 高度，scrollView 无法用 flex: 1 撑满页面
    const res = wx.getSystemInfoSync()
    const windowHeight = res.windowHeight;//窗口可视高
    const windowWidth = res.windowWidth;//窗口可视宽
    const statusBarHeight = res.statusBarHeight
    let query = wx.createSelectorQuery().in(this);
    query.select('.navbar').boundingClientRect(); // 查询头部导航栏
    query.exec((res) => {
      let navbarHeight = res[0].height;
      let contentHeight = windowHeight - statusBarHeight - navbarHeight;
      console.log(windowHeight, windowWidth)
      this.setData({
        windowHeight,
        windowWidth,
        statusBarHeight,
        contentHeight

      });
    });
    //加载活动详情信息
    var that=this
    wx.request({
      // url: 'http://192.168.3.135:8000/activites/activityinfo/?aid=' +options.activity_id,
      url: host+'/activites/activityinfo/?aid=' + options.activity_id,
      method:'GET',
      success(res){
        console.log(res.data.activity)
        const activity = res.data.activity
        const activity_price_deposit = parseFloat(activity.activity_price_deposit)
        const activity_price_deposit_ = activity_price_deposit - (activity_price_deposit * 0.006)
        const backprice = activity_price_deposit_ / 2
        that.setData({
          activity:res.data.activity,
          num:res.data.number,
          backprice:backprice,
          isShow:false
        })
      }
    })
  },



  //分享链接
  goShareLink() {
    if(wx.getStorageSync('userid')){
      console.log(111111111111111)
      let that = this
      let activity_id = that.data.activity.id
      let scene = String(activity_id + ',' + app.globalData.user_id)
      wx.navigateTo({
        url: '/pages/scan/scan?flag=1&scene=' + scene,
      })
    }else{
      wx.navigateTo({
        url: '/pages/accredit/accredit'
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

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function (option) {

  }







})