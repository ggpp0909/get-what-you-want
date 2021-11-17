<template>
  <div>
    <input type="text" v-model="title">
    <input type="text" v-model="content" rows="3">
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'PostCreate',
  data() {
    return {
      title: '',
      content: '',
      id: null,
    }
  },
  computed: {
    ...mapState(['posts'])
  },
  // methods: {
  //   uploadPost() {
  //     const post_id = this.posts.length -1

  //   }
  // }
}
</script>

<style>

</style>