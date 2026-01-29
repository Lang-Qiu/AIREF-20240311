<template>
  <div class="main">
    <div class="modellist">
      <Banner>
        <h1 slot="title">模型列表</h1>
        <p slot="text">这里列出了各种机器学习和深度学习模型，可以用于各种任务，包括图像分类、自然语言处理、推荐系统等。这些模型包含详细的描述和代码示例，方便您快速应用。如果您开发了自己的模型，您可以在这里上传和分享它们。我们为您提供一个平台，以便更多人能够受益于您的工作</p>
        <img slot="image" src="../../assets/gnzs21.png" alt="" >
      </Banner>
    </div>
    <el-table
      :data="tableData"
      stripe
      style="width: 720px; margin: 100px auto;">
      <el-table-column
        prop="model_type"
        label="类型"
        width="360">
      </el-table-column>
      <el-table-column
        prop="model_pic"
        label="url"
        width="360">
      </el-table-column>
    </el-table>
  </div>
</template>


<script>

export default {
  name: 'ModelList',
  components: {

  },
  data() {
    return {
  
    }
  },
  computed: {
      tableData() {
        return this.$store.state.modelTest
      }
    },
    methods: {
      
    }
}
</script>
<style lang="less">
.modellist {
  background: url('../../assets/bk.png') no-repeat;
  background-size: 100% 100%;
}
.el-table th {
  text-align: center;
}
.el-table .cell {
  text-align: center;
}
</style>