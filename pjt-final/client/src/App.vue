<template>
  <v-app>
    <v-app-bar
      absolute
      color="white"
      shrink-on-scroll
      scroll-target="#scrolling-techniques-2"
    >
    
      <router-link :to="{ name: 'Home' }" class="text-button">HOME</router-link>
       <v-spacer></v-spacer>
      <router-link :to="{ name: 'Board' }">Board</router-link> |
      <router-link :to="{ name: 'MovieRecommend' }">MovieRecommend</router-link> |
      <div v-if="userName">
        <router-link :to="{ name: 'Profile', params: { userName: this.userName } }">Profile</router-link> |
        <router-link to="#" @click.native="logout">Logout</router-link>
      </div>
      <div v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> | 
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </div>
      <div>
        <input v-model="searchMovie" @keyup.enter="goToSearchPage" @click="searchMovie=''" type="text">
      </div>
    </v-app-bar>

    <v-container
      id="scrolling-techniques-2"
      class="overflow-y-auto"
      max-height="300"
    >
      <router-view :key="$route.fullPath"/>
    </v-container>
  </v-app>
</template>

<script>
import { mapState } from 'vuex'


export default {
  name: 'App',
  data: function () {
    return {
      searchMovie: '',
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('jwt')
      this.$store.dispatch('deleteUserName')
      this.$router.push({ name: 'Login' })
    },
    goToSearchPage() {
      this.$router.push({ name: 'SearchMovie', params: { keyword: this.searchMovie } }).catch(()=> {})

    }
  },
  computed: {
    ...mapState(['userName'])
  }
}
</script>
