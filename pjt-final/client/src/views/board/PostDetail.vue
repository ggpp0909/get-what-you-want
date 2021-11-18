<template>
  <div>
    <!-- <h1>{{ post.title }}</h1>
    {{ post.content }} -->
    <h1>detail</h1>
    <div v-if="isSameUser">
      <button>update</button>
      <button>delete</button>
    </div>
    <comment-list></comment-list>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CommentList from '@/components/CommentList'

export default {
  name: 'PostDetail',
  components: {
    CommentList
  },
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
  created() {
    this.getPost() // 영화 디테일 불러오기 
    console.log(this.post)
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