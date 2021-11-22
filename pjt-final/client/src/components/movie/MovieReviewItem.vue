<template>
  <div>
    <div :class="{'hide': isUpdate }">
      <div v-if="oldReview">
        <h4>{{ oldReview.content }}</h4>
        <p>{{ oldReview.is_spoiler }}</p>
        <p>{{ oldReview.rank }}</p>
        <p>{{ changeDate(oldReview.created_at) }}</p>
        <p @click="goToProfile">{{ oldReview.nickname }}</p>
        <img :src="getUserProfileImg()" alt="프로필이미지" @click="goToProfile" height="100px">
        <button @click="showInput">수정</button>
        <button @click="deleteReview">삭제</button>
      </div>
      <div v-else>
        아직 리뷰가 없습니다 ! 영화의 리뷰를 남겨보세요
      </div>
    </div>
    <div :class="{'hide': !isUpdate }">
      <input type="number" v-model="rank" value="별점">
      <v-checkbox value="True" v-model="isSpoiler" label="스포일러를 포함한 내용인가요?"></v-checkbox>
      <v-text-field v-model.trim="newReview" color="error" @keyup.enter="updateReview"></v-text-field>
      <button @click="updateReview">+</button>
      <button @click="isUpdate = !isUpdate">취소</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import _ from 'lodash'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieReviewItem',
  props: {
    oldReview: Object,
    reloadReview: Function
  },
  data() {
    return {
      newReview: null,
      rank: 0,
      isSpoiler: false,
      isSameUser: false,
      isUpdate: false,
    }
  },
  methods: {
    // 리뷰작성자 프로필로 이동 
    goToProfile() {
      this.$router.push({ name: 'Profile', params: { userName: this.oldReview.user.username } })
    },
    // 리뷰 삭제 
    deleteReview() {
      this.$axios({
        method: 'delete',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/review/${this.oldReview.id}/`, 
        headers: this.config
      })
        .then(() => {
          this.reloadReview()
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 리뷰 업뎃 
    updateReview() { 
      const reviewItem = {
        content: this.newReview,
        rank: this.rank,
        is_spoiler: this.isSpoiler ? true : false,
      }
      this.$axios({
        method: 'put',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/review/${this.oldReview.id}/`, 
        data: reviewItem,
        params: 1,
        headers: this.config
      })
        .then(() => {
          this.reloadReview()
          this.isUpdate = !this.isUpdate
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 수정 버튼 눌렸을 때, input창 나타내기 
    showInput() { 
      this.isUpdate = !this.isUpdate
      this.newReview = this.oldReview.content
      this.rank = this.oldReview.rank
      this.isSpoiler = this.oldReview.is_spoiler
    },
    // 프로필 이미지
    getUserProfileImg() {
      if (this.oldReview.user.profile_image === null) {
        return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU00i-_pNcxxQ69OH2c8MyVuHS0Q4GdMDR7w&usqp=CAU'
      } else {
        return `http://127.0.0.1:8000${this.comment.user.profile_image}`
      }
    },
    // 날짜 수정
    changeDate(date) {
      return _.join(_.slice(date, 0, 10), '')
    }
  },
  computed: {
    ...mapState(['config', 'userName'])
  },
  watch: {
    oldReview() {
      if (this.userName === this.oldReview.user.username) {
        this.isSameUser = true
      }
    }
  }
}
</script>

<style>
.hide {
  display: none;
}
</style>