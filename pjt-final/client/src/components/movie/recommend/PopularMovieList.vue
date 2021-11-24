<template>
  <div class="swiper mySwiper">
    <div class="swiper-wrapper">
      <div
        v-for="popularItem in popularMovie"
        :key="popularItem.id"
        :popular-item="popularItem"
        class="swiper-slide"
      >
      <template>
        <div @click="goToMovieDetail(popularItem.id)" class="d-flex flex-column align-items-center">
          <img :src="`https://image.tmdb.org/t/p/w500${popularItem.backdrop_path}`" :alt="`${popularItem.title} 포스터`" width="100%">
          <div>{{ popularItem.title }}</div>
        </div>
      </template>
      </div>
    </div>
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
    
  </div>
  
</template>

<script>
// import PopularMovieItem from '@/components/movie/recommend/PopularMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'PopularMovieList',
  components: {
    // PopularMovieItem
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
      this.getPopularMovie()
      // this.swiper.update();
    },
    
  
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
/* .swiper:not(:hover){
  animation:text-scroll 35s linear infinite;
}
@keyframes text-scroll{
  from{
    transform:translateX(20%);
    -moz-transform:translateX(20%);
    -webkit-transform:translateX(20%);
    -o-transform:translateX(20%);
    -ms-transform:translateX(20%);
  }
  to{
    transform:translateX(-100%);
    -moz-transform:translateX(-100%);
    -webkit-transform:translateX(-100%);
    -o-transform:translateX(-100%);
    -ms-transform:translateX(-100%);
  } */
/* } */

</style>