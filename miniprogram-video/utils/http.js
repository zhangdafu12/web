// 获取请求头信息
const getHeader = (raw) => {
  const header = {}
  if (!raw) {
    const token = wx.getStorageSync('token')
    if (token) {
      header.Authorization = `Bearer ${token}`
    }
  }
  return header
}

// 处理未认证请求
const handleUnauth = () => {
  getApp().login()
}

// 显示错误信息弹窗
const showErrToast = (e) => {
  wx.showToast({
    title: e,
    icon: 'none',
    duration: 3000
  })
}

// 调试输出
const log = (method, url, result) => {
  const date = new Date()
  const timeStr = date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
  console.log(timeStr + ' ' + method + ' ' + url)
  console.log(result)
}

// 获取 promise 对象
const getPromise = (method, url, {
  // 可选参数
  data = {},
  fileName = '', // 同时指定 fileName 和 filePath, 且 method 为 post, 则调用 wx.uploadFile 上传文件
  filePath = '',
  raw = false, // true: header 中不加 token, result 不处理直接返回
  showLoading = false // true: 加载过程中显示动画
} = {}) => {
  return new Promise((resolve, reject) => {
    if (showLoading) { // 显示加载动画
      wx.showLoading({
        title: '加载中...'
      })
    }
    if (fileName != '' && filePath != '' && method == 'POST') { // 上传文件
      wx.uploadFile({
        url: url,
        header: getHeader(raw),
        filePath,
        name: fileName,
        formData: data,
        success: (result) => {
          log(method, url, result)
          if (raw) {
            resolve(result)
          } else {
            resolve(JSON.parse(result.data)) // 坑，此方法的 data 被强转成了 str
          }
        },
        fail: () => {
          reject('网络异常，请稍后重试')
        },
        complete: () => {
          if (showLoading) {
            wx.hideLoading()
          }
        }
      })
    } else { // 普通请求
      wx.request({
        url: url,
        data: data,
        header: getHeader(raw),
        method: method,
        success: (result) => {
          log(method, url, result)
          // 处理响应
          if (raw) {
            resolve(result)
          } else {
            const code = result.statusCode.toString()
            if (code.startsWith('2')) { // 请求成功
              resolve(result.data)
            } else if (code === '401') { // 未认证或 token 失效
              handleUnauth()

            } else { // 其他状态码
              const errMsg = '请求异常，响应码：' + code
              reject(errMsg)
            }
          }
        },
        fail: (err) => {
          reject('网络异常，请稍后重试')
        },
        complete: () => {
          if (showLoading) {
            wx.hideLoading()
          }
        }
      })
    }
  }).catch((e) => {
    console.log(e)
    showErrToast(e)
  })
}

// 封装 http 对象
const Http = {
  get: (url, options) => {
    return getPromise('GET', url, options)
  },
  post: (url, options) => {
    return getPromise('POST', url, options)
  },
  put: (url, options) => {
    return getPromise('PUT', url, options)
  },
  delete: (url, options) => {
    return getPromise('DELETE', url, options)
  }
}

export default Http