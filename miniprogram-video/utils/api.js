import Http from '../utils/http'

const host = 'https://www.heiyunworld.com:8800'
// const host = 'http://192.168.3.43:8000'
// const host = 'http://192.168.3.169:8000'
// const host = 'http://192.168.10.51:8000'
// const host = 'http://localhost:8000'
// const host= 'http://192.168.3.30:8000'
// 用户信息
export const User = {
  retrieve: (id) => {
    return Http.get(`${host}/user/${id}/`)
  },
}

// Token 相关
export const Token = {
  obtain: (data) => {
    return Http.post(`${host}/token/`, {
      data,
      raw: true
    })
  },
  check: () => {
    return Http.get(`${host}/check/`)
  }
}

// 注册接口
export const register = (data) => {
  return Http.post(`${host}/register/`, {
    data,
    raw: true
  })
}

// V币余额查询接口
export const Account = {
  get: () => {
    return Http.get(`${host}/account/`)
  }
}

// 账单接口
export const Bill = {
  list: () => {
    return Http.get(`${host}/bill/`, {
      showLoading: true
    })
  }
}

// 机构相关接口
export const Institution = {
  create: (data) => { // 上传机构入驻申请
    return Http.post(`${host}/institution/`, {
      data,
      showLoading: true
    })
  },
  retrieve: (id) => { // 机构信息
    return Http.get(`${host}/institution/${id}/`, {
      showLoading: true
    })
  },
  update: (id, data) => { // 更新机构信息
    return Http.put(`${host}/institution/${id}/`, {
      data
    })
  },
  list: (params) => {
    return Http.get(`${host}/institution/`, {
      showLoading: true,
      data: params
    })
  },
  // search: (params) => {
  //   return Http.get(`${host}/institution/`, {
  //     data: params
  //   })
  // },
  uploadAvatar: (id, fileName, filePath) => { // 上传机构头像
    return Http.post(`${host}/institution/${id}/avatar/`, {
      fileName,
      filePath
    })
  },
  getDetail: (id) => { // 机构详细信息
    return Http.get(`${host}/institution/${id}/detailed/`, {
      showLoading: true
    })
  },
  collect: (id) => { // 收藏
    return Http.post(`${host}/institution/${id}/collect/`)
  },
  cancelCollect: (id) => { // 取消收藏
    return Http.delete(`${host}/institution/${id}/collect/`)
  }
}

// 机构视频相关接口
export const Video = { // 上传视频
  create: (fileName, filePath, data) => {
    return Http.post(`${host}/video/`, {
      data,
      fileName,
      filePath,
      showLoading: true
    })
  },
  retrieve: (id) => { // 视频信息
    return Http.get(`${host}/video/${id}/`)
  },
  list: (data) => { // 视频列表
    return Http.get(`${host}/video/`, {
      data,
      showLoading: true
    })
  },
  like: (id) => { // 点赞
    return Http.post(`${host}/video/${id}/like/`)
  },
  cancelLike: (id) => { // 取消点赞
    return Http.delete(`${host}/video/${id}/like/`)
  },
  record: (id, data) => {
    return Http.post(`${host}/video/${id}/record/`, {
      data
    })
  }
}

// 历史记录接口
export const History = {
  list: () => {
    return Http.get(`${host}/history/`, {
      showLoading: true
    })
  }
}

// 评论接口
export const Comment = {
  create: (data) => {
    return Http.post(`${host}/comment/`, {
      data,
      showLoading: true
    })
  },
  list: (params) => {
    return Http.get(`${host}/comment/`, {
      data: params
    })
  }
}


// 机构活动接口
export const Activity = {
  create: (data) => {
    return Http.post(`${host}/activity/`, {
      data,
      showLoading: true
    })
  },
  list: (params) => {
    return Http.get(`${host}/activity/`, {
      data: params
    })
  },
  delete: (id) => {
    return Http.delete(`${host}/activity/${id}/`)
  },
  update: (id, data) => { 
    return Http.put(`${host}/activity/${id}/`, {
      data
    })
  },
  retrieve: (id) => {
    return Http.get(`${host}/activity/${id}/`)
  }
}


// 机构活动图片接口
export const ActivityPhoto = {
  create: (fileName, filePath) => {
    return Http.post(`${host}/activity_photo/`, {
      fileName,
      filePath,
    })
  },
  delete: (id) => {
    return Http.delete(`${host}/activity_photo/${id}/`)
  },
}
// 机构图片接口
export const InstitutionImage = {
  create: (fileName, filePath) => {
    // return Http.post(`${host}/institutionimage/`, {
    //   fileName,
    //   filePath,
    // })
    return Http.post(`${host}/institutionimage/`, {
      fileName,
      filePath,
    })
  },
  delete: (id) => {
    return Http.delete(`${host}/institutionimage/${id}/`)
  },
}


// 活动报名记录接口
export const ApplyRecord = {
  create: (data) => {
    return Http.post(`${host}/apply_record/`, {
      data,
      showLoading: true
    })
  },
  delete: (id) => {
    return Http.delete(`${host}/apply_record/${id}/`)
  },
  update: (id, data) => {
    return Http.put(`${host}/apply_record/${id}/`, {
      data
    })
  },
  retrieve: (id) => {
    return Http.get(`${host}/apply_record/${id}/`)
  }
}

export const Order = {
  retrieve: (data) => {
    return Http.post(`${host}/wechatpay/myorder/`,{
      data
    })
  }
}


export const Lookinfo = {
  retrieve: (data) => {
    return Http.post(`${host}/wechatpay/lookinfo/`, {
      data
    })
  }
}



