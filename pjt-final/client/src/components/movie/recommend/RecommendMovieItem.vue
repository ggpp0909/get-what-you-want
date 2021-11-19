<template>
  <div>
    <div @click="goToMovieDetail">
      <img :src="posterPath" :alt="`${recommendItem.title} 포스터`" height="100">
      <p>{{ recommendItem.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.recommendItem.poster_path}`
    }
  },
  props: {
    recommendItem: Object
  },
  methods: {
    goToMovieDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.recommendItem.id } })
    }
  }
}
</script>

<style>

</style>