<template>
  <div class="swiper mySwiper">
    <div class="swiper-wrapper">
      <div
        v-for="weatherItem in weatherMovies"
        :key="weatherItem.id"
        :weather-item="weatherItem"
        class="swiper-slide"
      >
      <template>
        <div @click="goToMovieDetail(weatherItem.id)" class="d-flex flex-column align-items-center">
          <img :src="`https://image.tmdb.org/t/p/w500${weatherItem.backdrop_path}`" :alt="`${weatherItem.title} 포스터`" width="100%">
          <p>{{ weatherItem.title }}</p>
        </div>
      </template>
      </div>
    </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div> 
  </div>
</template>

<script>
// import WeatherMovieItem from '@/components/movie/recommend/WeatherMovieItem'
import axios from 'axios'

const WEATHER_API = "c902eb9aee51998b30d90694ef0a29f7"
// const WEATHER_API = process.env.VUE_APP_WEATHER_API
const SERVER_URL = process.env.VUE_APP_SERVER_URL
const COORDS = "coords"

export default {
  name: 'WeatherMovieList',
  components: {
    // WeatherMovieItem
  },
  data() {
    return {
      weather: null,
      weatherMovies: [],
    }
  },
  methods: {
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
      this.getWeatherMovies(latitude, longitude);
    },
    loadCoords() {
      const loadedCoords = localStorage.getItem(COORDS);
      if (loadedCoords === null) {
        this.askForCoords();
      } else {
        const parsedCoords = JSON.parse(loadedCoords);
        this.getWeatherMovies(parsedCoords.latitude, parsedCoords.longitude);
      }
    },
    saveCoords(coordsObj) {
      localStorage.setItem(COORDS, JSON.stringify(coordsObj));
    },
    async getWeatherMovies(lat, lng) {
      let temp1 = await fetch(
          `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${WEATHER_API}&units=metric`
        )
        .then(function (response) {
          return response.json();
        })
        .then(function (json) {
          const weather = json.weather[0].main
          const sendWeather = {
            weather: weather
          }
          let temp2 = axios({ 
            method: 'post',
            url: `${SERVER_URL}/movie/weather_recommend/`,
            data: sendWeather,
          })
            .then(res => {
              return res.data
            })
          return temp2
          })
        this.weatherMovies = temp1[1].filter(movie => {  // 포스터 없는 영화 거르기 
            return movie.backdrop_path
          })
        this.weather = temp1[0].weather
        this.$emit('weather-name', this.weather)
    },
  goToMovieDetail(id) {
    this.$router.push({ name: 'MovieDetail', params: { movieId: id } })
  },
  },
  created() {
    this.loadCoords()
  },
}
</script>

<style>
.turn {
  writing-mode: vertical-rl;
    border-left-style: solid;
}
.swiper-slide {
  border-left-style: solid;
}
</style>