<template>
  <div class="">

    <!-- <div class="movieLine mx-3">
    <h1>POPULAR MOVIE</h1>
      <popular-movie-list></popular-movie-list>
    </div> -->
<!-- <MARQUEE class="movieTag"><h5>POPULAR MOVIE </h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5><h5> POPULAR MOVIE</h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5></MARQUEE> -->
<div class="movieTag d-flex"><h5>POPULAR MOVIE </h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5><h5> POPULAR MOVIE</h5><h5 class="test2 mx-2"> POPULAR MOVIE</h5></div>
  <v-slide-group class="movieLine v-slide-item--active" show-arrows change center-active mandatory>
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
    
  </div>
</template>

<script>
import PopularMovieList from '@/components/movie/recommend/PopularMovieList'
import TopRatedMovieList from '@/components/movie/recommend/TopRatedMovieList'
import RecommendMovieList from '@/components/movie/recommend/RecommendMovieList'
import SimilarMovieList from '@/components/movie/recommend/SimilarMovieList'
import { mapState } from 'vuex'

import _ from 'lodash'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const COORDS = "coords"

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
    // 날씨 
    askForCoords() {
      navigator.geolocation.getCurrentPosition(this.handleGeoSuccess, this.handleGeoError);
    },
    handleGeoError() {
      console.log("Cant aceess geo location");
    },
    handleGeoSuccess(position) {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      const coordsObj = {
        latitude,
        longitude,
      };
      this.saveCoords(coordsObj);
      this.getWeather(latitude, longitude);
    },
    loadCoords() {
      const loadedCoords = localStorage.getItem(COORDS);
      if (loadedCoords === null) {
        this.askForCoords();
      } else {
        const parsedCoords = JSON.parse(loadedCoords);
        this.getWeather(parsedCoords.latitude, parsedCoords.longitude);
      }
    },
    saveCoords(coordsObj) {
      localStorage.setItem(COORDS, JSON.stringify(coordsObj));
    },
    getWeather(lat, lng) {
      const API_KEY = "c902eb9aee51998b30d90694ef0a29f7";
        fetch(
          `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`
        )
          .then(function (response) {
            return response.json();
          })
          .then(function (json) {
            const weather = json.weather[0].main
            const sendWeather = {
              weather: weather
            }
            axios({
              method: 'post',
              url: `${SERVER_URL}/movie/weather_recommend/`,
              data: sendWeather,
            })
              .then(res => {
                console.log(res)
              })
              .catch(err => {
                console.log(err)
              })
            })
    },
    
  },
  computed: {
    ...mapState(['userName', 'config'])
  },
  created() {
    this.getProfile()
    this.loadCoords()
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