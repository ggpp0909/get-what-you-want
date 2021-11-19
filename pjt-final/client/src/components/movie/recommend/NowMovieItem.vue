<template>
  <div>
    <img :src="posterPath" :alt="`${nowItem.title} 포스터`" height="100">
    <p>{{ nowItem.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'NowMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.nowItem.poster_path}`
    }
  },
  props: {
    nowItem: Object
  }
}
</script>

<style>

</style>