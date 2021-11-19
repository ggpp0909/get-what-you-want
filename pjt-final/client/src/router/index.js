import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home'

// 자유게시판
import Board from '@/views/board/Board'
import PostDetail from '@/views/board/PostDetail'
import PostCreate from '@/views/board/PostCreate'

// 유저
import Profile from '@/views/accounts/Profile'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'

// 영화 
import MovieDetail from '@/views/movie/MovieDetail'
import MovieRecommend from '@/views/movie/MovieRecommend'

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
    path: '/board/create/:postId',
    name: 'PostCreate',
    component: PostCreate
  },

  // 유저
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile/:userName',
    name: 'Profile',
    component: Profile
  },

  // 영화 조회 
  {
    path: '/movie/:movieId',
    name: 'MovieDetail',
    component: MovieDetail
  },
  // 상세 추천
  {
    path: '/movie/recommend',
    name: 'MovieRecommend',
    component: MovieRecommend
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
