<template>
  <div>
    <div>
      <h1>Signup</h1>
      <!-- <div>
        <label for="username">아이디: </label>
        <input 
          type="text" 
          id="username"
          v-model="credentials.username"
        >
      </div> -->
      <v-text-field
        v-model="credentials.username"
        label="ID"
      ></v-text-field>

      <!-- <div>
        <label for="nickname">닉네임: </label>
        <input 
          type="text" 
          id="nickname"
          v-model="credentials.nickname"
        >
      </div> -->
      <v-text-field
        v-model="credentials.nickname"
        label="Nickname"
      ></v-text-field>

      <!-- <div>
        <label for="password">비밀번호: </label>
        <input 
          type="password" 
          id="password"
          v-model="credentials.password"
        >
      </div> -->
      <v-text-field
        v-model="credentials.password"
        :append-icon="credentials.show1 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[credentials.rules.required, credentials.rules.min]"
        :type="credentials.show1 ? 'text' : 'password'"
        name="input-10-1"
        label="Password"
        @click:append="credentials.show1 = !credentials.show1"
      ></v-text-field>
      
      <!-- <div>
        <label for="passwordConfirmation">비밀번호 확인: </label>
        <input
          type="password" 
          id="passwordConfirmation"
          v-model="credentials.passwordConfirmation"
          @keyup.enter="signup"
        >
      </div> -->
      <v-text-field
        v-model="credentials.passwordConfirmation"
        :type="credentials.show2 ? 'text' : 'password'"
        name="input-10-1"
        label="Password Confirmation"
        @click:append="credentials.show2 = !credentials.show2"
      ></v-text-field>
<!-- 
      <div>
        <label for="email">이메일: </label>
        <input 
          type="email" 
          id="email"
          v-model="credentials.email"
        >
      </div> -->
      <v-text-field
        v-model="credentials.email"
        label="E-Mail"
      ></v-text-field>


      <v-select
        v-model="credentials.values"
        :items="credentials.items"
        chips
        label="Chips"
        multiple
        solo
        item-text="name"
        item-value="value"
      ></v-select>

      <v-divider></v-divider>
      <!-- <button @click="signup">회원가입</button> -->
      <v-btn
        elevation="1"
        outlined
        rounded
        @click="signup"
      >Sign Up</v-btn>

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
        passwordConfirmation: '',
        email: null,
        show1: false,
        show2: false,
        password: '',
        rules: {
          required: value => !!value || '비밀번호를 입력하세요.',
          min: v => v.length >= 8 || '비밀번호는 8글자 이상입니다.',
        },
        values: [],
        items: [
          { name: 'SF', value: '878' },
          { name: 'TV 영화', value: '10770' },
          { name: '가족', value: '10751' },
          { name: '공포', value: '27' },
          { name: '드라마', value: '18' },
          { name: '로맨스', value: '10749' },
          { name: '모험', value: '12' },
          { name: '미스터리', value: '9648' },
          { name: '범죄', value: '80' },
          { name: '서부', value: '37' },
          { name: '스릴러', value: '53' },
          { name: '애니메이션', value: '16' },
          { name: '액션', value: '28' },
          { name: '역사', value: '36' },
          { name: '음악', value: '10402' },
          { name: '판타지', value: '14' },
          { name: '전쟁', value: '10752' },
          { name: '코미디', value: '35' },
        ]
      },
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
              this.$store.dispatch('setUserName', this.credentials.username)  // 로그인한 유저 아이디 저장 
              this.$store.dispatch('setToken')  // 토큰 state에 저장
              this.$router.push({ name: 'Home' })//// 위의 then에서 위치 옮김
            })
              // .then(() => {////
              //   // this.getMovies()/////
              // })
            .catch(err => {
              console.log(err)
            })
          // like movie
          this.$axios({
            method: 'post',
            url: `${SERVER_URL}/movie/signup_like/`, 
            data: this.credentials.values,
          })
            .then(res => {
              console.log(res)
            })
            .catch(err => {
              console.log(err)
            })
            })
            .catch(err => {
              console.log(err)
            })
    },
    // getMovies() {
    //    this.$axios({
    //     method: 'get',
    //     url: `${SERVER_URL}/movie/signup_like/`,
    //     data: credentials
    //   })
    //     .then(res => {
    //       console.log(res)
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },
  },

}
</script>