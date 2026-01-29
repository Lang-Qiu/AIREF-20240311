<template>
  <div>
    <div class="text">
      <Banner>
        <h1 slot="title">文本模型评估</h1>
        <p slot="text">文本分类模型评估旨在衡量自然语言处理（NLP）模型在文本分类任务中的性能。它包括情感分析、垃圾邮件检测、主题分类等任务。通过评估准确性、精确度、召回率等指标，我们可以了解模型在不同文本分类任务中的表现</p>
      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'TextClassify'
}
</script>

<style>
.text {
  background: url('../../../assets/text_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>