<template>
  <div>
    <h1>BoardList</h1>
    <board-item
      v-for="(board, idx) in getBoardItem"
      :key="idx"
      :board="board"
    >
    </board-item>
  </div>
</template>

<script>
import BoardItem from '@/components/BoardItem'

export default {
  name: 'BoardList',
  components: {
    BoardItem,
  },
  computed: {
    getBoardItem() {
      return this.$store.state.boards
    }
  }
}
</script>

<style>

</style>