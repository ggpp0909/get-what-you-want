<template>
  <div>
    <h1>popular movie</h1>
    <div class="d-flex">
      <popular-movie-item
        v-for="popularItem in popularMovie"
        :key="popularItem.id"
        :popular-item="popularItem"
      ></popular-movie-item>
    </div>
  </div>
</template>

<script>
import PopularMovieItem from '@/components/movie/recommend/PopularMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'PopularMovieList',
  components: {
    PopularMovieItem
  },
  data() {
    return {
      popularMovie: [],
    }
  },
  methods: {
    getPopularMovie() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/popular/`, 
      })
        .then(res => {
          this.popularMovie = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getPopularMovie()
    }
}
</script>

<style>

</style>