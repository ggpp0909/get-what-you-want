<template>
  <div class="swiper mySwiper">
    <div class="swiper-wrapper">
      <div
        v-for="topRatedItem in topRatedMovies"
        :key="topRatedItem.id"
        :top-rated-item="topRatedItem"
        class="swiper-slide"
      >
      <template>
          <div @click="goToMovieDetail(topRatedItem.id)" class="d-flex flex-column align-items-center">
            <img :src="`https://image.tmdb.org/t/p/w500${topRatedItem.backdrop_path}`" :alt="`${topRatedItem.title} 포스터`" width="100%">
            <div>{{ topRatedItem.title }}</div>
          </div>
      </template>
      </div>
    </div>
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </div>
</template>

<script>
// import TopRatedMovieItem from '@/components/movie/recommend/TopRatedMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TopRatedMovieList',
  components: {
    // TopRatedMovieItem
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
          this.topRatedMovies = res.data.filter(movie => {
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
      this.getTopRatedMovies()
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