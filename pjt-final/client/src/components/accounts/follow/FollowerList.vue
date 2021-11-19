<template>
  <div>
    Follower
    <follower-item 
      v-for="followerItem in this.followers"
      :key="followerItem.id"
      :followerItem="followerItem"
      :reloadFollower="reloadFollower"
    ></follower-item>
  </div>
</template>

<script>
import FollowerItem from '@/components/accounts/follow/FollowerItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'FollowerList',
  components: {
    FollowerItem
  },
  data() {
    return {
      followers: this.followerList
    }
  },
  props: {
    followerList: Array
  },
  methods: {
    reloadFollower() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/${this.$route.params.userName}/`,
      })
        .then(res => {
          console.log(res.data)
          this.follower = res.data.followings
        })
        .catch(err => {
          console.log(err)
        })
    }
  }

}
</script>

<style>

</style> 