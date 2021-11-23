<template>
  <div>
    <div @click="goToMovieDetail" class="movieitem">
      <img :src="posterPath" :alt="`${weatherUseItem.title} 포스터`" height="90%">
      <p>{{ weatherUseItem.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WeatherMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.weatherItem.backdrop_path}`,
      weatherUseItem: null,
    }
  },
  props: {
    weatherItem: Object
  },
  methods: {
    goToMovieDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.weatherItem.id } })
    }
  },
  created() {
    this.weatherUseItem = this.weatherItem
  },
  watch: {
    weatherItem() {
      this.weatherUseItem = this.weatherItem
    }
  }
}
</script>

<style>

</style>