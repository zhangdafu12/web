import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {//data数据存放
    count: [
        { id: 1, text: '...', done: true }
    ],
    userInfo:{
        tel:window.localStorage.getItem('tel'),
        username:window.localStorage.getItem('user_name'),
        icon:window.localStorage.getItem('icon'),
        // tel:'',
        // username:'',
        // icon:'',
    },
    
    indexNum:0,//排行榜查询我的等选项
    loginState:false,//登录状态
    mineTab:0,//我的默认导航
    indexTab:'公链交易量top10',
    params:{
            chain:'bch',
            time_unit:'1h',
            Time_tange:'1h'
    },
    activeIndex: "1",//首页默认导航
    activeIndexVal:'',//首页次级菜单
    queryIndex:'0',//查询默认导航
    queryTitle:'单一账户查询',
    history:[],
  
},
getters: {
    // 可以认为是 store 的计算属性
    //调用this.$store.getters.doneTodos
    doneTodos: state => {
        return state.count.filter(todo => todo.done)
    },
    //调用this.$store.getters.getTodoById(2) 
    getTodoById: (state) => (id) => {
        return state.todos.find(todo => todo.id === id)
    },
   
},
mutations: {//修改方法，同步的icon
    increment(state, payload) {
        state.count += payload.amount
    },
    changeUserInfoIcon: (state,url) =>{
        return state.userInfo.icon=url
    },
    changeUserInfoTel: (state,tel) =>{
        return state.userInfo.tel=tel
    },
    changeUserInfoUsername: (state,name) =>{
        return state.userInfo.username=name
    },
    changeIndexNum: (state, id) =>{
        return state.indexNum=id
    },
    changeLoginState:(state,bool)=>{
        return state.loginState=bool
    },
    changeMineTab:(state,num)=>{
        return state.mineTab=num
    },
    changeIndexTab:(state,str)=>{
        return state.indexTab=str
    },
    changeParams:(state,obj)=>{
        return state.params=obj
    },
    changeActiveIndex:(state,str)=>{
        return state.activeIndex=str
    },
    changeActiveIndexVal:(state,str)=>{
        return state.activeIndexVal=str
    },
    changeQueryIndex:(state,num)=>{
        return state.queryIndex=num
    },
    changeQueryTitle:(state,str)=>{
        return state.queryTitle=str
    },
    changeHistory:(state,str)=>{
        return state.history.push(str)
    }
   
   
    //使用commit(方法名，要修改为的值)   
    //   this.$store.commit('increment', {
    //     amount: 10
    //   })   
},
actions: {//修改方法，异步的，
    ISLOGINACTION({ commit }, payload) {
        commit('ISLOGIN', payload)
    }
    // this.$store.dispatch('ISLOGINACTION')
},
modules: {
    //   store.state.a // -> moduleA 的状态
    // store.state.b // -> moduleB 的状态   
}
})
