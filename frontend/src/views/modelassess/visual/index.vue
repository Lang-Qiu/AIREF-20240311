<template>
  <div>
    <div class="visual">
      <Banner>
        <h1 slot="title">视频模型评估</h1>
        <p slot="text">视频分类模型评估关注视频数据中的对象检测、行为识别、场景分类等任务。通过测量模型的准确性、时间精度、空间精度等指标，我们可以评估其对视频数据的适用性</p>
      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'VisualClassify'
}
</script>

<style>
.visual {
  background: url('../../../assets/visual_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>