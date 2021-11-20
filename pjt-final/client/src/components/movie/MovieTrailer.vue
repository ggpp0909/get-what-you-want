<template>
  <div>
    <iframe v-if="videoId" :src="videoURI" frameborder="0" width="800" height="500"></iframe>
    <div v-else>예고편을 준비중입니다</div>
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
    videoId: [String, Boolean],
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