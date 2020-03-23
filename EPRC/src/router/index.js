import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home/home'
import topOne from '@/components/home/topOne'
import topTwo from '@/components/home/topTwo'
import topThree from '@/components/home/topThree'
import topFour from '@/components/home/topFour'
import topFive from '@/components/home/topFive'

import login from '@/components/login'
import query from '@/components/query/query'
import singleAccount from '@/components/query/singleAccount'
import relevance from '@/components/query/relevance'
import transaction from '@/components/query/transaction'
import trendChart from '@/components/query/trendChart'
import exchange from '@/components/query/exchange'

import mine from '@/components/mine/mine'
import favorite from '@/components/mine/favorite'
import trace from '@/components/mine/trace'
import record from '@/components/mine/record'
import amend from '@/components/mine/amend'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      name:'home',
      component:home,
      children: [{
        path: '',
        component: topOne
      },{
        path: 'topTwo',
        component: topTwo
      },{
        path: 'topThree',
        component: topThree
      },{
        path: 'topFour',
        component: topFour
      },{
        path: 'topFive',
        component: topFive
      }]
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/query',
      component: query,
      redirect: '/singleAccount',
      children: [
        { path: '/singleAccount', name: 'singleAccount', component: singleAccount },
        { path: '/relevance', name: 'relevance', component: relevance },
        { path: '/transaction', name: 'transaction', component: transaction },
        { path: '/trendChart', name: 'trendChart', component: trendChart },
        { path: '/exchange', name: 'exchange', component: exchange },

      ]

    },
    {
      path: '/mine',
      component: mine,
      redirect: '/favorite',
      children: [
        { path: '/favorite', name: 'favorite', component: favorite },
        { path: '/trace', name: 'trace', component: trace },
        { path: '/record', name: 'record', component: record },
        { path: '/amend', name: 'amend', component: amend },
      ]

    },
  ]
})
