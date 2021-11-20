<template>
  <div>

  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Search',
  methods: {
    search() {
      this.$axios({
        method: 'get',
          url: `${SERVER_URL}/movie/${this.$route.params.postNum}/search/`,
          data: this.searchMovie
       })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
    
  }
}
</script>

<style>

</style>