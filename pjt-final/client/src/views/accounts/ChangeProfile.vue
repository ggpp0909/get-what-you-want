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
// import swal from 'sweetalert'

import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const COORDS = "coords";

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
      newProfileImage: null,
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
          this.profileImage = `http://127.0.0.1:8000${res.data.profile_image}`
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 회원 정보 수정 완료 
    changeUserInfo() {
      let info = new FormData
      // info.append('file', this.files[0])
      // if (this.files===null) {             // 파일을 보내지 않을 경우
      //   info.append('image', [])
      // } else {
      //   info.append('image', this.files);
      // }
      // let config = {
        //     'Content-Type': 'multipart/form-data', // Content-Type을 변경해야 파일이 전송됨
      //     'Authorization': `JWT ${this.token}`
      // }
      // if (this.nickname === '') {
        //   swal ("닉네임을 입력해주세요.", {
      //     dangerMode: true,
      //   })
      // }
      // const changeInfo = {
      //   nickname: this.nickname,
      //   email: this.email,
      //   profile_image: info,
      // }
      info.append('files', this.files);
      info.append('nickname', this.nickname);
      info.append('email', this.email);

      console.log(this.files)
      console.log(info)
      
      console.log(this.files.name)
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
          this.$router.go()
        })
        .catch(err => {
          console.log(err)
        })
    },
   // 프로필 이미지 변경 
    changeProfileImg(file) {
      this.newProfileImage = URL.createObjectURL(file)
      console.log(URL.createObjectURL(file))
      
     }
     ,
    // 회원 탈퇴로 이동
    goToDelete() {
      this.$router.push({ name: 'DeleteUser' })
    },
    askForCoords() {
      navigator.geolocation.getCurrentPosition(this.handleGeoSuccess, this.handleGeoError);
    },
    handleGeoError() {
      console.log("Cant aceess geo location");
    },
    handleGeoSuccess(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  // 객체 저장
  const coordsObj = {
    latitude,
    longitude,
  };
  this.saveCoords(coordsObj);
  this.getWeather(latitude, longitude);
},

  loadCoords() {
    
    const loadedCoords = localStorage.getItem(COORDS);
    if (loadedCoords === null) {
      // 결국 getWeather 함수 실행된다. local stroage 아무것도 없으면
      // askForCoords 함수가 실행되고, 이 함수 안에서 정상적으로 위치 정보 가져오게 되면
      // handle GeoSuccess가 실행되는데, 이 안에서 API가 최종적으로 호출되기 떄문.
      this.askForCoords();
    } else {
      // getWeather 함수 호출
      // loadedCoords 문자이니 object로 바꿔준다.
      const parsedCoords = JSON.parse(loadedCoords);
      this.getWeather(parsedCoords.latitude, parsedCoords.longitude);
    }
  },
  saveCoords(coordsObj) {
  // 저장할때 string으로 바꾸기
  localStorage.setItem(COORDS, JSON.stringify(coordsObj));
},
    getWeather(lat, lng) {
      const API_KEY = "c902eb9aee51998b30d90694ef0a29f7";
        fetch(
          `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`
        ) //then 함수 : fetch가 완료 된 후 다음 함수 실행
          .then(function (response) {
            return response.json();
          })
          .then(function (json) {
            console.log(json)
            const temperature = json.main.temp;
            const place = json.name;
            // weather.innerText = `현재 ${place}의 기온은 ${temperature}° 입니다.`;
            console.log(temperature)
            console.log(place)
          });

      
    }
  },
  computed: {
    ...mapState(['userName', 'token'])
  },
  created() {
    this.getProfile()
    this.loadCoords()
  }
}
</script>

<style>

</style>