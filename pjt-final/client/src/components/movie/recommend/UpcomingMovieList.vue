<template >
  <!-- <h1>upcoming movie</h1> -->
  <div class="swiper mySwiper">
  <div class="swiper-wrapper">
    <div
      v-for="upcomingItem in upcomingMovies"
      :key="upcomingItem.id"
      :upcoming-item="upcomingItem"
     class="swiper-slide"
    >
  <template>
    <img :src="`https://image.tmdb.org/t/p/w500${upcomingItem.poster_path}`" :alt="`${ upcomingItem.title } 포스터`" height="100">
    <p>{{ upcomingItem.title }}</p>
    </template>
  </div>
    
  </div>
    <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
      <div class="swiper-pagination"></div>
  </div>
</template>

<script>
// import UpcomingMovieItem from '@/components/movie/recommend/UpcomingMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'UpcomingMovieList',
  components: {
    // UpcomingMovieItem
  },
  data() {
    return {
      upcomingMovies: [],
    }
  },
  methods: {
    getUpcomingMovies() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/upcoming/`, 
      })
        .then(res => {
          this.upcomingMovies = res.data.filter(movie => {  // 포스터 없는 영화 거르기 
            return movie.poster_path
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
      this.getUpcomingMovies()
    }
}
</script>

<style>
.swiper {
  width: 100%;
  height: 400px;
}
</style>