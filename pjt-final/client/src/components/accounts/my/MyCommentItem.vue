<template>
  <div>
    <div @click="goToPost">
      <h3>{{ comment.content }}</h3>
      <p>{{ comment.created_at }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyCommentItem',
  props: {
    comment: Object,
  },
  methods: {
    goToPost() {
      this.$router.push({ name: 'PostDetail', params: { postNum: this.comment.post_id } })
    }
  }
}
</script>

<style>

</style>