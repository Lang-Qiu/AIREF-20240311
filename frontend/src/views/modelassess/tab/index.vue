<template>
  <div>
    <div class="tab">
      <Banner>
        <h1 slot="title">表格模型评估</h1>
        <p slot="text">表格分类模型是一种用于自动识别和分类表格数据的工具。这些模型可应用于文档自动化、数据抽取和结构化信息提取。它们可以识别表格中的列、行和数据内容，以支持各种应用程序</p>
        <img slot="image" src="../../../assets/rightimg.png" alt="" style="width: 220px;">
      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'TabClassify'
}
</script>

<style>
.tab {
  background: url('../../../assets/bj.png') no-repeat;
  background-size: 100% 100%;
}
</style>