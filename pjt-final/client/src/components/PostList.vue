<template>
  <div>
    <h1>PostList</h1>
    <div v-if="isPost">
      <div
        v-for="post in posts"
        :key="post.id"
      >
        <h1 @click="postDetail(post.id)">{{ post.title }}</h1>
      </div>
    </div>
    <div v-else>
      <h1>{{ this.searchBeforeKeyword }}에 해당하는 게시글이 없습니다.</h1>
    </div>
    <input type="text" v-model.trim="searchKeyword" placeholder="찾으려는 게시글의 제목을 입력해주세요" @keyup.enter="searchSearch">
    <button @click="searchSearch">검색</button>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'PostList',
  data() {
    return {
      posts: null,
      searchKeyword: null,
      searchBeforeKeyword: null,
      isPost: true,
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
    },
    // 게시글 검색
    searchSearch() {
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
    }
  },
  created() {
    this.getPosts()
  }
}
</script>

<style>

</style>