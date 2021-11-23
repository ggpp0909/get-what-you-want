<template>
  <div>
    my review
    <my-review-item
      v-for="review in this.reviewSet"
      :key="review.id"
      :review="review"
    ></my-review-item>
  </div>
</template>

<script>
import MyReviewItem from '@/components/accounts/my/MyReviewItem'

export default {
  name: 'MyReviewList',
  components: {
    MyReviewItem
  },
  props: {
    reviewSet: Array
  }
}
</script>

<style>

</style>