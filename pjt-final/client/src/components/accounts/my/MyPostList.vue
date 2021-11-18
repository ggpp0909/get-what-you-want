<template>
  <div>
    my-post
    <my-post-item></my-post-item>
  </div>
</template>

<script>
import MyPostItem from '@/components/accounts/my/MyPostItem'

export default {
  name: 'MyPostList',
  components: {
    MyPostItem
  }
}
</script>

<style>

</style>