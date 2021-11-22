<template>
  <div>
    <h1>회원 정보 수정 페이지</h1>
    <div>
      <input type="text" v-model="nickname">
      <input type="email" v-model="email">
      <v-file-input v-model="files" name="files" label="File input" @change="changeProfileImg"></v-file-input>
      <img :src="profileImage" alt="기존 프로필이미지" height="100">
      <img :src="newProfileImage" alt="새 프로필이미지" height="100">
      <button @click="changeUserInfo">회원 정보 수정 완료</button>

      <change-password></change-password>
      <button @click="goToDelete">회원 탈퇴 </button>
    </div>
  </div>
</template>

<script>
import ChangePassword from '@/views/accounts/ChangePassword'
import swal from 'sweetalert'

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
      newProfileImage: 'https://mblogthumb-phinf.pstatic.net/MjAxODA0MTBfMjI2/MDAxNTIzMzY2MjI5Nzk0.xDtjpIX7dGFtPIY5sakKXpIF6295RrBbaF88VDSGyEEg.WRuXJKeZJNbiaNzyceStJLk7Imcn5fk3MpWZbn5g1wcg.JPEG.0ooz05/%EB%B9%84%EA%B3%B5%EA%B0%9C_%EC%95%84%EB%B0%94%ED%83%80.jpg?type=w800',
      files: null
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
          if (res.data.profile_image === null) {
            this.profileImage = this.profileImg
          } else {
            this.profileImage = `http://127.0.0.1:8000${res.data.profile_image}`
            this.$store.dispatch('setUserProfileImg', res.data.profile_image)
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 회원 정보 수정 완료 
    changeUserInfo() {
      if (this.nickname === '') {
          swal ("닉네임을 입력해주세요.", {
          dangerMode: true,
        })
      }
      // 수정 데이터 넣기 
      let info = new FormData
      info.append('files', this.files);
      info.append('nickname', this.nickname);
      info.append('email', this.email);
      // 서버에 수정 요청 
      this.$axios({
        method: 'put',
        url: `${SERVER_URL}/accounts/change_profile/`,
        data: info,
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `JWT ${this.token}`
        }
      })
        .then(() => {
          this.getProfile()
          this.profileImage = 'https://mblogthumb-phinf.pstatic.net/MjAxODA0MTBfMjI2/MDAxNTIzMzY2MjI5Nzk0.xDtjpIX7dGFtPIY5sakKXpIF6295RrBbaF88VDSGyEEg.WRuXJKeZJNbiaNzyceStJLk7Imcn5fk3MpWZbn5g1wcg.JPEG.0ooz05/%EB%B9%84%EA%B3%B5%EA%B0%9C_%EC%95%84%EB%B0%94%ED%83%80.jpg?type=w800'
        })
        .catch(err => {
          console.log(err)
        })
    },
   // 프로필 이미지 미리보기 
    changeProfileImg(file) {
      this.newProfileImage = URL.createObjectURL(file)
     }
     ,
    // 회원 탈퇴로 이동
    goToDelete() {
      this.$router.push({ name: 'DeleteUser' })
    },
  },
  computed: {
    ...mapState(['userName', 'token', 'profileImg'])
  },
  created() {
    this.getProfile()
  }
}
</script>

<style>

</style>