<template>
  <div>
    <div @click="goToMovieDetail" class="movieitem">
      <img :src="posterPath" :alt="`${wheaterItem.title} 포스터`" height="90%">
      <p>{{ weatherItem.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WeatherMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.weatherItem.poster_path}`
    }
  },
  props: {
    weatherItem: Object
  },
  methods: {
    goToMovieDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.weatherItem.id } })
    }
  }
}
</script>

<style>

</style>