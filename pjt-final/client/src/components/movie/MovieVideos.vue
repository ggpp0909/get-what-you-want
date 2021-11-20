<template>
  <div>
    <h3>예고</h3>
    <iframe :src="getVideoURI()" frameborder="0" width="800" height="500"></iframe>
    <h3>{{ representVideo.name }}</h3>
    <!-- <div>예고편을 준비중입니다</div> -->
    <movie-video-c-list
      v-if="notRVideos"
      :cVideoList="notRVideos"
      @select-video="onSelectVideo"
    ></movie-video-c-list>
  </div>
</template>

<script>
import MovieVideoCList from '@/components/movie/MovieVideoCList'

export default {
  name: 'MovieVideos',
  components: {
    MovieVideoCList
  },
  data() {
    return {
      notRVideos: [],
      representVideo: '',
      videoAllList: this.videoList
    }
  },
  props: {
    videoList: Array
  },
  methods: {
    getVideoURI() {
      return `https://www.youtube.com/embed/${this.representVideo.video_id}`
    },
    onSelectVideo(video) {
      this.representVideo = video
    },
    chooseRVideo() { // 대표 메인 비디오 골라내기
      const videoListWithoutT = this.videoAllList.filter(video => {
        return video.type != "Trailer"
      })
      const videoListT = this.videoAllList.filter(video => {
        return video.type === "Trailer"
      })
      this.representVideo = videoListT[0]
      this.notRVideos = [
        ...videoListT,
        ...videoListWithoutT
      ]
      this.notRVideos = this.notRVideos.length > 1 ? this.notRVideos : false
    }
  },
  watch: {
    videoList() {
      this.videoAllList = this.videoList
      this.chooseRVideo()
    }
  }
}
</script>

<style>

</style>