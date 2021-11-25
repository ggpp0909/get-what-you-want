<template>
  <div class="swiper mySwiper">
    <div class="swiper-wrapper">
      <div
        v-for="reviewItem in reviewMovies"
        :key="reviewItem.movie_id"
        :review-item="reviewItem"
        class="swiper-slide"
      >
      <template> <!-- 여기 이미지 나중에 데이터 다시 받고 백드롭패스로 바꿔야됨 -->
        <div @click="goToMovieDetail(reviewItem.id)" class="d-flex flex-column align-items-center">
          <img :src="`https://image.tmdb.org/t/p/w500${reviewItem.backdrop_path}`" :alt="`${reviewItem.title} 포스터`" width="100%">
          <div>{{ reviewItem.title }}</div>
        </div>
      </template>
      </div>
    </div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
  </div>
</template>

<script>
// import ReviewMovieItem from '@/components/movie/recommend/ReviewMovieItem'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewMovieList',
  components: {
    // ReviewMovieItem
  },
  data() {
    return {
      reviewMovies: [],
    }
  },
  methods: {
    getReviewMovies() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/YNs_recommend/`,
        headers: this.config 
      })
        .then(res => {
          console.log(res)
          this.reviewMovies = res.data.filter(movie => {  // 포스터 없는 영화 거르기 
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
      this.getReviewMovies()
  },
  computed: {
    ...mapState(['userName', 'config'])
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
</style>