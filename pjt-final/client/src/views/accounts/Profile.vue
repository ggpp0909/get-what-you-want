<template>
  <div>
    <h1>user</h1>
    <!-- <button @click="">〠</button>
    <button @click="">✎</button>
    <button @click="">♥︎</button> -->

    <!-- 팔로우 팔로워 -->
    <div>
      <following></following>
      <follower></follower>
    </div>

    <!-- 유저가 작성한 글 -->
    <div>
      <my-review></my-review>
      <my-post></my-post>
      <my-comment></my-comment>
    </div>

    <!-- 유저가 좋아요한 것들 -->
    <div>
      <like-movie></like-movie>
      <like-post></like-post>
    </div>
  </div>
</template>

<script>
// import { Following } from '@/components/accounts/'
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
  methods: {

  }
}
</script>

<style>

</style>