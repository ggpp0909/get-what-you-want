<template>
  <div>
    created
    <v-text-field v-model="post.title"
      placeholder="제목을 입력해주세요."
      color="error"
    ></v-text-field>
    <v-textarea v-model="post.content"
      color="success"
    ></v-textarea>
    <button @click="createPost">done</button>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'PostCreate',
  data() {
    return {
      post: {
        title: '',
        content: '',
      }
    }
  },
  methods: {
    createPost() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }

      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/community/`,
        data: this.post,
        headers: config
      })
        .then(res => {
          this.$router.push({ name: 'PostDetail', params: { postNum: res.pk } }) // 맘에 걸리는 부분 
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