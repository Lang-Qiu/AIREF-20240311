<template>
  <div>
    <div class="frame">
      <Banner>
        <h1 slot="title">基础安全框架检测</h1>
        <div slot="text">
          <p>本方案的核心任务是检测您的项目中所使用的人工智能框架第三方库的安全性，确保您的应用程序在安全性方面达到最高标准。</p>
          <h4>主要特点和优势：</h4>
          <p><b>全面的检测：</b></p>
          <span>我们的方案着眼于您项目中使用的第三方库，这些库可能会因版本升级而产生变化。我们的检测不仅关注已知漏洞，还侧重于检测可能存在的潜在问题。</span>
          <p><b>源码静态分析：</b></p>
          <span>我们通过源码静态分析的方法，深入检查待测第三方库，以确定其中是否存在潜在漏洞隐患。这有助于您及时发现潜在问题并采取适当的措施。</span>
          <p><b>综合评估：</b></p>
          <span>我们基于经过版本断代的待测项目所需检测项，对待测方案的安全性进行全面评估。这包括确定漏洞隐患的程度以及待测方对漏洞的补救措施。</span>
          <p><b>庞大漏洞数据集：</b></p>
          <span>我们依托庞大的漏洞数据集，以确保我们的检测方案能够覆盖各种可能性，帮助您降低潜在风险。</span>
        </div>
        
      </Banner>
    </div>
    <el-upload
      class="upload-demo"
      drag
      action="https://jsonplaceholder.typicode.com/posts/"
      multiple
      style="width: 500px;height: 500px;">
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
  </div>
</template>

<script>
export default {
    name: 'FrameIndex'
}
</script>

<style lang="less">
.frame {
  background: url('../../assets/frame_bg.jpg') no-repeat;
  background-size: 100% 100%;
  height: 500px;
  p {
    padding-top: 10px!important;
    font-size: 16px;
  }
  span {
    font-size: 15px;
  }
  h4 {
    padding-top: 10px;
  }
  h1 {
    padding-top: 40px!important;
  }
  img {
    margin: 115px auto!important;
  }
}
.upload-demo {
  margin: 0 auto;
}
.el-upload-dragger {
  margin-top: 100px;
  width: 500px!important;
  height: 300px;
  .el-icon-upload {
    font-size: 150px;
    margin: 100px 0 16px;
  }
  .el-upload__text {
    margin-top: 20px;
  }
}

</style>