<template>
  <div>
    <h1>{{ board.title }}</h1>
    {{ board.content }}
  </div>
</template>

<script>
export default {
  name: 'BoardItem',
  props: {
    board: {
      type: Object,
    }
  }
}
</script>

<style>

</style>