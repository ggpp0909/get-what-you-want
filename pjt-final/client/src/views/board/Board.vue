<template>
  <v-container>
    <post-list></post-list>
   <v-row>
      <v-col class="pa-2">
        <button @click="postCreate">Create</button>
      </v-col>
      <v-col>
        <!-- 검색 -->
        <v-text-field v-model.trim="searchMovie" @keyup.enter="searchSearch" 
            placeholder="검색어를 입력하세요" outlined dense label="Search Movie" >
          <v-icon slot="append" @click="searchSearch">mdi-magnify</v-icon>
        </v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import PostList from '@/components/PostList'

  export default {
    name: 'Board',
    components: {
      PostList,
    },
    methods: {
      postCreate() {
        const token = localStorage.getItem('jwt')
        if (token) { // 로그인 상태 -> 게시글 생성 
          this.$router.push({ name: 'PostCreate', params: { postId: 0 }})
        } else {    // 비로그인 상태 -> 로그인 
          this.$router.push({ name: 'Login' })
        }
      },
    },
  }
</script>
