<template>
  <div>
    <div @click="goToMovieDetail">
      <img :src="posterPath" :alt="`${nowItem.title} 포스터`" height="100">
      <p>{{ nowItem.title }}</p>
    </div>
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
  },
  methods: {
    goToMovieDetail() {
    this.$router.push({ name: 'MovieDetail', params: { movieId: this.nowItem.id } })
    }
  }
}
</script>

<style>

</style>