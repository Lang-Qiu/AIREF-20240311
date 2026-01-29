<template>
  <div class="content">
      <div class="main">
        
        
        <el-form ref="form" :model="form" :rules="rules" style="margin:20px auto;width:40%;min-width:500px;" label-width="110px">
          <el-steps :space="600" :active="active" finish-status="success" align-center>
            <el-step title="数据测评" icon="el-icon-document-remove"></el-step>
            <el-step title="模型测评" icon="el-icon-s-help"></el-step>
            <el-step title="综合评测" icon="el-icon-cpu"></el-step>
          </el-steps>
          <el-form-item label="model_url:" prop="model_url">   
            <el-input v-model="form.model_url" ></el-input>  
          </el-form-item>
          <el-form-item label="model_token:" prop="model_token">   
            <el-input v-model="form.model_token" ></el-input>  
          </el-form-item>
        </el-form>
        <router-link to="data" style="color:#606266;">
          <el-button class="nextButton" style="margin-top: 12px;" :round='true'>
            上一步
          </el-button>
        </router-link>
        <el-button style="margin: 20px 10px 20px" :round='true' @click="getTestResult">
            测试
        </el-button>
        
          <el-button class="nextButton" style="margin-top: 20px;" :round='true' @click="nextHandler">
            下一步
          </el-button>
      </div>
    </div>
</template>

<script>
import { getTestResultTwo } from '@/api/test';

// import axios from 'axios'
export default {  
  name: 'ModelAssess',
  data() {
    return {
      form: {
        model_url: '',
        model_token: '',
        model_type: ''
      },
      active: 1,
      status: '',
      model_pic: '',
      rules: {
          model_token: [
            { required: true, message: '请输入token', trigger: 'blur' },
            { pattern: /^[a-zA-Z0-9]+$/, message: '请输入正确的token', trigger: 'blur'}
          ],
          model_url: [
            { required: true, message: '请输入url', trigger: 'blur' },
            { pattern: /^((https|http|ftp|rtsp|mms)?:\/\/)(([A-Za-z0-9]+-[A-Za-z0-9]+|[A-Za-z0-9]+)\.)+([A-Za-z]{2,6})(:\d+)?(\/.*)?(\?.*)?(#.*)?$/, message: '请输入正确的url地址', trigger: 'blur'}
          ],
      }
    }
  },
  
  // computed: {
  //   // 这里定义上传文件时携带的参数，即表单数据
  //   modelList() {
  //       return this.$store.state.modelList
  //     }
  // },
  methods: {
    
    async getTestResult() {
      if (this.$route.path.includes('image')) {
          this.form.model_type = '图像模型'                
        } else if (this.$route.path.includes('audio')) {
          this.form.model_type = '音频模型'
        } else if (this.$route.path.includes('knowledge')) {
          this.form.model_type = '知识图谱'
        } else if (this.$route.path.includes('reinforce')) {
          this.form.model_type = '强化学习'
        } else if (this.$route.path.includes('tab')) {
          this.form.model_type = '表格模型'
        } else if (this.$route.path.includes('text')) {
          this.form.model_type = '文本模型'
        } else if (this.$route.path.includes('visual')) {
          this.form.model_type = '视频模型'
        } else if (this.$route.path.includes('compete')) {
          this.form.model_type = '对抗攻击'
        } else if (this.$route.path.includes('backdoor')) {
          this.form.model_type = '后门检测'
        } else if (this.$route.path.includes('strengthen')) {
          this.form.model_type = '模型加固'
        }      
      this.$store.commit('addModel', this.form)
      let modelData = { ...this.$store.state.modelList, ...this.$store.state.fileList}
      console.log(modelData);
      const { data } = await getTestResultTwo(modelData)
      this.status = data.status
      this.model_pic = data.model_pic
      let time = new Date().toLocaleString()
      let modelTestList = {
        model_type: this.form.model_type,
        model_pic: this.model_pic,
        model_time: time,
        }
      this.$store.commit('addModelTest', modelTestList)
      this.$message.info({
          content: '测试成功',
          duration: 3000,
          closeBtn: true,
          theme: 'success'
        });
    },
    nextHandler () {
      if (this.status === 200) {
        this.$router.push('attack')
      }
    }
    //表单提交
    // submitUpload() {
    //   //触发组件的action
    //   // this.$refs.upload.submit();
    //   // console.log(form);
    //   // console.log(this.$refs.upload);
      
    // },
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