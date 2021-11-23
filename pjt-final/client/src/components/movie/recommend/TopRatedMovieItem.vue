<template>
  <div>
    <div @click="goToMovieDetail" class="movieitem">
      <img :src="posterPath" :alt="`${topRatedItem.title} 포스터`" height="90%">
      <p>{{ topRatedItem.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopRatedMovieItem',
  data() {
    return {
      posterPath: `https://image.tmdb.org/t/p/w500${this.topRatedItem.backdrop_path}`
    }
  },
  props: {
    topRatedItem: Object
  },
  methods: {
    goToMovieDetail() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.topRatedItem.id } })
    }
  }
}
</script>

<style>

</style>