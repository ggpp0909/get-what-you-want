<template>
  <div>
    <div :class="{'hide': isUpdate }">
      <div @click="goToProfile">
        <h4>{{ oldReview.content }}</h4>
        <p>{{ oldReview.is_spoiler }}</p>
        <p>{{ oldReview.rank }}</p>
        <p>{{ oldReview.created_at }}</p>
        <p>{{ oldReview.nickname }}</p>
        <img :src="oldReview.profile_image" alt="프로필이미지">
      </div>
      <button @click="showInput">수정</button>
      <button @click="deleteReview">삭제</button>
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
    goToProfile() {
      this.$router.push({ name: 'Profile', params: { userName: this.oldReview.user.username } })
    },
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
    showInput() { // 수정 버튼 눌렸을 때, input창 나타내기 
      this.isUpdate = !this.isUpdate
      this.newReview = this.oldReview.content
      this.rank = this.oldReview.rank
      this.isSpoiler = this.oldReview.is_spoiler
    },
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