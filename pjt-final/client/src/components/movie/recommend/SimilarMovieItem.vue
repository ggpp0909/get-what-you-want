<template>
  <div>
    <img :src="posterPath" :alt="`${similarItem.title} 포스터`" height="100">
    <p>{{ similarItem.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'SimilarMovieItem',
  props: {
    similarItem: Object
  },
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.similarItem.poster_path}`
    }
  },
}
</script>

<style>

</style>