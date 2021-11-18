<template>
  <div>
    like movie
    <like-movie-item></like-movie-item>
  </div>
</template>

<script>
import LikeMovieItem from '@/components/accounts/like/LikeMovieItem'

export default {
  name: 'LikeMovieList',
  components: {
    LikeMovieItem,
  }
}
</script>

<style>

</style>