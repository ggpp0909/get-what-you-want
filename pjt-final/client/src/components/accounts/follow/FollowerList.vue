<template>
  <div>
    Follower
    <follower-item 
      v-for="follower in followerUsers"
      :key="follower.id"
      :follower="follower"
      @reload-follower="reloadFollower"
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
      followerUsers: this.followers,
    }
  },
  props: {
    followers: Array,
  },
  methods: {
    // 팔로워 삭제했을때 리스트 업뎃 및 숫자 감소
    reloadFollower(newFollowers) {
      this.followerUsers = newFollowers
      this.$emit('delete-follower')
    }
  }, 
  watch: {
    followers() {
      this.followerUsers = this.followers
    }
  },
}
</script>

<style>

</style> 