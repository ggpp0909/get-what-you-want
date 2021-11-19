<template>
  <div>
    <img :src="posterPath" :alt="`${ upcomingItem.title } 포스터`" height="100">
    <p>{{ upcomingItem.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'UpcomingMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.upcomingItem.poster_path}`
    }
  },
  props: {
    upcomingItem: Object
  }
}
</script>

<style>

</style>