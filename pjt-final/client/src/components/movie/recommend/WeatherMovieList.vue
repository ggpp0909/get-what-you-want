<template>
  <div>
    <h1>{{ weather }} 추천 </h1>
    <div class="d-flex">
      <weather-movie-item
        v-for="weatherItem in weatherMovies"
        :key="weatherItem.id"
        :weather-item="weatherItem"
      ></weather-movie-item>
    </div>
  </div>
</template>

<script>
import WeatherMovieItem from '@/components/movie/recommend/WeatherMovieItem'
import axios from 'axios'

const WEATHER_API = "c902eb9aee51998b30d90694ef0a29f7"
// const WEATHER_API = process.env.VUE_APP_WEATHER_API
const SERVER_URL = process.env.VUE_APP_SERVER_URL
const COORDS = "coords"

export default {
  name: 'WeatherMovieList',
  components: {
    WeatherMovieItem
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
        this.weatherMovies = temp1[1]
        this.weather = temp1[0].weather
    },
  },
  created() {
    this.loadCoords()
  },
}
</script>

<style>

</style>