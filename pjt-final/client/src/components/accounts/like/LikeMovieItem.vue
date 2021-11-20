<template>
  <div>
    <div @click="goToMovie">
      <img :src="posterPath" :alt="`${movie.like_movie_title} 포스터`" height="100">
      <h3>{{ movie.like_movie_title }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikeMovieItem',
  props: {
    movie: Object,
  },
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.movie.like_poster_path}`
    }
  },
  methods: {
    goToMovie() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.movie.movie_id } })
    }
  }
}
</script>

<style>

</style>