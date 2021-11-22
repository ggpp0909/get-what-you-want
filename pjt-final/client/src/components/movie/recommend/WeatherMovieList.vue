<template>
  <div>
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
    getWeatherMovies(lat, lng) {
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
            
            this.myAxios(sendWeather)
          })
          .then(res => {
            this.weatherMovies = res
          })
      
    },
    myAxios(sendWeather) {
      axios({
              method: 'post',
              url: `${SERVER_URL}/movie/weather_recommend/`,
              data: sendWeather,
            })
              .then(res => {
                console.log(res.data[1])
                return res.data[1]
              })
              .catch(err => {
                console.log(err)
              })
    }

  },
  created() {
      this.loadCoords()

    }
}
</script>

<style>

</style>