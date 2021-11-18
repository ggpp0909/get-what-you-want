<template>
  <div>
    my-post-item
    <p @click="goToPost"></p>
  </div>
</template>

<script>
export default {
  name: 'MyPostItem',
  methods: {
    goToPost() {
      // this.$route.push({ name: 'PostDetail', params: { postId: postId } })
    }
  }
}
</script>

<style>

</style>