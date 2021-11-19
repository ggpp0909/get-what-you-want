<template>
  <div>
    <h1>recommend movie</h1>
    <movie-detail-recommend-item
      v-for="recommendItem in recommendMovies"
      :key="recommendItem.id"
      :recommend-item="recommendItem"
    ></movie-detail-recommend-item>
  </div>
</template>

<script>
import MovieDetailRecommendItem from '@/components/movie/MovieDetailRecommendItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetailRecommend',
  components: {
    MovieDetailRecommendItem
  },
  data() {
    return {
      recommendMovies: [],
    }
  },
  methods: {
    getRecommendMovie() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/recommend/`, 
      })
        .then(res => {
          this.recommendMovies = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getRecommendMovie()
    }
}
</script>

<style>

</style>