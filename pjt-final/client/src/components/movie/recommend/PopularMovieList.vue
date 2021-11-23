<template>
  <div>
    <div class="d-flex">
      <h3 class="turn">POPULAR MOVIE</h3>
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
          this.popularMovie = res.data.filter(movie => {  // 포스터 없는 영화 거르기 
            return movie.poster_path
          })
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
.turn {
  writing-mode: vertical-rl;
    border-left-style: solid;

}

</style>