<template>
  <v-container>
    <post-list></post-list>
    <b-button @click="postCreate" squared variant="outline-dark">Create</b-button>
  </v-container>
</template>

<script>
import PostList from '@/components/PostList'

export default {
  name: 'Board',
  components: {
    PostList,
  },
  methods: {
    // 게시글 작성 
    postCreate() {
      const token = localStorage.getItem('jwt')
      if (token) { // 로그인 상태 -> 게시글 생성 
        this.$router.push({ name: 'PostCreate', params: { postId: 0 }})
      } else {    // 비로그인 상태 -> 로그인 
        this.$router.push({ name: 'Login' })
      }
    },
  }
}
</script>

<style scoped>
.searchInput {
  margin-bottom: -30px;
}
</style>