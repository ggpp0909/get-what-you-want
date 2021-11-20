<template>
  <div>
    <h1>회원 정보 수정 페이지</h1>
    <div>
      <input type="text" v-model="nickname">
      <input type="email" v-model="email">
      <img :src="profileImage" alt="프로필이미지">
      <button @click="changeUserInfo">회원 정보 수정 완료</button>
      <change-password></change-password>
      <button @click="goToDelete">회원 탈퇴 </button>
    </div>
  </div>
</template>

<script>
import ChangePassword from '@/views/accounts/ChangePassword'

import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ChangeProfile',
  components: {
    ChangePassword
  },
  data() {
    return {
      nickname: null,
      email: null,
      profileImage: null,
    }
  },
  methods: {
    // 프로필 받아오기 
    getProfile() {
      this.$axios({
      method: 'get',
      url: `${SERVER_URL}/accounts/${this.userName}/`, 
      })
        .then(res => {
          this.nickname = res.data.nickname
          this.email = res.data.email
          this.profileImage = res.data.profile_image
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 회원 정보 수정 완료 
    changeUserInfo() {
      const changeInfo = {
        nickname: this.nickname,
        email: this.email,
        profile_image: this.profileImage
      }
      this.$axios({
        method: 'put',
        url: `${SERVER_URL}/accounts/change_profile/`,
        data: changeInfo,
        headers: this.config
      })
        .then(() => {
          this.$router.go()
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 회원 탈퇴로 이동
    goToDelete() {
      this.$router.push({ name: 'DeleteUser' })
    }
  },
  computed: {
    ...mapState(['userName', 'config'])
  },
  created() {
    this.getProfile()
  }
}
</script>

<style>

</style>