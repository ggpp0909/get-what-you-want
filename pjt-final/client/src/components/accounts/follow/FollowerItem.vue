<template>
  <div>
    <img :src="follower.profile_image" alt="프로필이미지">
    {{ follower.nickname }}
    <button v-if="this.userName === this.$route.params.userName" @click="deleteFollower(followerItem.username)">삭제</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'FollowerItem',
  data() {
    return {
      follower: this.followerItem
    }
  },
  props:{
    followerItem: Object,
    reloadFollower: Function
  },
  methods: {
    // 팔로우 삭제 
    deleteFollower(deleteUserName) {
      this.$axios({
        method: 'delete',
        url: `${SERVER_URL}/accounts/${this.userName}/delete/${deleteUserName}/`,
        headers: this.config
      })
        .then(() => {
          this.reloadFollower()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed: {
    ...mapState(['config'])
  }
}
</script>

<style>

</style>