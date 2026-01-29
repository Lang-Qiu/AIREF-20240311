<template>
  <div>
    <div class="audio">
      <Banner>
        <h1 slot="title">音频模型评估</h1>
        <p slot="text">音频分类模型评估涵盖了声音识别、音乐分类和环境音分类等领域。这种评估旨在测量模型对声音数据的准确性和性能。指标可能包括准确率、混淆矩阵等</p>
      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'AudioClassify'
}
</script>

<style>
.audio {
  background: url('../../../assets/audio_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>