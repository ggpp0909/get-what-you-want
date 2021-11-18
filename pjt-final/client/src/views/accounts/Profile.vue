<template>
  <div>
    <h1>user</h1>
    <following></following>
    <follower></follower>
    <my-review></my-review>
    <my-post></my-post>
    <my-comment></my-comment>
    <like-movie></like-movie>
    <like-post></like-post>
  </div>
</template>

<script>
import Following from '@/components/accounts/Following'
import Follower from '@/components/accounts/Following'
import MyReview from '@/components/accounts/MyReview'
import MyPost from '@/components/accounts/MyPost'
import MyComment from '@/components/accounts/MyComment'
import LikeMove from '@/components/accounts/LikeMove'
import LikePost from '@/components/accounts/LikePost'

export default {
  name: 'User',
  components: {
    Following,
    Follower,
    MyReview,
    MyPost,
    MyComment,
    LikeMove,
    LikePost
  }
}
</script>

<style>

</style>