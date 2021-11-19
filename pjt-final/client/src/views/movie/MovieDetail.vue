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
    <movie-detail-recommend></movie-detail-recommend>
    <movie-detail-similar></movie-detail-similar>
  </div>
</template>

<script>
import MovieTrailer from '@/components/movie/MovieTrailer'
import MovieDetailRecommend from '@/components/movie/MovieDetailRecommend'
import MovieDetailSimilar from '@/components/movie/MovieDetailSimilar'
import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetail',
  components: {
    MovieTrailer,
    MovieDetailRecommend,
    MovieDetailSimilar
  },
  data() {
    return {
      movieData: null,
      posterPath: null,
      genres: null,
    }
  },
  methods: {
    getMovieDetail() {
       this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/${this.$route.params.movieId}/detail/`, 
      })
        .then(res => {
          console.log(res)
          this.movieData = res.data
          this.posterPath = `https://image.tmdb.org/t/p/w500${res.data.poster_path}`
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
    }
  },
  created() {
    this.getMovieDetail()
  }
}
</script>

<style>

</style>