<template>
  <div>
    <div>
      <h1>Signup</h1>
      <div>
        <label for="username">아이디: </label>
        <input 
          type="text" 
          id="username"
          v-model="credentials.username"
        >
      </div>
      <div>
        <label for="nickname">닉네임: </label>
        <input 
          type="text" 
          id="nickname"
          v-model="credentials.nickname"
        >
      </div>
      <div>
        <label for="password">비밀번호: </label>
        <input 
          type="password" 
          id="password"
          v-model="credentials.password"
        >
      </div>
      <div>
        <label for="passwordConfirmation">비밀번호 확인: </label>
        <input
          type="password" 
          id="passwordConfirmation"
          v-model="credentials.passwordConfirmation"
          @keyup.enter="signup"
        >
      </div>
      <div>
        <label for="email">이메일: </label>
        <input 
          type="email" 
          id="email"
          v-model="credentials.email"
        >
      </div>
      <button @click="signup">회원가입</button>
    </div>
    <div>
      <after-signup></after-signup>
    </div>
  </div>
</template>

<script>
// template에서 aftersignup이랑 본체 div로 구분해놨어요
import AfterSignup from '@/views/accounts/AfterSignup'///
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  components: {////
    AfterSignup
  },
  data: function () {
    return {
      credentials: {
        username: null,
        nickname: null,
        password: null,
        passwordConfirmation: null,
        email: null,
      },
      genres: ['18', '16'] ////
    }
  },
  methods: {
    signup: function () {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/signup/`, 
        data: this.credentials,
      })
        .then(() => {
          this.$axios({
            method: 'post',
            url: `${SERVER_URL}/accounts/api-token-auth/`,
            data: this.credentials,
          })
            .then(res => {
              localStorage.setItem('jwt', res.data.token)
              this.$emit('login')
              this.$store.dispatch('setUserName', this.credentials.username)  // 로그인한 유저 아이디 저장 
              this.$store.dispatch('setToken')  // 토큰 state에 저장
            })
              .then(() => {////
                this.getMovies()/////
                this.$router.push({ name: 'Home' })//// 위의 then에서 위치 옮김
              })
            .catch(err => {
              console.log(err)
            })
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMovies() {
       this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/signup_like/`,
        data: credentials
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>