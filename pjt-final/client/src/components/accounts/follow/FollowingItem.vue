<template>
  <div>
    following item
    <button v-if="this.userName === this.$route.params.userName" @click="followingChangeState">??</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'FollowingItem',
  data() {
    return {
      
    }
  },
  methods: {
    followingChangeState() {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/`,
        headers: this.config
      })
        .then(() => {
          
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