<template>
 <div @click="goToMovie()" class="m-3 d-flex justify-space-between align-items-center">
    <p class="px-1">{{ idx }}.</p>
    <div class="d-flex flex-column justify-center">
      <b>{{ review.movie_title }}</b>
      <p> {{ review.content }} </p>
    </div>
    <div class="d-flex flex-column justify-center date">
      <p>{{ review.rank }}</p>
      <p>{{ changeDate(review.created_at) }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'MyReviewItem',
  props: {
    review: Object,
    idx: Number,
  },
  methods: {
    goToMovie() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.review.movie_id } })
    },
    // 날짜 슬라이싱 
    changeDate(date) {
      return _.join(_.slice(date, 0, 10), '')
    },
  }
}
</script>

<style>

</style>