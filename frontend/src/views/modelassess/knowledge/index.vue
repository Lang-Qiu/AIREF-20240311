<template>
  <div>
    <div class="knowledge">
      <Banner>
        <h1 slot="title">知识图谱评估</h1>
        <p slot="text">知识图谱评估涉及到知识图谱中实体关系、三元组的准确性、一致性和完整性等方面的评估。这对于知识图谱的质量和可用性至关重要，因为它们用于知识图谱搜索、自然语言理解和智能推荐等领域</p>

      </Banner>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
    name: 'MappingKnowledgeDomain'
}
</script>

<style>
.knowledge {
  background: url('../../../assets/knowledge_bg.jpg') no-repeat;
  background-size: 100% 100%;
}
</style>