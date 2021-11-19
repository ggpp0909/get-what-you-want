<template>
  <div>Following
    <following-item
      v-for="following in this.followings"
      :key="following.id"
      :following-user="following"
      @unfollow="unfollow"
      @follow="follow"
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
    followings: Array,
  },
  methods: {
    unfollow() {
      this.$emit('unfollow')
    },
    follow() {
      this.$emit('follow')
    }
  }
}
</script>

<style>

</style>