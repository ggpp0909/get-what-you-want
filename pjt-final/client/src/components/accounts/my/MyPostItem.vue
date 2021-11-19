<template>
  <div>
    <div @click="goToPost">
      <h3>{{ post.title }}</h3>
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
      console.log(this.post)
      this.$router.push({ name: 'PostDetail', params: { postNum: this.post.id } })
    }
  }
}
</script>

<style>

</style>