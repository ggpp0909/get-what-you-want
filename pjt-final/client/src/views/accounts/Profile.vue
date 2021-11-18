<template>
  <div>
    <h1>user</h1>
    <button @click="clickFollow">〠</button> |
    <button @click="clickMy">✎</button> |
    <button @click="clickLike">♥︎</button>

    <div>
      <!-- 팔로우 팔로워 -->
      <div :class="{'hide': showFollow }">
        <following></following>
        <follower></follower>
      </div>

      <!-- 유저가 작성한 글 -->
      <div :class="{'hide': showMy }">
        <my-review></my-review>
        <my-post></my-post>
        <my-comment></my-comment>
      </div>

      <!-- 유저가 좋아요한 것들 -->
      <div :class="{'hide': showLike }">
        <like-movie></like-movie>
        <like-post></like-post>
      </div>
    </div>
  </div>
</template>

<script>
import Following from '@/components/accounts/Following'
import Follower from '@/components/accounts/Following'
import MyReview from '@/components/accounts/MyReview'
import MyPost from '@/components/accounts/MyPost'
import MyComment from '@/components/accounts/MyComment'
import LikeMovie from '@/components/accounts/LikeMovie'
import LikePost from '@/components/accounts/LikePost'

export default {
  name: 'User',
  components: {
    Following,
    Follower,
    MyReview,
    MyPost,
    MyComment,
    LikeMovie,
    LikePost
  },
  data() {
    return {
      showFollow: false,
      showMy: true,
      showLike: true,
    }
  },
  methods: {
    clickFollow() {
      this.showFollow = false
      this.showMy = true
      this.showLike = true
    },
    clickMy() {
      this.showFollow = true
      this.showMy = false
      this.showLike = true
    },
    clickLike() {
      this.showFollow = true
      this.showMy = true
      this.showLike = false
    }
  }
}
</script>

<style>
.hide {
  display: none;
}
</style>