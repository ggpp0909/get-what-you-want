<template>
  <div>
    Follower
    <follower-item 
  
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
  //   reloadFollower(followers) {
  //     this.followers = followers
  //   }
  // }
  }
    // @follower="reloadFollower"
    //   v-for="followerItem in followers"
    //   :key="followerItem.username"
    //   :followerItem="followerItem"
}
</script>

<style>

</style> 