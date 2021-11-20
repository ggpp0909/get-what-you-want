<template>
  <div>
    <h1>비밀번호 확인</h1>
    <div>
      <label for="password">비밀번호: </label>
      <input 
        type="password" 
        id="password"
        v-model="credentials.password"
      >
    </div>
    <button @click="login">확인</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'test',
  data: function () {
    return {
      credentials: {
        username: this.userName,
        password: null,
      }
    }
  },
  methods: {
    login() {
      this.credentials.username = this.userName
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credentials,
      })
        .then(() => {
          console.log('ok')
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  computed: {
    ...mapState(['userName'])
  }
}
</script>

<style>

</style>