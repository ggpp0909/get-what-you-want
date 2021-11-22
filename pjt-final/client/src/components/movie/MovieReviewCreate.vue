<template>
  <div>
    <input type="number" v-model="rank" value="별점">
    <v-checkbox value="True" v-model="isSpoiler" label="스포일러를 포함한 내용인가요?"></v-checkbox>
    <v-text-field v-model.trim="review" color="error" @keyup.enter="createReview"></v-text-field>
    <button @click="createReview">+</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import swal from 'sweetalert'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieReviewCreate',
  data() {
    return {
      review: '',
      rank: 0,
      isSpoiler: false,
    }
  },
  props: {
    reloadReview: Function,
    movieId: Number
  },
  methods: {
    createReview() {
      if (this.review === '') {
          swal ("내용을 입력하세요.", {
          dangerMode: true,
        })
      }
      const reviewItem = {
        content: this.review,
        rank: this.rank,
        is_spoiler: this.isSpoiler ? true : false,
      }
      console.log(this.is_spoiler)
      if (this.config) {
        this.$axios({
          method: 'post',
          url: `${SERVER_URL}/movie/${this.$route.params.movieId}/review_create/`,
          data: reviewItem,
          headers: this.config
        })
          .then(() => {
            this.reloadReview()
            this.review = null
            this.rank = 0
            this.isSpoiler = false
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