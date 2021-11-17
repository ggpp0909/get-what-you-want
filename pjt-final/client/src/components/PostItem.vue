<template>
  <div>
    <h1>{{ post.title }}</h1>
  </div>
</template>

<script>
export default {
  name: 'PostItem',
  props: {
    post: {
      type: Object,
    }
  }
}
</script>

<style>

</style>