<template>
  <v-container>
    <post-list></post-list>
  <button @click="postCreate">Create</button>
  </v-container>
</template>

<script>
  import PostList from '@/components/PostList'

  export default {
    name: 'Board',
    components: {
      PostList,
    },
    methods: {
      postCreate() {
        this.$router.push({ name: 'PostCreate'})
      }
    }
  }
</script>
