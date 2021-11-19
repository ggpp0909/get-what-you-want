<template>
  <div>
    mycomment
    <my-comment-item
      v-for="comment in this.commentSet"
      :key="comment.id"
      :comment="comment"
    ></my-comment-item>
  </div>
</template>

<script>
import MyCommentItem from '@/components/accounts/my/MyCommentItem'

export default {
  name: 'MyCommentList',
  components: {
    MyCommentItem
  },
  props: {
    commentSet: Array
  }
}
</script>

<style>

</style>