import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import left from '@/components/homeshow/left'
import right from '@/components/homeshow/right'
import clear from '@/components/homeshow/clear'
import hunt from '@/components/homeshow/hunt'
import mine from '@/components/homeshow/newmine/mine'
import paper from '@/components/homeshow/newmine/paper'
import newPage from '@/components/newPage'
import lunbo from '@/components/轮播'
import message from '@/components/homeshow/newpaper/message'
import client from '@/components/homeshow/newpaper/client'
import matter from '@/components/homeshow/newpaper/matter'
import pictures from '@/components/homeshow/newpaper/pictures'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: home,
      children:[
        {path:'',component:left,name:'home',
          children:[
            {path:'',component:mine,name:'mine'},
            {path:'paper',component:paper,
            children:[
            {path:'',component:message,name:'message'},
            {path:'client',component:client,name:'client'},
            {path:'matter',component:matter,name:'matter'},
            {path:'pictures',component:pictures,name:'pictures'},
          ]},
        ],

        },

      ]
    },
    {
      path:'/newPage',
      name:'newPage',
      component:newPage
    },
    {
      path:'/lunbo',
      name:'lunbo',
      component:lunbo
    },
    {
      path:'/clear',
      name:'clear',
      component:clear
    },
    {
      path:'/hunt',
      name:'hunt',
      component:hunt
    }
    // {path:'/right', component:right},
  ]
})
