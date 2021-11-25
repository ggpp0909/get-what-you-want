<template>
  <v-container id="scroll-target" style="max-height: 800px"
    class="overflow-y-auto">
    <movie-review-create :reload-review="getMovieReview"></movie-review-create>
    <v-virtual-scroll v-if="reviewList" :bench="benched" :items="items"
      height="300" item-height="50"
    >
      <template>
        <v-list-item :key="item">
          <v-list-item-action>
            <movie-review-item 
              v-for="review in reviewList"
              :key="review.id"
              :old-review="review"
              :reload-review="getMovieReview"
            ></movie-review-item>
        </v-list-item-action>
        </v-list-item>
      </template>
    </v-virtual-scroll>
    <v-row v-else>
      작성된 리뷰가 없습니다. 첫번째로 리뷰를 남겨보세요 ! 
    </v-row>
  </v-container>
</template>

<script>
import MovieReviewCreate from '@/components/movie/MovieReviewCreate'
import MovieReviewItem from '@/components/movie/MovieReviewItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieReviewList',
  components: {
    MovieReviewItem,
    MovieReviewCreate
  },
  data() {
    return {
      reviewList: [],
      benched: 0,
      currentPage: 0,
    }
  },
  methods: {
    // 전체 리뷰 받아오기 
    getMovieReview() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/review_list/`, 
        params: {page: this.currentPage}
      })
        .then(res => {
          console.log(res.data)
          this.reviewList = res.data
          // this.reviewList = res.data.length > 1 ? res.data : false
        })
        .catch(err => {
          console.log(err)
        })
    }, 
    onscroll(e) {
      this.offsetTop = e.target.scrollTop

      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/review_list/`, 
        params: {page: this.currentPage}
      })
        .then(res => {
          console.log(res.data)
          this.reviewList = res.data
          // this.reviewList = res.data.length > 1 ? res.data : false
        })
        .catch(err => {
          console.log(err)
        })
      this.currentPage += 1
    }
  },
  created() {
    this.getMovieReview()
  },
  computed: {
    items () {
      return Array.from({ length: this.length }, (k, v) => v + 1)
    },
    length () {
      return 70
    },
  },
}
</script>

<style>

</style>