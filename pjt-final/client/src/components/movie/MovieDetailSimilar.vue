<template>
  <div>
    <h1>recommend movie</h1>
    <movie-detail-similar-item
      v-for="similarItem in similarMovies"
      :key="similarItem.id"
      :similar-item="similarItem"
    ></movie-detail-similar-item>
  </div>
</template>

<script>
import MovieDetailSimilarItem from '@/components/movie/MovieDetailSimilarItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetailSimilar',
  components: {
    MovieDetailSimilarItem
  },
  data() {
    return {
      similarMovies: [],
    }
  },
  methods: {
    getSimilarMovie() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/similar/`, 
      })
        .then(res => {
          this.similarMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getSimilarMovie()
    }
}
</script>

<style>

</style>