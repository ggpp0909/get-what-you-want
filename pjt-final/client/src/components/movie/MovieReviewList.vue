<template>
  <div>
    <movie-review-create :reload-review="getMovieReview"></movie-review-create>
    <movie-review-item 
      v-for="review in reviewList"
      :key="review.id"
      :old-review="review"
      :reload-review="getMovieReview"
    ></movie-review-item>
  </div>
</template>

<script>
import MovieReviewCreate from '@/components/movie/MovieReviewCreate'
import MovieReviewItem from '@/components/movie/MovieReviewItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieReviewList',
  components: {
    MovieReviewItem,
    MovieReviewCreate
  },
  data() {
    return {
      reviewList: []
    }
  },
  methods: {
    // 전체 리뷰 받아오기 
    getMovieReview() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/review_list/`, 
      })
        .then(res => {
          this.reviewList = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }, 
  },
  created() {
    this.getMovieReview()
  }

}
</script>

<style>

</style>