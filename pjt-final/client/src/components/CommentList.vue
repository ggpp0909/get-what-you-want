<template>
  <div>
    <comment-item 
      v-for="(comment, idx) in getComments" 
      :key="idx"
      :comment="comment"
    >
    </comment-item>
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem'

export default {
  name: 'CommentList',
  components: {
    CommentItem
  },
  computed: {
    getComments() {
      return 
    }
  }
}
</script>

<style>

</style>