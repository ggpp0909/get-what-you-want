<template>
  <div class="swiper mySwiper">
    <div class="swiper-wrapper">
      <div
        v-for="timeItem in timeMovies"
        :key="timeItem.id"
        :time-item="timeItem"
        class="swiper-slide"
      >
      <template>
        <div @click="goToMovieDetail(timeItem.id)" class="d-flex flex-column align-items-center">
          <img :src="`https://image.tmdb.org/t/p/w500${timeItem.backdrop_path}`" :alt="`${timeItem.title} 포스터`" width="90%">
          <div>{{ timeItem.title }}</div>
        </div>
      </template>
      </div>
    </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div> 
  </div>
</template>

<script>
// import TimeMovieItem from '@/components/movie/recommend/TimeMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TimeMovieList',
  components: {
    // TimeMovieItem
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
          this.timeMovies = res.data[1].filter(movie => {  // 포스터 없는 영화 거르기 
            return movie.backdrop_path
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
  goToMovieDetail(id) {
    this.$router.push({ name: 'MovieDetail', params: { movieId: id } })
  }
  },
  created() {
      this.getTimeMovies()
  }
}
</script>

<style scoped>
.turn {
  writing-mode: vertical-rl;
    border-left-style: solid;
}
.swiper-slide {
  border-left-style: solid;
}
</style>