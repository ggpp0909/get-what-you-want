<template>
  <div>
     <v-text-field v-model.trim="content" color="error" @keyup.enter="createComment"></v-text-field>
     <button @click="createComment">+</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import swal from 'sweetalert'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentCreate',
  data() {
    return {
      content: '',
    }
  },
  props: {
    reloadComment: Function
  },
  methods: {
    createComment() {
      if (this.content === '') {
          swal ("댓글을 입력해주세요.", {
          dangerMode: true,
        })
      }
      const commentItem = {
        content: this.content
      }
      if (this.config) {
        this.$axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.$route.params.postNum}/comment_create/`,
          data: commentItem,
          headers: this.config
        })
          .then(() => {
            this.reloadComment()
            this.content = null
            // swal('하이')
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        this.$router.push({ name: 'Login' })
      }
    }
  },
  computed: {
    ...mapState(['config'])
  }
}
</script>

<style>

</style>