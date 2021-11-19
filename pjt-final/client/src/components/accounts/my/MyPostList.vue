<template>
  <div>
    <my-post-item
      v-for="post in this.postSet"
      :key="post.id"
      :post="post"
    ></my-post-item>
  </div>
</template>

<script>
import MyPostItem from '@/components/accounts/my/MyPostItem'

export default {
  name: 'MyPostList',
  components: {
    MyPostItem
  },
  props: {
    postSet: Array
  },
}
</script>

<style>

</style>