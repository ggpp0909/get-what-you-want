<template>
  <div>
    <div class="d-flex">
      <time-movie-item
        v-for="timeItem in timeMovies"
        :key="timeItem.id"
        :time-item="timeItem"
      ></time-movie-item>
    </div>
  </div>
</template>

<script>
import TimeMovieItem from '@/components/movie/recommend/TimeMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TimeMovieList',
  components: {
    TimeMovieItem
  },
  data() {
    return {
      timeMovies: [],
    }
  },
  methods: {
    getTimeMovies() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/time_recommend/`, 
      })
        .then(res => {
          console.log(res)
          this.timeMovies = res.data[1]
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getTimeMovies()
    }
}
</script>

<style>

</style>