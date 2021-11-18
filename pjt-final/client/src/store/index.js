import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  state: {
    posts: [],
    post: null,
    userName: null,
    // userInfo: null,
   
  },
  mutations: {
    SET_USERNAME(state, userName) {
      state.userName = userName
    },
    DELETE_USERNAME(state) {
      state.userName = null
    },
    GET_POSTS(state, posts) {
      state.posts = posts
    }
    // SET_TOKEN(state, userInfo) {
    //   state.userInfo = userInfo
    // }
  },
  actions: {
    // 유저 네임 저장 
    setUserName({ commit }, userName) {
      commit('SET_USERNAME', userName)
    },
    // 유저 삭제
    deleteUserName({ commit }) {
      commit('DELETE_USERNAME')
    },
    // setToken({ commit }) {
    //   const token = localStorage.getItem('jwt')
    //   const config = {
    //     Authorization: `JWT ${token}`
    //   }
    //   commit('SET_TOKEN', [token, config])
    // },
    // 자유게시판 전체 글 가져오기 
    getPosts({ commit }) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/`,
        // headers: this.state.userInfo.config
      })
        .then(res => {
          commit('GET_POSTS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 게시글 상세 조회 (메소드에 따라 삭제, 수정)
    getPostItem(method, id) {
      axios({
        method: `${method}`,
        url: `${SERVER_URL}/community/${id}/`, 
        headers: this.userInfo.config
      })
        .then(res => {
          console.log(res)
          this.state.post = res.data
          return 
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})
