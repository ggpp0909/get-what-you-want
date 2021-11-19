<template>
  <div>
    <img :src="posterPath" :alt="`${topRatedItem.title} 포스터`" height="100">
    <p>{{ topRatedItem.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'TopRatedMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.topRatedItem.poster_path}`
    }
  },
  props: {
    topRatedItem: Object
  }
}
</script>

<style>

</style>