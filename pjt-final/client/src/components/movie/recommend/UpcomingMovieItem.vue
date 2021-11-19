<template>
  <div>
    <div @click="goToMovieDetail">
      <img :src="posterPath" :alt="`${ upcomingItem.title } 포스터`" height="100">
      <p>{{ upcomingItem.title }}</p>
    </div>

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
  },
  methods: {
    goToMovieDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.upcomingItem.id } })
    }
  }
}
</script>

<style>

</style>