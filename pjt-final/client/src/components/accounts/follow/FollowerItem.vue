<template>
  <div>
    <img :src="followerItem.profile_image" alt="프로필이미지">
    {{ followerItem.nickname }}
    <!-- <button v-if="this.userName === this.$route.params.userName" @click="deleteFollower">삭제</button> -->
  </div>
</template>

<script>
import { mapState } from 'vuex'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'FollowerItem',
  props:{
    followerItem: Object
  },
  methods: {
    // deleteFollower() {
    //   this.$axios({
    //     method: 'delete',
    //     url: `${SERVER_URL}/`,
    //     headers: this.config
    //   })
    //     .then(() => {
    //       this.reloadFollower()
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },
    // reloadFollower() {
    //   this.$axios({
    //     method: 'get',
    //     url: `${SERVER_URL}/`,
    //   })
    //     .then(res => {
    //       this.$emit('followers', res.data)
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // }
  },
  computed: {
    ...mapState(['config'])
  }
}
</script>

<style>

</style>