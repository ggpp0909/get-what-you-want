<template>
  <div>
    like post
    <like-post-item></like-post-item>
  </div>
</template>

<script>
import LikePostItem from '@/components/accounts/like/LikePostItem'

export default {
  name: 'LikePostList',
  components: {
    LikePostItem
  }
}
</script>

<style>

</style>