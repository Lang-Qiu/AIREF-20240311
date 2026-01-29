<template>
  <div>
    <div class="image">
      <Banner>
        <h1 slot="title">图像模型评估</h1>
        <p slot="text">图像分类模型评估是一种用于测量计算机视觉模型性能的方法。它涵盖了图像识别、目标检测和图像分割等领域。通过评估精确度、召回率、F1分数等指标，该评估有助于确定模型的性能和适用性</p>
        
      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'ImageClassify'
}
</script>

<style>
.image {
  background: url('../../../assets/image_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>