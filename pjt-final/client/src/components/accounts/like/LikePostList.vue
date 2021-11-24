<template>
  <v-container>
    <h5 v-if="likeCount()" class="text-center">좋아요한 게시글이 없습니다.</h5>
    <like-post-item
      v-for="(post, idx) in likePosts"
      :key=post.id
      :post="post"
      :idx="idx+1"
    >
    </like-post-item>
  </v-container>
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
    likePostCount: Number,
  },
  methods: {
    likeCount() {
      return this.likePostCount < 1 ? true : false
    }
  }
}
</script>

<style>

</style>