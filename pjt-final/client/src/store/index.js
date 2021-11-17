import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    posts: [
      { 
        id: 1,
        title: 'temp',
        content: 'temp323423423'
      },
      { 
        id: 2,
        title: 'temp2',
        content: 'temp31234',
      }
    ],
    userInfo: null,
  },
  mutations: {
    SET_TOKEN(state, userInfo) {
      state.userInfo = userInfo
    }
  },
  actions: {
    setToken({ commit }) {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      commit('SET_TOKEN', [token, config])
    },
    // getPosts() {
    //   this.$axios({
    //     method: 'get',
    //     url: `${SERVER_URL}/community/`,
    //     headers: this.setToken()
    //   })
    //     .then(res => {
    //       this.posts = res.data
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // }
  },
  modules: {
  }
})
