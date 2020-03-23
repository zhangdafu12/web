import {
  QQMapConfig
} from './config'

const QQMapWX = require('../libs/qqmap-wx-jssdk.min.js')
const qqmapsdk = new QQMapWX({
  key: QQMapConfig.key
})

// 调用腾讯地图接口获取坐标所在城市
export const getCity = (latitude, longitude) => {
  return new Promise((resolve, reject) => {
    qqmapsdk.reverseGeocoder({
      location: {
        latitude,
        longitude
      },
      sig: QQMapConfig.sig,
      success: (response) => {
        if (response.status === 0) {
          const city = response.result.ad_info.city
          resolve(city)
        } else {
          reject(response)
        }
      },
      fail: (error) => {
        reject(error)
      }
    })
  })
}


const fsm = wx.getFileSystemManager()
export const base64src = (base64data, filename, cb) => {
  return new Promise((resolve, reject) => {
    const [, format, bodyData] = /data:image\/(\w+);base64,(.*)/.exec(base64data) || [];
    if (!format) {
      reject(new Error('ERROR_BASE64SRC_PARSE'))
      };
    debugger
    const filePath = `images/qrcode/${filename}.${format}`;
    const buffer = wx.base64ToArrayBuffer(bodyData);
    fsm.writeFile({
      filePath,
      data: buffer,
      encoding: 'binary',
      success() {
        cb(filePath);
      },
      fail() {
        reject(new Error("'ERROR_BASE64SRC_WRITE'"))
      }
    })
    
  })
}

