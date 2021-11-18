<template>
  <div>
    <h1>{{ post.title }}</h1>
    {{ post.content }}
    <p>마지막 수정일 :{{ post.updated_at }}</p>
    <p>작성일 : {{ post.created_at }}</p>

    <div v-if="isSameUser">
      <button>update</button>
      <button @click="deletePost">delete</button>
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
    // 게시글 가져오기 
    getPost() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/community/${this.$route.params.postNum}/`, 
      })
        .then(res => {
          this.post = res.data
          // 지금 로그인한 유저가 글쓴 유저인지 
          if (this.userName === res.data.user.username) {
            this.isSameUser = true
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 게시글 삭제 
    deletePost() {
      const config = {
        Authorization: `JWT ${this.token}` // 이렇게 header에 함께 보내준다. 
      }
      console.log(this.token)
      this.$axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${this.$route.params.postNum}/`, 
        headers: config
      })
        .then(() => {
          this.$router.push({ name: 'Board' })
        })
        .catch(err => {
          console.log(err)
        })
    },

  },
  created() {
    this.getPost() // 영화 디테일 불러오기 

    // console.log(this.post)
    // console.log(this.userName)
    // console.log(this.post.username)
    // 
  }
}
</script>

<style>

</style>