<template>
  <div>
    Follower
    <follower-item 
      @follower="reloadFollower"
      v-for="followerItem in followers"
      :key="followerItem.username"
      :followerItem="followerItem"
    ></follower-item>
  </div>
</template>

<script>
import FollowerItem from '@/components/accounts/follow/FollowerItem'

export default {
  name: 'FollowerList',
  components: {
    FollowerItem
  },
  data() {
    return {
      followers: null,
    }
  },
  methods: {
    reloadFollower(followers) {
      this.followers = followers
    }
  }
}
</script>

<style>

</style>