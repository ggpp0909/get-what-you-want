<template>
  <div>
    {{ comment.content }}
    <p>작성자: {{ comment.user.nickname }}</p>
    <p>작성일: {{ comment.created_at }}</p>
  </div>
</template>

<script>
export default {
  name: 'CommentItem',
  props: {
    comment: {
      type: Object
    }
  }
}
</script>

<style>

</style>