<template>
  <div>
    <iframe :src="videoURI" frameborder="0" width="800" height="500"></iframe>
  </div>
</template>

<script>
// const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieTrailer',
  data() {
    return {
      videoURI: null,
    }
  },
  props: {
    videoId: String
  },
  methods: {
    // getTrailer() {
    //   const params = {
    //     key: API_KEY,
    //     part: 'snippet',
    //     q: this.inputValue,
    //     type: 'video'
    //   }
    //   this.$axios({
    //     method: 'get',
    //     url: API_URL,
    //     params,
    //   })
    //     .then(res => {
    //       this.trailer = res.data.items
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },
    getVideoURI() {
      this.videoURI = `https://www.youtube.com/embed/${this.videoId}`
    }
  },
  created() {
    this.getVideoURI()
    console.log(this.videoId)
  }
}
</script>

<style>

</style>