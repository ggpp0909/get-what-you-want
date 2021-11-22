<template>
  <v-container>
    <v-row >
      <v-col md="2"><h1>BOARD</h1></v-col>
      <v-col md="4" offset-md="6" class="searchInput">
        <v-text-field v-model.trim="searchMovie" @keyup.enter="searchPost" 
            placeholder="검색어를 입력하세요" dense flat shaped label="Search Movie">
          <v-icon slot="append" @click="searchPost">mdi-magnify</v-icon>
        </v-text-field>
      </v-col>
    </v-row>
  <post-list :is-post="isPost"></post-list>
  <b-button @click="postCreate" squared variant="outline-dark">Create</b-button>
  </v-container>
</template>

<script>
  import PostList from '@/components/PostList'

  const SERVER_URL = process.env.VUE_APP_SERVER_URL

  export default {
    name: 'Board',
    components: {
      PostList,
    },
    data() {
      return {
        searchKeyword: null,
        searchBeforeKeyword: null,
        isPost: true,
      }
    },
    methods: {
      postCreate() {
        const token = localStorage.getItem('jwt')
        if (token) { // 로그인 상태 -> 게시글 생성 
          this.$router.push({ name: 'PostCreate', params: { postId: 0 }})
        } else {    // 비로그인 상태 -> 로그인 
          this.$router.push({ name: 'Login' })
        }
      },
    },
    // 게시글 검색
    searchPost() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/community/${this.searchKeyword}/search/`,
      })
        .then(res => {
          this.posts = res.data
          console.log(res)
          this.isPost = this.posts.length > 0 ? true : false
          this.searchBeforeKeyword = this.searchKeyword
          this.searchKeyword = null
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
</script>

<style scoped>
.searchInput {
  margin-bottom: -30px;
}
</style>