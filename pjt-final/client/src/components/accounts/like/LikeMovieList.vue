<template>
  <div>
    like movie
    <like-movie-item
      v-for="movie in likeMovies"
      :key=movie.movie_id
      :movie="movie"
    ></like-movie-item>
  </div>
</template>

<script>
import LikeMovieItem from '@/components/accounts/like/LikeMovieItem'

export default {
  name: 'LikeMovieList',
  components: {
    LikeMovieItem,
  },
  props: {
    likeMovies: Array,
  }
}
</script>

<style>

</style>