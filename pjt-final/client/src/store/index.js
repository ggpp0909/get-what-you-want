import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    userName: null,
    token: null,
    config: null,
  },
  mutations: {
    SET_USERNAME(state, userName) {
      state.userName = userName
    },
    DELETE_USERNAME(state) {
      state.userName = null
      state.token = null
      state.config = null
    },
    SET_TOKEN(state, token) {
      state.token = token
      state.config = {
        Authorization: `JWT ${token}` 
      }
    }
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
    setToken({ commit }) {
      commit('SET_TOKEN', localStorage.getItem('jwt'))
    },
  },
  modules: {
  }
})
