<template>
  <div>
    <input type="number" v-model="rank" value="별점">
    <input type="checkbox" value="스포일러를 포함한 내용인가요?" v-model="isSpoiler">
    <v-text-field v-model.trim="review" color="error" @keyup.enter="createReview"></v-text-field>
    <button @click="createReview">+</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieReviewCreate',
  data() {
    return {
      review: null,
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
      const reviewItem = {
        content: this.review
      }
      if (this.config) {
        this.$axios({
          method: 'post',
          url: `${SERVER_URL}/movie/${this.movieId}/review_create/`,
          data: reviewItem,
          headers: this.config
        })
          .then(() => {
            this.reloadReview()
            this.review = null
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