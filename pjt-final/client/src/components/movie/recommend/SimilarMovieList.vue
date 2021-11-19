<template>
  <div>
    <!-- 영화 디테일 페이지에서 접근 -->
    <h1 v-if="accessDetail">recommend movie</h1>
    <!-- 영화 추천 페이지에서 접근 -->
    <h1 v-else>회원님이 좋아요를 누른 000 영화와 비슷한 영화들은 어때요?  </h1>
    <div class="d-flex">
      <similar-movie-item
        v-for="similarItem in similarMovies"
        :key="similarItem.id"
        :similar-item="similarItem"
      ></similar-movie-item>
    </div>
  </div>
</template>

<script>
import SimilarMovieItem from '@/components/movie/recommend/SimilarMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'SimilarMovieList',
  components: {
    SimilarMovieItem
  },
  data() {
    return {
      similarMovies: [],
      accessDetail: true,
    }
  },
  methods: {
    getSimilarMovie(movieId) {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${movieId}/similar/`, 
      })
        .then(res => {
          this.similarMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    pickLikeMovie() {

    }
  },
  created() {
    if (this.$route.params.movieId) { // 영화 디테일 페이지에서 접근 했을때 
      this.getSimilarMovie(this.$route.params.movieId)
    } else {  // 영화 추천 페이지에서 접근 했을때 
      this.accessDetail = false
    }
  }
}
</script>

<style>

</style>