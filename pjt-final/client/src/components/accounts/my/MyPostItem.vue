<template>
  <div>
    <div @click="goToPost">
      <p>{{ post.title }}</p>
      <p>{{ post.created_at }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyPostItem',
  props: {
    post: Object,
  },
  methods: {
    goToPost() {
      this.$route.push({ name: 'PostDetail', params: { postId: this.post.id } })
    }
  }
}
</script>

<style>

</style>