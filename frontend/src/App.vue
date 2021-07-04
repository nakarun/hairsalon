<template>
  <v-app>
    <main class="container mt-5 p-5">
      <router-view />
    </main>
  </v-app>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

main.container {
  border: 1px solid #cccccc;
  width: 600px;
}
</style>
