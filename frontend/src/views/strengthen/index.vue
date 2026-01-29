<template>
  <div>
    <div class="strengthen">
      <Banner>
        <h1 slot="title">模型安全加固</h1>
        <p slot="text">模型安全加固旨在提高机器学习和人工智能模型的安全性、鲁棒性和可信度，保护模型免受恶意攻击和滥用，确保其在现实世界中的应用是可行的、安全的和可信的。这有助于维护用户隐私、防止不当使用，提高模型的可信度</p>

      </Banner>
    </div>
    <router-view></router-view>
    </div>
</template>

<script>
export default {
  name: 'StrengthenIndex'
}
</script>

<style>
.strengthen {
  background: url('../../assets/strengthen_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>