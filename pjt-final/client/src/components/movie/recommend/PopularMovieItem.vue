<template>
  <div>
    <img :src="posterPath" :alt="`${popularItem.title} 포스터`" height="100">
    <p>{{ popularItem.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'PopularMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.popularItem.poster_path}`
    }
  },
  props: {
    popularItem: Object
  }
}
</script>

<style>

</style>