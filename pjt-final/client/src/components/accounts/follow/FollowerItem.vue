<template>
  <div>
    <div @click="goToUserProfile">
      <img :src="follower.profile_image" alt="프로필이미지">
      {{ follower.nickname }}
    </div>
    <button v-if="this.userName === this.$route.params.userName" @click="deleteFollower(follower.username)">삭제</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'FollowerItem',
  props:{
    follower: Object
  },
  methods: {
    // 팔로우 삭제 
    deleteFollower(deleteUserName) {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${this.userName}/delete/${deleteUserName}/`,
        headers: this.config
      })
        .then(res => {
          this.$emit('reload-follower', res.data.followers) // 새로 받은 follower 리스트 올려주기 
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 클릭한 유저 프로필로 이동
    goToUserProfile() {
      // if (this.follower.username === this.userName) { // NavigationDuplicated 방지 
      //   console.log(this.follower.username)
      //   this.$router.go(this.$router.currentRoute)
      // } else {
      //   this.$router.push({ name: 'Profile', params: { userName: this.follower.username } })
      // }
      this.$router.push({ name: 'Profile', params: { userName: this.follower.username } })
      
    }
  },
  computed: {
    ...mapState(['config', 'userName'])
  },
  created() {
    console.log('item')
    console.log(this.follower.username)
  }
}
</script>

<style>

</style>