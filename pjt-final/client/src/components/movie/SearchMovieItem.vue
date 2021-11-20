<template>
  <div class="d-flex" @click="goToMovieDetail">
    <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" :alt="`${ movie.title } 포스터`" height="100">
    <h3>{{ movie.title }}</h3>
  </div>
</template>

<script>
export default {
  name: 'SearchMovieItem',
  props: {
    movie: Object
  },
  methods: {
    goToMovieDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movie.id } })
    }
  }
}
</script>

<style>

</style>