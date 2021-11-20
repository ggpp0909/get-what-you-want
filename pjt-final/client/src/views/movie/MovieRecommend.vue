<template>
  <div>
    Recommend
    <popular-movie-list></popular-movie-list>
    <top-rated-movie-list></top-rated-movie-list>
    <recommend-movie-list :pick-recommend-movie="pickForRecommendMovie"></recommend-movie-list>
    <similar-movie-list :pick-similar-movie="pickForSimilarMovie"></similar-movie-list>
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
          const pickTwo = _.sampleSize(res.data.like_movie, 2)
          this.pickForRecommendMovie = pickTwo[0]
          this.pickForSimilarMovie = pickTwo[1]
        })
        .catch(err => {
          console.log(err)
        })
    }
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