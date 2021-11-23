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
  },
  created() {
    if (this.$route.name === 'MovieRecommend') { // 영화 추천 페이지에서 접근 했을때 
      this.posterPath = `https://image.tmdb.org/t/p/w500${this.recommendItem.backdrop_path}`
    }
  }
}
</script>

<style>

</style>