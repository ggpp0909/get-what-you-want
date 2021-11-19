<template>
  <div>
    <div>
      <h1>recommend movie</h1>
      <div class="d-flex">
        <recommend-movie-item
          v-for="recommendItem in recommendMovies"
          :key="recommendItem.id"
          :recommend-item="recommendItem"
        ></recommend-movie-item>
      </div>
    </div>
    <div>
      <h1>회원님이 좋아요를 누른 000 영화를 기반으로 추천드려요 ! </h1>

    </div>
  </div>
</template>

<script>
import RecommendMovieItem from '@/components/movie/recommend/RecommendMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetailRecommend',
  components: {
    RecommendMovieItem
  },
  data() {
    return {
      recommendMovies: [],
      isDetail: false,
    }
  },
  methods: {
    getRecommendMovie() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/recommend/`, 
      })
        .then(res => {
          this.recommendMovies = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    if (this.$route.params.movieId) {
      this.getRecommendMovie()
    } else {
      pass
    }
  }
}
</script>

<style>
.hide {
  display: none;
}
</style>