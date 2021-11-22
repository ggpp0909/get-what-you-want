<template>
  <div>
    <b-table-simple hover small caption-top responsive>
      <colgroup><col><col><col><col></colgroup>
      <b-thead head-variant="dark">
        <b-tr>
          <b-th colspan="1">number</b-th>
          <b-th colspan="5">Title</b-th>
          <b-th colspan="4">User</b-th>
          <b-th colspan="2">Date</b-th>
        </b-tr>
      </b-thead>
      <!-- 게시글 목록 -->
      <b-tbody v-if="isPost">
        <b-tr v-for="(post, index) in posts"
            :key="post.id"
            @click="postDetail(post.id)"
        >
          <b-td >{{ index+1 }}</b-td>
          <b-th >{{ post.title }}</b-th>
          <b-td  
            v-for="user in post" 
            :key="user.id"
          >
            <!-- <img :src="`http://127.0.0.1:8000${user.profile_image}`" alt="" height="30"> -->
            {{ user.nickname }}
          </b-td>
          <b-td>{{changeDate(post.created_at)}}</b-td>
        </b-tr>
      </b-tbody>
      <b-tbody v-else>
        <b-td colspan="12" rowspan="3" class="text-center">{{ this.searchBeforeKeyword }}에 해당하는 게시글이 없습니다.</b-td>
      </b-tbody>
    </b-table-simple>
  </div>
</template>

<script>
import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'PostList',
  data() {
    return {
      posts: null,
    }
  },
  props: {
    isPost: Boolean
  },
  methods: {
    // 클릭한 게시글로 이동 
    postDetail(id) {
      this.$router.push({ name: 'PostDetail', params: { postNum: id } })
    },
    // 전체 게시글 서버에서 불러오기 
    getPosts() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/community/`,
      })
        .then(res => {
          this.posts = res.data
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    changeDate(date) {
      return _.join(_.slice(date, 0, 10), '')
    },
  },
  created() {
    this.getPosts()
  }
}
</script>

<style>
.searchBar {
  margin-right: 0px;
  padding-left: 100px;
}
</style>