<template>
  <el-container>
    <el-header style="height: 64px;" v-if="$route.path !== '/show'">
      <Header></Header>
    </el-header>
    <el-main :class="{black: $route.path === '/show'}">
      <router-view></router-view>
    </el-main>

  </el-container>
</template>

<script>
import Header from '@/components/header.vue'

export default {
    name: 'LayoutIndex',
    components: {
      Header
    }
}
</script>

<style>
.black {
  background-color: #020308;
  width: 100vw;
  height: 100vh;
  margin: 0;
  padding: 0;
}
.el-container {
  height: 100%;
  width: 100%;
}
.el-footer,
.el-main {
  text-align: center;
  padding: 0;
}
.el-header {
    padding: 0;
    display: flex;
    justify-content: space-between;
  }
  .el-main {
    overflow-y: scroll;
    
    
    /* overflow: hidden; */
  }
  .el-footer {
    font-size: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

</style>