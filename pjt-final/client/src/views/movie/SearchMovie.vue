<template>
  <div>
    <h1>{{ this.$route.params.keyword }} 검색 결과</h1>
    <div v-if="searchResult">
      <search-movie-item
        v-for="movie in searchResult"
        :key="movie.id"
        :movie="movie"
      ></search-movie-item>
    </div>
    <div v-else>
      <h1>검색 결과가 없습니다.</h1>
    </div>
    
  </div>
</template>

<script>
import SearchMovieItem from '@/components/movie/SearchMovieItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Search',
  components:{
    SearchMovieItem,
  },
  data() {
    return {
      keyword: this.$route.params.keyword,
      searchResult: null,
    }
  },
  methods: {
    search() {
      this.$axios({
        method: 'get',
          url: `${SERVER_URL}/movie/${this.$route.params.keyword}/search/`,
       })
        .then(res => {
          this.searchResult = res.data.length > 0 ? res.data : false
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created() {
    this.search()
  }
}
</script>

<style>

</style>