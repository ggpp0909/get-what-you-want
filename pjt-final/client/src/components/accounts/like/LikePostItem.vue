<template>
  <div>
    <div @click="goToPost">
      <h3>{{ post.title }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikePostItem',
  props: {
    post: Object
  },
  methods: {
    goToPost() {
      this.$router.push({ name: 'PostDetail', params: { postNum: this.post.id } })
    }
  }

}
</script>

<style>

</style>