import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'

import Board from '../views/Board.vue'
import PostDetail from '../components/PostDetail.vue'
import PostCreate from '../components/PostCreate.vue'

import Recommend from '../views/Recommend.vue'
import User from '../views/User.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // 자유게시판 
  {
    path: '/board',
    name: 'Board',
    component: Board
  },
  {
    path: '/board/:postNum',
    name: 'PostDetail',
    component: PostDetail
  },
  {
    path: '/board/create',
    name: 'PostCreate',
    component: PostCreate
  },
  
  // 상세 추천
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/user',
    name: 'User',
    component: User
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
