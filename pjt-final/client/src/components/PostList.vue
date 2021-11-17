<template>
  <div>
    <h1>PostList</h1>
    <div
      v-for="(post, idx) in getPostItem"
      :key="idx"
    >
      <h1 @click="postDetail(post.id)">{{ post.title }}
      </h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostList',
  computed: {
    getPostItem() {
      return this.$store.state.posts
    }
  },
  methods: {
    postDetail(id) {
      this.$router.push({ name: 'PostDetail', params: { postNum: id } })
    },
  }
}
</script>

<style>

</style>