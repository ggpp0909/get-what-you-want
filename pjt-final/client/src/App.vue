<template>
  <v-app>
    <nav>
      <router-link :to="{ name: 'Home'}">HOME</router-link> |
      <router-link :to="{ name: 'Board'}">Board</router-link> |
      <router-link :to="{ name: 'Recommend'}">Recommend</router-link> |
      <router-link :to="{ name: 'User'}">User</router-link>
      <router-link :to="{ name: 'Signup'}">Signup</router-link>
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
