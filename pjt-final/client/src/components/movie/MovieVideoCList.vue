<template>
  <div>
    <h3>후보 영화</h3>
    <movie-video-c-item
      v-for="cVideo in propcVideoList"
      :key=cVideo.video_id
      :video="cVideo"
       @select-video="onSelectVideo"
    ></movie-video-c-item>
  </div>
</template>

<script>
import MovieVideoCItem from '@/components/movie/MovieVideoCItem'

export default { 
  name: 'MovieVideoCList',
  components: {
    MovieVideoCItem
  },
  props: {
    cVideoList: Array,
  },
  data() {
    return {
      propcVideoList: this.cVideoList
    }
  },
  methods: {
    onSelectVideo(video) {
      this.$emit('select-video', video)
    }
  },
  watch: {
    cVideoList() {
      this.propcVideoList = this.cVideoList
    }
  }

}
</script>

<style>

</style>