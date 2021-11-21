<template>
  <v-app>
    <v-app-bar absolute color="white" shrink-on-scroll scroll-target="#scrolling-techniques-2"
      class="application"
    >
      <!-- home -->
      <router-link :to="{ name: 'Home' }" 
        class="text-decoration-none black--text"
      >HOME</router-link>

      <v-spacer></v-spacer>
      <!-- 자유게시판 -->
      <router-link :to="{ name: 'Board' }" 
        class="text-decoration-none black--text mx-3"
      >BOARD</router-link>
      <!-- 영화 추천 -->
      <router-link :to="{ name: 'MovieRecommend' }"
        class="text-decoration-none black--text mx-3"
      >RECOMMEND</router-link>
      <!-- 검색창 -->
      <div>
        <input v-model="searchMovie" @keyup.enter="goToSearchPage" @click="searchMovie=''" type="text">
      </div>

      <!-- 로그인-->
      <div v-if="userName">
        <router-link :to="{ name: 'Profile', params: { userName: this.userName } }"
          class="text-decoration-none black--text"
        >Profile</router-link>
        <router-link to="#" @click.native="logout"
          class="text-decoration-none black--text"
        >Logout</router-link>
      </div>
      <!-- 프로필 이미지 -->
      <div v-else>
        <v-menu bottom min-width="150px" rounded offset-y>
          <template v-slot:activator="{ on }">
            <v-btn icon x-large v-on="on">
              <v-avatar color="white" size="48">
                <!-- <span class="black--text text-h5">JS</span> -->
                <!-- 로그인 -->
                <img :src="require(`@/assets/money.png`)" alt="유저로필" height="70" v-if="userName">
                <!-- 비로그인 -->
                <img :src="require(`@/assets/어피치.png`)" alt="기본프로필" height="70" v-else>
              </v-avatar>
            </v-btn>
          </template>
        <!-- 프로필 이미지 눌렀을때 메뉴 -->
          <v-card>
            <v-list-item-content class="justify-center">
              <!-- 로그인 -->
              <div class="mx-auto text-center" v-if="userName">
                <v-btn depressed rounded text>
                  <router-link :to="{ name: 'Profile', params: { userName: this.userName } }"
                    class="text-decoration-none black--text"
                  >MY PROFILE</router-link>
                </v-btn>
                <v-divider class="my-3"></v-divider>
                <v-btn depressed rounded text>
                  <router-link :to="{ name: 'ChangeProfile' }"
                    class="text-decoration-none black--text"
                  >SETTING</router-link>
                </v-btn>
                <v-divider class="my-3"></v-divider>
                <v-btn depressed rounded text>
                  <router-link to="#" @click.native="logout"
                    class="text-decoration-none black--text"
                  >LOGOUT</router-link>
                </v-btn>
              </div>
              <!-- 비로그인 -->
              <div class="mx-auto text-center" v-else>
                <v-btn depressed rounded text>
                  <router-link :to="{ name: 'Signup' }"
                    class="text-decoration-none black--text mx-3"
                  >SIGNUP</router-link>
                </v-btn>
                <v-divider class="my-3"></v-divider>
                <v-btn depressed rounded text>
                  <router-link :to="{ name: 'Login' }"
                    class="text-decoration-none black--text mx-3"
                  >LOGIN</router-link>
                </v-btn>
              </div>
            </v-list-item-content>
          </v-card>
        </v-menu>
      </div>
    </v-app-bar>

    <v-sheet
      id="scrolling-techniques-2"
      class="overflow-y-auto"
      max-height="100vh"
    >
      <v-container style="height: 1000px;">
        <router-view :key="$route.fullPath"/>
      </v-container> 
    </v-sheet>
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


<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display+SC:wght@700&display=swap');
.application {
  font-family: 'Playfair Display SC', serif;
}
</style>