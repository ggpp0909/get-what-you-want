<template>
  <div>
    <h1>user</h1>
    <button @click="clickFollow">〠</button> |
    <button @click="clickMy">✎</button> |
    <button @click="clickLike">♥︎</button>

    <div>
      <!-- 팔로우 팔로워 -->
      <div :class="{'hide': showFollow }">
        <button @click="clickFollowing">Following</button> |
        <button @click="clickFollower">Follower</button>

        <following :class="{'hide': showFollowing }"></following>
        <follower :class="{'hide': showFollower }"></follower>
      </div>

      <!-- 유저가 작성한 글 -->
      <div :class="{'hide': showMy }">
        <button @click="clickMyR">My Review</button> |
        <button @click="clickMyP">My Post</button> |
        <button @click="clickMyC">My Comment</button> 

        <my-review :class="{'hide': showMyR }"></my-review>
        <my-post :class="{'hide': showMyP }"></my-post>
        <my-comment :class="{'hide': showMyC }"></my-comment>
      </div>

      <!-- 유저가 좋아요한 것들 -->
      <div :class="{'hide': showLike }">
        <button @click="clickLikeM">Like Movie</button> |
        <button @click="clickLikeP">Like Post</button>

        <like-movie :class="{'hide': showLikeM }"></like-movie>
        <like-post :class="{'hide': showLikeP }"></like-post>
      </div>
    </div>
  </div>
</template>

<script>
import Following from '@/components/accounts/Following'
import Follower from '@/components/accounts/Follower'
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
      showFollowing: false,
      showFollower: true,
      showMyR: false,
      showMyP: true,
      showMyC: true,
      showLikeM: false,
      showLikeP: true,
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
    },
    clickFollowing() {
      this.showFollowing = false
      this.showFollower = true
    },
    clickFollower() {
      this.showFollowing = true
      this.showFollower = false
    },
    clickMyR() {
      this.showMyR = false
      this.showMyP = true
      this.showMyC = true
    },
    clickMyP() {
      this.showMyR = true
      this.showMyP = false
      this.showMyC = true
    },
    clickMyC() {
      this.showMyR = true
      this.showMyP = true
      this.showMyC = false
    },
    clickLikeM() {
      this.showLikeM = false,
      this.showLikeP = true
    },
    clickLikeP() {
      this.showLikeM = true
      this.showLikeP = false
    },
    
  }
}
</script>

<style>
.hide {
  display: none;
}
</style>