<template>
  <v-container>
    <board-list></board-list>
  </v-container>
</template>

<script>
  import BoardList from '@/components/BoardList'

  export default {
    name: 'Board',
    components: {
      BoardList,
    }
  }
</script>
