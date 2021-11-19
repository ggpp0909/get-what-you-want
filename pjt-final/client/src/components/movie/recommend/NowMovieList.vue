<template>
  <div>
    <h1>now movie</h1>
    <div class="d-flex">
      <now-movie-item
        v-for="nowItem in nowMovies"
        :key="nowItem.id"
        :now-item="nowItem"
      ></now-movie-item>
    </div>
  </div>
</template>

<script>
import NowMovieItem from '@/components/movie/recommend/NowMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'NowMovieList',
  components: {
    NowMovieItem
  },
  data() {
    return {
      nowMovies: [],
    }
  },
  methods: {
    getNowMovies() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/now_playing/`, 
      })
        .then(res => {
          this.nowMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getNowMovies()
    }
}
</script>

<style>

</style>