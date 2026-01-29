<template>
  <div>
    <div class="reinforce">
      <Banner>
        <h1 slot="title">强化学习评估</h1>
        <p slot="text">强化学习评估是用于测量强化学习代理在不同环境下学习和决策能力的方法。这包括评估代理的策略、奖励函数和学习曲线等。这对于优化强化学习算法和应用于自动控制和决策系统至关重要</p>
        <img slot="image" src="../../../assets/rightimg.png" alt="" style="width: 230px;">
      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'ReinforceLearning'
}
</script>

<style lang="less">
.reinforce {
  background: url('../../../assets/function_bg.png') no-repeat;
  background-size: 100% 100%;
}
</style>