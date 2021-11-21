<template>
  <div>
    Recommend
    <popular-movie-list></popular-movie-list>
    <top-rated-movie-list></top-rated-movie-list>
    <div v-if="showRS">
      <recommend-movie-list :pick-recommend-movie="pickForRecommendMovie"></recommend-movie-list>
      <similar-movie-list :pick-similar-movie="pickForSimilarMovie"></similar-movie-list>
    </div>
    
  </div>
</template>

<script>
import PopularMovieList from '@/components/movie/recommend/PopularMovieList'
import TopRatedMovieList from '@/components/movie/recommend/TopRatedMovieList'
import RecommendMovieList from '@/components/movie/recommend/RecommendMovieList'
import SimilarMovieList from '@/components/movie/recommend/SimilarMovieList'
import { mapState } from 'vuex'

import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Recommend',
  components: {
    PopularMovieList,
    TopRatedMovieList,
    RecommendMovieList,
    SimilarMovieList,
  },
  data() {
    return {
      pickForRecommendMovie: null,
      pickForSimilarMovie: null,
      showRS: false,
    }
  },
  methods:{
    // 좋아요한 영화 받아오기 
    getProfile() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/${this.userName}/`, 
      })
        .then(res => {
          // 로그인 상태 및 좋아요한 개수에 따라 추천, 비슷한 영화 보여주는거 결정 
          if (this.userName) {
            if (res.data.like_movie.length > 1) {
              const pickTwo = _.sampleSize(res.data.like_movie, 2)
              this.pickForRecommendMovie = pickTwo[0]
              this.pickForSimilarMovie = pickTwo[1]
            } else if (res.data.like_movie.length === 1) {
              this.pickForRecommendMovie = res.data.like_movie[0]
              this.pickForSimilarMovie = res.data.like_movie[0]
            } else {
              this.showRS = false
            }
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed: {
    ...mapState(['userName'])
  },
  created() {
    this.getProfile()
  }
}
</script>

<style>

</style>