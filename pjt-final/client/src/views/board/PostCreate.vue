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
    <button @click="uploadPost">done</button>
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
    uploadPost() {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/community/create/`,
        data: this.post
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