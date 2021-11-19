<template>
  <div>
    like post
    <like-post-item
      v-for="post in likePosts"
      :key=post.id
      :post="post"
    >
    </like-post-item>
  </div>
</template>

<script>
import LikePostItem from '@/components/accounts/like/LikePostItem'

export default {
  name: 'LikePostList',
  components: {
    LikePostItem
  },
  props: {
    likePosts: Array,
  }
}
</script>

<style>

</style>