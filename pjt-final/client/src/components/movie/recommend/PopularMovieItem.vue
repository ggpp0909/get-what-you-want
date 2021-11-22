<template>
  <div @click="goToMovieDetail" class="movieitem d-flex flex-column align-items-center">
    <img :src="posterPath" :alt="`${popularItem.title} 포스터`" height=43%>
    <p>{{ popularItem.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'PopularMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.popularItem.backdrop_path}`
    }
  },
  props: {
    popularItem: Object
  },
  methods: {
    goToMovieDetail() {
    this.$router.push({ name: 'MovieDetail', params: { movieId: this.popularItem.id } })
    }
  }
}
</script>

<style>
.movieitem {
  height: 400px;
  width: 100%;
  border-right-style: solid;
}
</style>