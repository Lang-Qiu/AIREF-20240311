<template>
  <div>
    <div class="database">
      <Banner>
        <h1 slot="title">数据集列表</h1>
        <p slot="text">这里列出了我们提供的内置数据集，涵盖了各种领域和用途。这些数据集已准备好供您使用，并包含详细的描述和下载链接。如果您有自己的数据集，您可以在这里上传和共享它们。我们为您提供一个方便的平台，让您的数据集能够为更多人所用</p>
        <img slot="image" src="../../assets/aigc_r.png" alt="">
      </Banner>
    </div>
    <el-table
      :data="tableData"
      style="width: 760px; margin: 100px auto;"
      >
      <el-table-column
        prop="data_time"
        label="上传时间"
        width="240">
      </el-table-column>
      <el-table-column
        prop="data_type"
        label="类型"
        width="240">
      </el-table-column>
      <el-table-column
        prop="data_pic"
        label="url"
        width="280">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  export default {
    name: 'DataBase',
    data() {
      return {
        // tableData: this.$store.state.fileList
      }
    },
    computed: {
      tableData() {
        return this.$store.state.dataTest
      }
    },
    // mounted() {
    //   console.log(this.tableData);
    // }
  }
</script>

<style>
.database {
  height: 330px;
  background: url('../../assets/ber3.png') no-repeat;
  background-size: 100% 100%;
}
.el-table th {
  text-align: center;
}
.el-table .cell {
  text-align: center;
}
</style>