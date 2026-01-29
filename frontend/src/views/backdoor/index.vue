<template>
  <div>
    <div class="backdoor">
      <Banner>
        <h1 slot="title">后门检测</h1>
        <p slot="text">Ai模型后门攻击是一种新兴的针对深度学习模型的攻击方式，攻击者旨在模型的训练过程中通过某种方式对模型植入后门。当后门未被激发时，被攻击的模型具有和正常模型类似的表现；而当模型中埋藏的后门被攻击者激活时，模型的输出变为攻击者预先指定的标签，以达到恶意的攻击目的。本平台集成了多种目前最新的Ai模型后门检测方法，用户只需界面化操作，便可达到模型后门的检测</p>

      </Banner>
    </div>
    <router-view></router-view>
  </div>
  
</template>

<script>
export default {
    name: 'BackdoorIndex'
}
</script>

<style>
.backdoor {
  background: url('../../assets/backdoor_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>