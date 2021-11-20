<template>
  <div>
    <li class="list-group-item" @click="selectVideo">
      <span>{{ video.name }}</span>
    </li>
  </div>
</template>

<script>
export default { 
  name: 'MovieVideoCItem',
  props: {
    video: Object
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  },
}
</script>

<style>

</style>