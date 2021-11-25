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
      <v-container fluid>
        <v-row align="center">
          <v-col
            class="d-flex"
            cols="12"
            sm="6"
          >
            <v-select
              :items="items"
              label="탈퇴 사유"
              solo
              v-model="reason"
            ></v-select>
          </v-col>
        </v-row>
      </v-container>
      <v-textarea color="error" placeholder="탈퇴 사유를 구체적으로 입력해주세요" v-model="detailReason"></v-textarea>
      <button @click="deleteUser">회원탈퇴</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import swal from 'sweetalert'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'DeleteUser',
  data() {
    return {
      confirm: false,
      password: '',
      items: ['서비스 불만', '개인정보 유출 우려', '사이트 이용 빈도 낮음', '지구 온난화 방지를 위한 PC사용 자제', '재 가입을 위해서', '기타'],
      detailReason: null,
      reason: null
    }
  },
  methods: {
    // 유저 인증
    isUser() {
      if (this.password === '') {
          swal ("비밀번호를 입력하세요.", {
          dangerMode: true,
        })
      }
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
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 회원탈퇴
    deleteUser: function () {
      const deleteInfo = {
        reason: this.reason,
        detailReason: this.detailReason
      }
      this.$axios({
        method: 'delete',
        url: `${SERVER_URL}/accounts/withdrawal/`, 
        data: deleteInfo,
        headers: this.config
      })
        .then(() => {
          localStorage.removeItem('jwt')  // 기존 토큰 삭제 
          this.$router.push({ name: 'Home' })
          this.$store.dispatch('deleteUserName')
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