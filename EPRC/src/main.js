// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Router from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import echarts from 'echarts'
import scroll from 'vue-seamless-scroll'
import store from './store'
import { historyPost } from "./api/api";

Vue.use(ElementUI)
Vue.use(scroll)
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false
Vue.use(Router)

const originalPush = Router.prototype.push
Router.prototype.push = function push(location) { return originalPush.call(this, location).catch(err => err) }
// // 路由全局前置钩子(路由守卫)
router.beforeEach((to, from, next) => {
  // 判断localstorage有没有token值,如果有就放行，没有就判断用户访问的是不是Login页面
  // 如果是放行，如果不是就强行跳转到login页面



  // store.commit('changeHistory',to.path)

  let history_info = {}
  if (store.state.indexNum == 0) {
    if (to.path == '/topThree' || to.path == '/topTwo'){
      history_info.path = to.path
      history_info.chain = store.state.indexTab
      history_info.query=store.state.activeIndexVal
    }else{
      history_info.path = to.path
      history_info.chain = store.state.indexTab
    }
  } else if (store.state.indexNum == 1) {
    history_info.path = to.path
    history_info.chain = store.state.queryTitle

  } else {
    let list = ['我的收藏', '我的追踪', '浏览记录', '信息修改']
    history_info.path = to.path
    history_info.chain = list[store.state.mineTab]
  }
  console.log(history_info)
  // historyPost({
  //   user_id: localStorage.getItem('user_id'),
  //   history_info: history_info,
  //   type: store.state.indexNum
  // }).then(res => { })
  // console.log(from,to.path,store.state.queryTitle,store.state.mineTab,store.state.indexTab,store.state.indexNum)

  let token = localStorage.getItem("token") || ""
  if (token) {
    next()
  } else {
    if (to.path !== "/login") {
      next({ path: "/login" })
    } else {
      next()
    }
  }
})
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
