<template>
  <div>
    <div @click="goToUserProfile">
      <img :src="followingUser.profile_image" :alt="`${ followingUser.nickname }님의 프로필 사진`">
      {{ followingUser.nickname }}
    </div>
    
    <!-- <button 
      v-if="this.userName === this.$route.params.userName" 
      @click="followingChangeState"
    >??</button> -->
    <div v-if="this.userName === this.$route.params.userName" >
      <button :class="{ 'hide' : !followState }" @click="followingChangeState">unfollow</button>
      <button :class="{ 'hide' : followState }" @click="followingChangeState">follow</button>
    </div>
    
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'FollowingItem',
  data() {
    return {
      followState: true,
    }
  },
  props: {
    followingUser: Object
  },
  methods: {
    followingChangeState() {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${this.followingUser.username}/follow/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          if (this.followState) {
            this.$emit('unfollow')
            this.followState = false
          } else {
            this.$emit('follow')
            this.followState = true
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 클릭한 유저 프로필로 이동
    goToUserProfile() {
      this.$router.push({ name: 'Profile', params: { userName: this.followingUser.username } })
    }
  },
  computed: {
    ...mapState(['config', 'userName'])
  },
}
</script>

<style>
.hide {
  display: none;
}
</style>