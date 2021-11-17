<template>
  <v-app>
    <nav>
      <router-link to='/'>HOME</router-link> |
      <router-link to='/board'>Board</router-link> |
      <router-link to='/recommend'>Recommend</router-link> |
      <router-link to='/user'>User</router-link>
    </nav>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
