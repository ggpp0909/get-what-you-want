<template>
  <div>
    home
    <upcoming-movie-list></upcoming-movie-list>
    <now-movie-list></now-movie-list>

  


  <!-- If we need scrollbar -->
  <!-- <div class="swiper-scrollbar"></div> -->


  </div>

</template>

<script>
import NowMovieList from '@/components/movie/recommend/NowMovieList'
import UpcomingMovieList from '@/components/movie/recommend/UpcomingMovieList'

export default {
    name: 'Home',
    components: {
      NowMovieList,
      UpcomingMovieList,
    }
  }
</script>

<style scoped>

</style>