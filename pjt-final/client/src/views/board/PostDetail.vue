<template>
  <div>
    <h1>{{ post.title }}</h1>
    {{ post.content }}
    <div v-if="isSameUser">
      <button>update</button>
      <button>delete</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'PostDetail',
  computed: {
    ...mapState([
      'post',
      'userName'
    ])
  },
  data() {
    return {
      isSameUser: false,
    }
  },
  methods: {
    deletePost() {
      this.$store.dispatch('getPostItem', 'delete', this.post.id)
    },
    getPost() {
      this.$store.dispatch('getPostItem', 'get', this.post.id)
    }
  },
  create() {
    'getPost' // 영화 디테일 불러오기 
    // 조회하는 유저와 게시글을 작성한 유저가 같은지 보기 
    if (this.userName === this.post.id) {
      this.isSameUser = true
    }
  }
  // create() {
  //   this.$store.dispatch('getPostItem', 'get', this.post.id)
  // }
  // created() {
  //   const postItem = this.posts.filter(postDetail => {
  //     return postDetail.id === Number(this.$route.params.postNum)
  //   })[0]
  //   this.title = postItem.title
  //   this.content = postItem.content
  // }
}
</script>

<style>

</style>