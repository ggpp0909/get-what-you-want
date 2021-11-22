<template>
  <div>
    <div>
      <popular-movie-item
        v-for="popularItem in popularMovie"
        :key="popularItem.id"
        :popular-item="popularItem"
        class=""
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
          console.log(res)
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