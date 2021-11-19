<template>
  <div>
    <h1>Similar movie</h1>
    <div class="d-flex">
      <similar-movie-item
        v-for="similarItem in similarMovies"
        :key="similarItem.id"
        :similar-item="similarItem"
      ></similar-movie-item>
    </div>
  </div>
</template>

<script>
import SimilarMovieItem from '@/components/movie/recommend/SimilarMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'SimilarMovieList',
  components: {
    SimilarMovieItem
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