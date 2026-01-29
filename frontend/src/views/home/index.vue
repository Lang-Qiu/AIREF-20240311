<template>
  <div>
    <div class="home">
      <Banner>
        <h1 slot="title">产品介绍</h1>
        <p slot="text">针对人工智能模型和系统的“守护者”，通过集成现有的针对人工智能系统的攻击和防御技术，提供模型安全性评估以及模型安全性提升加固端到端全方位解决方案。目前该平台支持的数据集类型有文本，图像，语音，图谱，可以实现后门攻击和对抗样本攻击的检测和防御，提供被测的AI模型的安全风险评估报告</p>
        <div slot="btn" class="lianxi_btn">立即评估</div>
        <img slot="image" src="../../assets/rightimg.png" alt="">
      </Banner>
    </div>
    <KuangJia></KuangJia>
    <GongNeng></GongNeng>
    <YouShi></YouShi>
  </div>
</template>

<script>
import KuangJia from '@/components/kuangjia.vue'
import GongNeng from '@/components/gongneng.vue'
import YouShi from '@/components/youshi.vue'
export default {
  name: 'HomeIndex',
  components: {
      KuangJia,
      GongNeng,
      YouShi,
    },
    
}
</script>

<style lang="less" scoped>
.home {
  height: 400px;
  background: url('../../assets/aigc_bg.png') no-repeat;
  background-size: 100% 100%;
}
.lianxi_btn {
  width: 100px;
  height: 40px;
  border: 1px solid #222;
  border-radius: 20px;
  color: #222;
  text-align: center;
  line-height: 40px;
  margin-top: 30px;
}
</style>