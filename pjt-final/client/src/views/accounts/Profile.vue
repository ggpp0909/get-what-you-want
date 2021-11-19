<template>
  <div>
    <h1>{{ userProfile.nickname }}</h1>
    <div v-if="this.userName != this.$route.params.userName">
      <button v-if="followState" @click="changeFollowState">unfollow</button>
      <button v-else @click="changeFollowState">follow</button>
    </div>
    <button @click="clickFollow">〠</button> |
    <button @click="clickMy">✎</button> |
    <button @click="clickLike">♥︎</button>

    <div>
      <!-- 팔로우 팔로워 -->
      <div :class="{'hide': showFollow }">
        <h1>Following : {{ followingCount }}</h1>
        <h1>Follower: {{ followerCount }}</h1> 
        <button @click="clickFollowing">Following</button> | 
        <button @click="clickFollower">Follower</button>

        <following-list 
          :class="{'hide': showFollowing }" 
          :followings="userProfile.followings"
          @unfollow="decreaseFollowingCount"
          @follow="increaseFollowingCount"
        ></following-list>
        <follower-list 
          :class="{'hide': showFollower }" 
          :followers="userProfile.followers"
          @delete-follower="decreaseFollowerCount"
        ></follower-list>
      </div>

      <!-- 유저가 작성한 글 -->
      <div :class="{'hide': showMy }">
        <button @click="clickMyR">My Review</button> |
        <button @click="clickMyP">My Post</button> |
        <button @click="clickMyC">My Comment</button> 

        <my-review-list :class="{'hide': showMyR }"></my-review-list>
        <my-post-list :class="{'hide': showMyP }" :post-list="userProfile.post_set"></my-post-list>
        <my-comment-list :class="{'hide': showMyC }"></my-comment-list>
      </div>

      <!-- 유저가 좋아요한 것들 -->
      <div :class="{'hide': showLike }">
        <button @click="clickLikeM">Like Movie</button> |
        <button @click="clickLikeP">Like Post</button>

        <like-movie-list :class="{'hide': showLikeM }"></like-movie-list>
        <like-post-list :class="{'hide': showLikeP }"></like-post-list>
      </div>
    </div>
  </div>
</template>

<script>
import FollowingList from '@/components/accounts/follow/FollowingList'
import FollowerList from '@/components/accounts/follow/FollowerList'
import MyReviewList from '@/components/accounts/my/MyReviewList'
import MyPostList from '@/components/accounts/my/MyPostList'
import MyCommentList from '@/components/accounts/my/MyCommentList'
import LikeMovieList from '@/components/accounts/like/LikeMovieList'
import LikePostList from '@/components/accounts/like/LikePostList'
import { mapState } from 'vuex'
import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  components: {
    FollowingList,
    FollowerList,
    MyReviewList,
    MyPostList,
    MyCommentList,
    LikeMovieList,
    LikePostList
  },
  data() {
    return {
      userProfile: '',
      followerCount: 0,
      followingCount: 0,
      followState: false,
      // 숨기기 값들 
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
    // ------ 버튼 클릭 --------
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
      this.showLikeM = false
      this.showLikeP = true
    },
    clickLikeP() {
      this.showLikeM = true
      this.showLikeP = false
    },

    // 프로필 받아오기 
    getProfile() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/${this.$route.params.userName}/`, 
      })
        .then(res => {
          this.userProfile = res.data
          this.followerCount = res.data.followers_count
          this.followingCount = res.data.followings_count
          console.log(res.data)
        })
        .then(() => {
          this.didFollow()
        })
        .catch(err => {
          console.log(err)
        })
    },

    // follower 수 감소
    decreaseFollowerCount() {
      this.followerCount -= 1
    },
    // following 수 감소
    decreaseFollowingCount() {
      this.followingCount -= 1
    }, 
    // following 수 증가
    increaseFollowingCount() {
      this.followingCount += 1
    },

    // follow 했는지 알아보기
    didFollow() {
      this.followState = _.some(this.userProfile.followers, ['username', this.userName])
    },
    // follow 또는 언팔 하기 
    changeFollowState() {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${this.$route.params.userName}/follow/`,
        headers: this.config
      })
        .then(() => {
          this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created() {
    this.getProfile()
  },
  computed: {
    ...mapState(['userName', 'config'])
  }
}
</script>

<style>
.hide {
  display: none;
}
</style>