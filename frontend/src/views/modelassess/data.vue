<template>
  <div class="content">
      <div class="main">
        
        
        <el-form ref="form" :model="form" :rules="rules" style="margin:20px auto;width:40%;min-width:500px;" label-width="100px">
          <el-steps :space="600" :active="active" finish-status="success" align-center>
            <el-step title="数据测评" icon="el-icon-document-remove"></el-step>
            <el-step title="模型测评" icon="el-icon-s-help"></el-step>
            <el-step title="综合评测" icon="el-icon-cpu"></el-step>
          </el-steps>
          <el-form-item label="data_url:" prop="data_url">   
            <el-input v-model="form.data_url"></el-input>  
          </el-form-item>
          <el-form-item label="data_token:" prop="data_token">   
            <el-input v-model="form.data_token" trim></el-input>  
          </el-form-item>
          
        </el-form>
          <el-button style="margin: 20px" :round='true' @click="getTestResult">
              测试
          </el-button>
          <el-button style="margin-top: 20px;" :round='true' @click="nextHandler">
            下一步
          </el-button>
      </div>
    </div>
</template>

<script>
import { getTestResultOne } from '@/api/test';

// import axios from 'axios'
export default {
  name: 'UploadData',
  data() {
    return {
      form: {
        data_url: '',
        data_token: '',
        data_type: ''
      },
      fileList: [],
      active: 0,
      status: '',
      data_pic: '',
      rules: {
          data_token: [
            { required: true, message: '请输入token', trigger: 'blur' },
            { pattern: /^[a-zA-Z0-9]+$/, message: '请输入正确的token', trigger: 'blur'}
          ],
          data_url: [
            { required: true, message: '请输入url', trigger: 'blur' },
            { pattern: /^((https|http|ftp|rtsp|mms)?:\/\/)(([A-Za-z0-9]+-[A-Za-z0-9]+|[A-Za-z0-9]+)\.)+([A-Za-z]{2,6})(:\d+)?(\/.*)?(\?.*)?(#.*)?$/, message: '请输入正确的url地址', trigger: 'blur'}
          ],
      }
    }
  },
  
  methods: {
    async getTestResult() {
      if (this.$route.path.includes('image')) {
          this.form.data_type = '图像模型'                
        } else if (this.$route.path.includes('audio')) {
          this.form.data_type = '音频模型'
        } else if (this.$route.path.includes('knowledge')) {
          this.form.data_type = '知识图谱'
        } else if (this.$route.path.includes('reinforce')) {
          this.form.data_type = '强化学习'
        } else if (this.$route.path.includes('tab')) {
          this.form.data_type = '表格模型'
        } else if (this.$route.path.includes('text')) {
          this.form.data_type = '文本模型'
        } else if (this.$route.path.includes('visual')) {
          this.form.data_type = '视频模型'
        } else if (this.$route.path.includes('compete')) {
          this.form.data_type = '对抗攻击'
        } else if (this.$route.path.includes('backdoor')) {
          this.form.data_type = '后门检测'
        } else if (this.$route.path.includes('strengthen')) {
          this.form.data_type = '模型加固'
        }   
      this.$store.commit('addFile', this.form)
      // 获取store中的文件列表
      let Data = { ...this.$store.state.fileList }
      console.log(Data);
      // 获取测试结果
      // const { data_pic, status } = await getTestResultOne(Data)
      // 获取测试结果
      const { data } = await getTestResultOne(Data)
      // 设置状态
      this.status = data.status
      // 设置图片
      this.data_pic = data.data_pic
      let time = new Date().toLocaleString()
      let dataTestList = {
        data_type: this.form.data_type,
        data_pic: this.data_pic,
        data_time: time,
      }
      this.$store.commit('addDataTest', dataTestList)
      console.log(data, this);
      // 弹出提示框
      this.$message.info({
          content: '测试成功',
          duration: 3000,
          closeBtn: true,
          theme: 'success'
        });
      
      
    },
    nextHandler () {
      if (this.status == 200) {
        this.$router.push('model')
      }
    },
    
  }
}

</script>

<style lang="less" scoped>
.content {
  margin-top: 84px;
  padding: 0 100px 20px;
  .main {
    // display: block;
    // margin: 0 auto;
    text-align: center;
    .el-steps {
      margin: 50px 0;
    }
  }
}
</style>