<template>
  <div>
    <img :src="followingItem.profile_image" alt="프로필이미지">
    {{ followingItem.nickname }}
    <button v-if="this.userName === this.$route.params.userName" @click="followingChangeState">??</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'FollowingItem',
  props: {
    followingItem: Object
  },
  methods: {
    followingChangeState() {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${this.followingItem.username}/follow/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.$emit('unfollow')
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState(['config', 'userName'])
  }
}
</script>

<style>

</style>