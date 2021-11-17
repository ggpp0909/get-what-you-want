<template>
  <div>
    <input type="text" v-model="post.title">
    <input type="text" v-model="post.content" rows="3">
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'PostCreate',
  data() {
    return {
      post: {
        title: '',
        content: '',
        id: null,
      }
    }
  },
  computed: {
    ...mapState(['posts'])
  },
  methods: {
    uploadPost() {
      this.post.id = this.posts.length -1
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/community/create/`,
        data: this.post
      })
        .then(res => {
          this.$router.push({ name: 'PostDetail', params: { postNum: res.pk } })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>