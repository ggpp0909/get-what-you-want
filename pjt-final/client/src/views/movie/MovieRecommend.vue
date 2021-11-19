<template>
  <div>
    Recommend
    <popular-movie-list></popular-movie-list>
    <top-rated-movie-list></top-rated-movie-list>
    <recommend-movie-list></recommend-movie-list>
    <similar-movie-list></similar-movie-list>
  </div>
</template>

<script>
import PopularMovieList from '@/components/movie/recommend/PopularMovieList'
import TopRatedMovieList from '@/components/movie/recommend/TopRatedMovieList'
import RecommendMovieList from '@/components/movie/recommend/RecommendMovieList'
import SimilarMovieList from '@/components/movie/recommend/SimilarMovieList'

export default {
  name: 'Recommend',
  components: {
    PopularMovieList,
    TopRatedMovieList,
    RecommendMovieList,
    SimilarMovieList,
  }
}
</script>

<style>

</style>