<template>
  <div>Following
    <following-item
      v-for="following in this.followingList"
      :key="following.id"
      :followingItem="following"
      @unfollow="unfollow"
    ></following-item>
  </div>
</template>

<script>
import FollowingItem from '@/components/accounts/follow/FollowingItem'

export default {
  name: 'FollowingList',
  components: {
    FollowingItem
  },
  props: {
    followingList: Array,
  },
  methods: {
    unfollow() {
      this.$emit('unfollow')
    }
  }
}
</script>

<style>

</style>