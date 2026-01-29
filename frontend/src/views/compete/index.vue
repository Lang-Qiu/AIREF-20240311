<template>
  <div>
    <div class="compete">
      <Banner>
        <h1 slot="title">对抗攻击测评</h1>
        <p slot="text">对抗样本就是指在原始样本添加一些人眼无法察觉的扰动（这样的扰动不会影响人类的识别，但是却很容易愚弄模型），致使机器做出错误的判断。利用对抗样本对Ai模型进行攻击的方法被称为对抗攻击。本平台可以生成对抗样本，评估ai模型在受到对抗攻击时的表现，并生成测评报告</p>

      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'CompeteIndex'
}
</script>

<style>
.compete {
  background: url('../../assets/compete_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>