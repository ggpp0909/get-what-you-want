<template>
  <div>
    <div v-if="!confirm">
      <h1>비밀번호 확인</h1>
      <div>
        <label for="password">비밀번호: </label>
        <input 
          type="password" 
          id="password"
          v-model="password"
          @keyup.enter="isUser"
        >
      </div>
      <button @click="isUser">확인</button>
    </div>
    <div v-else>
      <div>
      <label for="password">새 비밀번호: </label>
      <input 
        type="password" 
        id="password"
        v-model="password"
      >
      </div>
      <div>
        <label for="passwordConfirmation">새 비밀번호 확인: </label>
        <input
          type="password" 
          id="passwordConfirmation"
          v-model="passwordConfirmation"
          @keyup.enter="changePassword"
        >
      </div>
      <button @click="changePassword">비밀번호 수정</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ChangePassword',
  data: function () {
    return {
      confirm: false,
      password: null,
      passwordConfirmation: null,
    }
  },
  methods: {
    // 유저 인증
    isUser() {
      const credentials = {
        username: this.userName,
        password: this.password
      }
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: credentials,
      })
        .then(() => {
          this.confirm = true
          this.password = null
          this.changePassword()
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 비밀번호 변경 
    changePassword: function () {
      const credential2 = {
        password: this.password,
        passwordConfirmation: this.passwordConfirmation
      }
      this.$axios({
        method: 'put',
        url: `${SERVER_URL}/accounts/change_password/`, 
        data: credential2,
        headers: this.config
      })
        .then(() => {
          localStorage.removeItem('jwt')  // 기존 토큰 삭제 
          const credential3 = {
            username: this.userName,
            password: this.password,
          }
          this.$axios({ // 새 토큰 발급 
            method: 'post',
            url: `${SERVER_URL}/accounts/api-token-auth/`,
            data: credential3,
          })
            .then(res => {
              localStorage.setItem('jwt', res.data.token)
              this.$emit('login')
              this.$store.dispatch('setToken')  // 토큰 state에 저장 
              this.$router.go() // 새로고침 
            })
            .catch(err => {
              console.log(err)
            })
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState(['userName', 'config'])
  }
}
</script>

<style>

</style>