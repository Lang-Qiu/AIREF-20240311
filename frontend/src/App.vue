<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
  // mounted() {
  //   console.log(this.$route.path);
  // }
}
</script>

<style lang="scss" scoped>
#app {
  width: 100%;
  height: 100%;
  // overflow-y: scroll;
}
</style>