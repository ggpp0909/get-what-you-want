<template>
  <div>
    my-post
    <my-post-item
      v-for="post in this.PostList"
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
    postList: Array
  },
  created() {
    console.log(this.postList)
  }
}
</script>

<style>

</style>