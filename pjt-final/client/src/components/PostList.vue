<template>
  <div>
    <v-row >
      <v-col md="2"><h1>BOARD</h1></v-col>
      <v-col md="4" offset-md="6" class="searchInput">
        <v-text-field v-model.trim="searchKeyword" @keyup.enter="searchPost" 
            placeholder="검색어를 입력하세요" dense flat shaped label="Search Movie">
          <v-icon slot="append" @click="searchPost">mdi-magnify</v-icon>
        </v-text-field>
      </v-col>
    </v-row>
    <b-table-simple hover small caption-top responsive id="my-table"
      :current-page="currentPage">
      <colgroup><col><col><col><col></colgroup>
      <b-thead head-variant="dark">
        <b-tr>
          <b-th  class="text-center">ID</b-th>
          <b-th colspan="4" class="text-center">TITLE</b-th>
          <b-th colspan="2" class="text-center">USER</b-th>
          <b-th  class="text-center">DATE</b-th>
        </b-tr>
      </b-thead>
      <!-- 게시글 목록 -->
      <b-tbody v-if="isPost">
        <b-tr v-for="(post, index) in posts"
            :key="post.id"
            @click="postDetail(post.id)"
        >
          <b-td class="text-center">{{ index+1 }}</b-td>
          <b-td class="text-center" colspan="4">{{ post.title }}</b-td>
          <b-td  
            v-for="user in post" 
            :key="user.id"
            class="text-center"
          >
            <img :src="getUserProfileImg(user.profile_image)" alt="" height="30">
            {{ user.nickname }}
          </b-td>
          <b-td class="text-center">{{changeDate(post.created_at)}}</b-td>
        </b-tr>
      </b-tbody>
      <!-- 게시글 없을때 -->
      <b-tbody v-else>
        <b-td colspan="12" rowspan="3" class="text-center">{{ this.searchBeforeKeyword }}에 해당하는 게시글이 없습니다.</b-td>
      </b-tbody>
    </b-table-simple>
    <!-- pagination -->
    <v-pagination
      v-model="currentPage"
      :length="totalPage"
      @input="goToPage"
      :max-pages="3"
    ></v-pagination>
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
      searchKeyword: null,
      searchBeforeKeyword: null,
      isPost: true,
      currentPage: 1,
      totalPage: 1, 
    }
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
        params: {page: this.currentPage}
      })
        .then(res => {
          this.posts = _.slice(res.data, 0, res.data.length-1)
          this.totalPage = _.last(res.data).possible_page
        })
        .catch(err => {
          console.log(err)
        })
    },
    changeDate(date) {
      return _.join(_.slice(date, 0, 10), '')
    },
    // 페이지 이동
    goToPage() {
      this.getPosts()
    },
    // 게시글 검색
    searchPost() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/community/${this.searchKeyword}/search/`,
      })
        .then(res => {
          this.posts = res.data
          this.isPost = this.posts.length > 0 ? true : false
          this.searchBeforeKeyword = this.searchKeyword
          this.searchKeyword = null
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 프로필 이미지
    getUserProfileImg(img) {
      if (img === null) {
        return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU00i-_pNcxxQ69OH2c8MyVuHS0Q4GdMDR7w&usqp=CAU'
      } else {
        return `http://127.0.0.1:8000${img}`
      }
    },
  },
  created() {
    this.getPosts()
  }
}
</script>

<style scoped lang="scss">
.searchBar {
  margin-right: 0px;
  padding-left: 100px;
}

$pagination-item  :70pxs;
</style>

<style scoped>
::v-deep .v-pagination__item {
  border-radius: 0px;
  margin: 0px;
  box-shadow: none;
}
::v-deep .v-pagination__item--active.primary {
  background-color: black !important;
}
::v-deep .v-pagination__navigation {
  border-radius: 0px;
}
</style>