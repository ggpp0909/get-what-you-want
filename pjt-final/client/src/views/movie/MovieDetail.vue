<template>
  <div>
    <h1>{{ movieData.title }}</h1>
    <img :src="posterPath" :alt="`${movieData.title} 포스터`">
    <p 
      v-for="genre in genres"
      :key="genre"
    >{{ genre }}</p>
    <p>{{ movieData.overview }}</p>
    <p>개봉일 : {{ movieData.release_data }}</p>
    <p>런타임: {{ movieData.runtime }}분</p>
    <p>상태 : {{ movieData.status }}</p>
    <p>간단소개 : {{ movieData.tagline }}</p>
    <p>평점 {{ movieData.vote_average }}</p>
    <p>투표한 사람 수 {{ movieData.vote_count }}</p>
    <movie-trailer :video-id="movieData.video_id"></movie-trailer>
    <recommend-movie-list></recommend-movie-list>
    <similar-movie-list></similar-movie-list>
    <h3>-----------</h3>
    <h3>영화 좋아요 {{ likeCount }}</h3>
    <button @click="changeLike">
      <p v-if="likeState">꽉찬 하트</p>
      <p v-else>빈 하트</p>
    </button>
  </div>
</template>

<script>
import MovieTrailer from '@/components/movie/MovieTrailer'
import RecommendMovieList from '@/components/movie/recommend/RecommendMovieList'
import SimilarMovieList from '@/components/movie/recommend/SimilarMovieList'
import _ from 'lodash'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetail',
  components: {
    MovieTrailer,
    RecommendMovieList,
    SimilarMovieList
  },
  data() {
    return {
      movieData: '',
      posterPath: null,
      genres: null,
      likeState: false,
      likeCount: '',
    }
  },
  methods: {
    getMovieDetail() {
       this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/detail/`, 
      })
        .then(res => {
          if (res.data.adult) {
            this.$router.push({ name: 'IsAdult'})
          }
          return res
        })
        .then(res => {
          console.log(res)
          this.movieData = res.data
          // 포스터 경로 설정 
          this.posterPath = `https://image.tmdb.org/t/p/w500${res.data.poster_path}`
          // 해당 영화 좋아요 상태
          this.likeState = res.data.liked
          // 좋아요 개수 
          this.likeCount = res.data.like_count
          // 장르만 뽑아내기 
          const genres = []
          _.forEach(res.data.genres, genre => {
            genres.push(genre.name)
          })
          this.genres = genres
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 좋아요
    changeLike() {
      if (this.config) {
        this.$axios({
          method: 'post',
          url: `${SERVER_URL}/movie/${this.movieData.movie_id}/like/`, 
          headers: this.config
        })
          .then(() => {
            if (this.likeState) {
              this.likeCount -= 1
            } else {
              this.likeCount += 1
            }
            this.likeState = !this.likeState
          })
          .catch(err => {
            console.log(err)
          })
      } else {
        this.$router.push({ name: 'Login' })
      }
    }
  },
  created() {
    this.getMovieDetail()
  },
  computed: {
    ...mapState(['config'])
  }
}
</script>

<style>

</style>