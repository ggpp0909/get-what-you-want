<template>
  <div>
    my-review-item
    <div>
      <hr>
      <h5 @click="goToMovie">{{ review.movie_title }}</h5>
      <p> {{ review.content }} </p>
      <p> {{ review.rank }} </p>
      <p> {{ review.created_at }} </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyReviewItem',
  props: {
    review: Object,
  },
  methods: {
    goToMovie() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.review.movie_id } })
    }
  }
}
</script>

<style>

</style>