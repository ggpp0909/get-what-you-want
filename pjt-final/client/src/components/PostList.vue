<template>
  <div>
    <h1>PostList</h1>
    <div
      v-for="post in posts"
      :key="post.id"
    >
      <h1 @click="postDetail(post.id)">{{ post.title }}
      </h1>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'PostList',
  data() {
    return {
      posts: null,
    }
  },
  methods: {
    // 클릭한 게시글로 이동 
    postDetail(id) {
      this.$router.push({ name: 'PostDetail', params: { postNum: id } })
    },
    // 전체 게시글 서버에서 불러오기 
    getPosts() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/community/`,
      })
        .then(res => {
          this.posts = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created() {
    this.getPosts()
  }
}
</script>

<style>

</style>