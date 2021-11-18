<template>
  <div>
    <h1>{{ post.title }}</h1>
    {{ post.content }}
    <p>마지막 수정일 :{{ post.updated_at }}</p>
    <p>작성일 : {{ post.created_at }}</p>

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

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'PostDetail',
  components: {
    CommentList
  },
  data() {
    return {
      post: null,
      isSameUser: false,
    }
  },
  computed: {
    ...mapState([
      'userName',
      'token'
    ])
  },
  methods: {
    getPost() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/community/${this.$route.params.postNum}/`, 
      })
        .then(res => {
          this.post = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deletePost() {
      this.$store.dispatch('getPostItem', 'delete', this.post.id)
    },
  },
  created() {
    this.getPost() // 영화 디테일 불러오기 
    if (this.userName === this.post.username) {
      this.isSameUser = true
    }
  }
}
</script>

<style>

</style>