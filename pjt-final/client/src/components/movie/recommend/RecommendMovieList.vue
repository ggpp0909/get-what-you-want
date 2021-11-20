<template>
  <div>
    <!-- 영화 디테일 페이지에서 접근 -->
    <h1 v-if="accessDetail">recommend movie</h1>
    <!-- 영화 추천 페이지에서 접근 -->
    <h1 v-else>회원님이 좋아요를 누른 영화 "{{ pickRecommendMovie.like_movie_title }}" 기반으로 추천드려요 ! </h1>
    <div class="d-flex">
      <recommend-movie-item
        v-for="recommendItem in recommendMovies"
        :key="recommendItem.id"
        :recommend-item="recommendItem"
      ></recommend-movie-item>
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
  props: {
    pickRecommendMovie: Object,
  },
  data() {
    return {
      recommendMovies: [],
      accessDetail: true,
    }
  },
  methods: {
    getRecommendMovie(movieId) {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${movieId}/recommend/`, 
      })
        .then(res => {
          this.recommendMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    if (this.$route.name === 'MovieRecommend') { // 영화 추천 페이지에서 접근 했을때 
      this.getRecommendMovie(this.pickRecommendMovie.movie_id)
      this.accessDetail = false
    } else {  // 영화 디테일 페이지에서 접근 했을때 
      this.getRecommendMovie(this.$route.params.movieId)
    }
  },
  watch: {
    pickRecommendMovie() {
      this.getRecommendMovie(this.pickRecommendMovie.movie_id)
      this.accessDetail = false
    }
  }
}
</script>

<style>

</style>