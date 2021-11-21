<template>
  <div>
    <div :class="{'show': isUpdate }">
      {{ comment.content }}
      <img :src="getUserProfileImg" alt="">
      <p>작성자: {{ comment.user.nickname }}</p>
      <p>작성일: {{ comment.created_at }}</p>
        <div v-if="isSameUser">
          <button @click="showInput">update</button> |
          <button @click="deleteComment">delete</button>
        </div>
    </div>
    <div :class="{'show': !isUpdate }">
      <v-text-field v-model.trim="field.content" color="error" @keyup.enter="updateComment"></v-text-field>
      <button @click="updateComment">완료</button>
      <button @click="isUpdate = !isUpdate">취소</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentItem',
  data() {
    return {
      field: {
        content: null,
      },
      isSameUser: false,
      isUpdate: false,
      profileImg: null,
    }
  },
  props: {
    comment: Object,
    reloadComment: Function
  },
  methods: {
    // 댓글 삭제 
    deleteComment() {
      this.$axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${this.comment.post_id}/comment/${this.comment.id}/`, 
        headers: this.config
      })
        .then(() => {
          this.reloadComment()
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 댓글 수정 
    updateComment() { 
      this.$axios({
        method: 'put',
        url: `${SERVER_URL}/community/${this.comment.post_id}/comment/${this.comment.id}/`, 
        data: this.field,
        headers: this.config
      })
        .then(() => {
          // console.log(res)
          this.reloadComment()
          this.isUpdate = !this.isUpdate
        })
        .catch(err => {
          console.log(err)
        })
    },
    showInput() { // 수정 버튼 눌렸을 때, input창 나타내기 
      this.isUpdate = !this.isUpdate
      this.field.content = this.comment.content
    },
    getUserProfileImg() {
      console.log(this.comment.profile_image)
      if (this.comment.profile_image === null) {
        return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU00i-_pNcxxQ69OH2c8MyVuHS0Q4GdMDR7w&usqp=CAU'
      } else {
        return `http://127.0.0.1:8000${this.comment.profile_image}`
      }
    }
  },
  created() {
    // 지금 로그인한 유저가 글쓴 유저인지 
    if (this.userName === this.comment.user.username) {
      this.isSameUser = true
    }
  },
  computed: {
    ...mapState(['userName', 'config'])
  }
}
</script>

<style>
.show {
  display: none;
}
</style>