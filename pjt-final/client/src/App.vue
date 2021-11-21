<template>
  <v-app>
    <v-app-bar color="white" absolute shrink-on-scroll scroll-target="#scrolling-techniques-2" fade-img-on-scroll prominent
      elevation="1"
      class="application">

      <!-- <template v-slot:img="{ props }">
            <img :src="require(`@/assets/test.png`)" alt="유저프로필" v-bind="props" >
          </template> -->
      <v-row>
        <!-- home -->
        <v-col cols="2">
          <router-link :to="{ name: 'Home' }" 
            class="text-decoration-none black--text" 
          >HOME</router-link>
        </v-col>
        <v-col cols="7" class="d-flex justify-center">
          <!-- 자유게시판 -->
          <div>
            <router-link :to="{ name: 'Board' }" 
              class="text-decoration-none black--text mx-3"
            >BOARD</router-link>
            <!-- 영화 추천 -->
            <router-link :to="{ name: 'MovieRecommend' }"
              class="text-decoration-none black--text mx-3"
            >RECOMMEND</router-link>
          </div>
        </v-col>
        <!-- 검색창 -->
        <v-col cols="2" >
          <v-text-field v-model.trim="searchMovie" @keyup.enter="goToSearchPage" 
            placeholder="검색어를 입력하세요" outlined dense label="Search Movie" >
          <v-icon slot="append" @click="goToSearchPage">mdi-magnify</v-icon>
          </v-text-field>
        </v-col>

        <v-col cols="1">
          <!-- 프로필 이미지 -->
          <v-menu bottom min-width="150px" rounded offset-y>
            <template v-slot:activator="{ on }">
              <v-btn icon x-large v-on="on">
                <v-avatar color="white" size="48">
                  <!-- <span class="black--text text-h5">JS</span> -->
                  <!-- 로그인 -->
                  <img :src="require(`@/assets/money.png`)" alt="유저프로필" height="70" v-if="userName">
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
                  <router-link :to="{ name: 'Profile', params: { userName: this.userName } }"
                    class="text-decoration-none black--text"
                  ><v-btn depressed rounded text>MY PROFILE</v-btn></router-link>
                  <v-divider class="my-3"></v-divider>
                  <router-link :to="{ name: 'ChangeProfile' }"
                    class="text-decoration-none black--text"
                  ><v-btn depressed rounded text>SETTING</v-btn></router-link>
                  <v-divider class="my-3"></v-divider>
                  <router-link to="#" @click.native="logout"
                    class="text-decoration-none black--text"
                  ><v-btn depressed rounded text>LOGOUT</v-btn></router-link>
                </div>
                <!-- 비로그인 -->
                <div class="mx-auto text-center" v-else>
                  <router-link :to="{ name: 'Signup' }"
                    class="text-decoration-none black--text"
                  ><v-btn depressed rounded text>SIGNUP</v-btn></router-link>
                  <v-divider class="my-3"></v-divider>
                  <router-link :to="{ name: 'Login' }"
                    class="text-decoration-none black--text"
                  ><v-btn depressed rounded text>LOGIN</v-btn></router-link>
                </div>
              </v-list-item-content>
            </v-card>
          </v-menu>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-sheet
      id="scrolling-techniques-2"
      class="overflow-y-auto padding"
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
.padding{
  padding-top:150px
}
</style>