<template>
  <div class="">

    <!-- <div class="movieLine mx-3">
    <h1>POPULAR MOVIE</h1>
      <popular-movie-list></popular-movie-list>
    </div> -->
<!-- <MARQUEE class="movieTag"><h5>POPULAR MOVIE </h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5><h5> POPULAR MOVIE</h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5></MARQUEE> -->
<div class="movieTag d-flex"><h5>POPULAR MOVIE </h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5><h5> POPULAR MOVIE</h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5></div>

  <v-slide-group class="movieLine v-slide-item--active" show-arrows active-class="success">
    <popular-movie-list></popular-movie-list>
  </v-slide-group>
  

    <div class="movieTag">
      <h1>top Rated movie</h1>
      <v-slide-group>
      <top-rated-movie-list></top-rated-movie-list>
      </v-slide-group>
    </div>
  
    <div v-if="showRS">
      <recommend-movie-list :pick-recommend-movie="pickForRecommendMovie"></recommend-movie-list>
      <similar-movie-list :pick-similar-movie="pickForSimilarMovie"></similar-movie-list>
    </div>

    <div class="movieTag">
      <h1>weather movie</h1>
      <v-slide-group>
      <weather-movie-list></weather-movie-list>
      </v-slide-group>
    </div>
    
  </div>
</template>

<script>
import PopularMovieList from '@/components/movie/recommend/PopularMovieList'
import TopRatedMovieList from '@/components/movie/recommend/TopRatedMovieList'
import RecommendMovieList from '@/components/movie/recommend/RecommendMovieList'
import SimilarMovieList from '@/components/movie/recommend/SimilarMovieList'
import WeatherMovieList from '@/components/movie/recommend/WeatherMovieList'
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
    WeatherMovieList,
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
    ...mapState(['userName', 'config'])
  },
  created() {
    this.getProfile()
  }
}
</script>

<style scoped>
.movieLine {
  border-style: solid;
  height: 200px;
}
.movieTag {
  border-style: solid;
  border-bottom-style: none;
  box-sizing: border-box;
  margin-bottom: -8px;
}
.test2 {
  color: orange;
}

</style>