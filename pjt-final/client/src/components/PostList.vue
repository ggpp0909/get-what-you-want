<template>
  <div>
    <h1>PostList</h1>
    <post-item
      v-for="(post, idx) in getPostItem"
      :key="idx"
      :post="post"
    >
    </post-item>
  </div>
</template>

<script>
import PostItem from '@/components/PostItem'

export default {
  name: 'PostList',
  components: {
    PostItem,
  },
  computed: {
    getPostItem() {
      return this.$store.state.posts
    }
  }
}
</script>

<style>

</style>