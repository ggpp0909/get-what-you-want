<template>
  <div>
    Follower
    <follower-item 
      v-for="followerItem in this.followers"
      :key="followerItem.id"
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
  props: {
    followers: Array
  },
  methods: {
  //   reloadFollower(followers) {
  //     this.followers = followers
  //   }
  // }
  }

}
</script>

<style>

</style> 