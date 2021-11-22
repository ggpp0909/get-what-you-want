<template>
  <div>
    <div class="d-flex">
      <review-movie-item
        v-for="reviewItem in reviewMovies"
        :key="reviewItem.movie_id"
        :review-item="reviewItem"
      ></review-movie-item>
    </div>
  </div>
</template>

<script>
import ReviewMovieItem from '@/components/movie/recommend/ReviewMovieItem'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewMovieList',
  components: {
    ReviewMovieItem
  },
  data() {
    return {
      reviewMovies: [],
    }
  },
  methods: {
    getReviewMovies() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/YNs_recommend/`,
        headers: this.config 
      })
        .then(res => {
          console.log(res)
          this.reviewMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getReviewMovies()
  },
  computed: {
    ...mapState(['userName', 'config'])
  },
}
</script>

<style>

</style>