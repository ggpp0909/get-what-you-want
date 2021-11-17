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
    ]
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
