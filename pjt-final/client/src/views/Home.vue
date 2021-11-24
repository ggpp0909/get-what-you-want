<template>
  <div>
    home
    <upcoming-movie-list></upcoming-movie-list>
    <now-movie-list></now-movie-list>

    <!-- Swiper -->
    <div class="swiper mySwiper">
      <div class="swiper-wrapper">
        <div class="swiper-slide">Slide 1</div>
        <div class="swiper-slide">Slide 2</div>
        <div class="swiper-slide">Slide 3</div>
        <div class="swiper-slide">Slide 4</div>
        <div class="swiper-slide">Slide 5</div>
        <div class="swiper-slide">Slide 6</div>
        <div class="swiper-slide">Slide 7</div>
        <div class="swiper-slide">Slide 8</div>
        <div class="swiper-slide">Slide 9</div>
      </div>
          <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
      <div class="swiper-pagination"></div>
    </div>
  <!-- If we need navigation buttons -->


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