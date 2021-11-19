<template>
  <div>
    <iframe :src="videoURI" frameborder="0" width="800" height="500"></iframe>
  </div>
</template>

<script>
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
    getVideoURI() {
      this.videoURI = `https://www.youtube.com/embed/${this.videoId}`
    }
  },
  created() {
    this.getVideoURI()
  }
}
</script>

<style>

</style>