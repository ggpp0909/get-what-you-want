<template>
  <div>
    <div @click="goToMovieDetail">
      <img :src="posterPath" :alt="`${similarItem.title} 포스터`" height="100">
      <p>{{ similarItem.title }}</p>
    </div>
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
  methods: {
    goToMovieDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.similarItem.id } })
    }
  }
}
</script>

<style>

</style>