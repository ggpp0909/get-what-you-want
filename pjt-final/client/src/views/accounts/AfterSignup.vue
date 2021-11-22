<template>
  <div>
    <h1>환영합니다</h1>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'AfterSignup',
  data: function () {
    return {
      // credentials:{
      //   'movie_id': null,
      //   'title': null,
      //   'poster_path': null,
      //   'genre_ids': null
      // }
    }
  },
  methods: {
    getMovies() {
       this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movie/signup_like/`,
        // data: credentials
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.getMovies()
  },
}

</script>

<style>

</style>