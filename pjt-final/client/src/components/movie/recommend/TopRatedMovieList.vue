<template>
  <div>
    <h1>top Rated movie</h1>
    <div class="d-flex">
      <top-rated-movie-item
        v-for="topRatedItem in topRatedMovies"
        :key="topRatedItem.id"
        :top-rated-item="topRatedItem"
      ></top-rated-movie-item>
    </div>
  </div>
</template>

<script>
import TopRatedMovieItem from '@/components/movie/recommend/TopRatedMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TopRatedMovieList',
  components: {
    TopRatedMovieItem
  },
  data() {
    return {
      topRatedMovies: [],
    }
  },
  methods: {
    getTopRatedMovies() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/top_rated/`, 
      })
        .then(res => {
          this.topRatedMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getTopRatedMovies()
    }
}
</script>

<style>

</style>