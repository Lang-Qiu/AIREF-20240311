<template>
  <div class="kuangjia">
      <h1>产品框架图</h1>
      <div class="kuangjia_main">
        <img src="../assets/kuangjia.jpg" alt="">
      </div>
    </div>
</template>

<script>
export default {
    name: 'KuangJia'
}
</script>

<style lang="less" scoped>
.kuangjia {
  background-color: #fff;
  h1 {
      text-align: center;
      padding: 50px 0;
    }
  .kuangjia_main {
   
    img {
      width: 1200px;
    }
  }
}
</style>