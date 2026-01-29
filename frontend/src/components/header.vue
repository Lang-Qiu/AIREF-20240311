<template>
  <div class="container_header">
      <div class="contain_head">
        <div class="container_header_left">
          <!-- <img style="height: 48px;" src="https://mdn.alipayobjects.com/huamei_ng7hag/afts/img/A*_sz7Qb8VS18AAAAAAAAAAAAADi-hAQ/original" alt=""> -->
          
        </div>
        <div class="container_header_middle" style="flex: 1 1;">
          <router-link to="/home" class="shouye common_head">首页</router-link>
          <router-link to="/modelassess" class="pinggu common_head" @click.native="sendActiveName" id="first">综合评估</router-link>
          <router-link to="/compete" class="pinggu common_head">对抗攻击测试</router-link>
          <router-link to="/backdoor" class="pinggu common_head">后门检测</router-link>
          <router-link to="/strengthen" class="pinggu common_head">模型加固</router-link>
          <router-link to="/frame" class="pinggu common_head">基础框架安全检测</router-link>         
          <router-link to="/modellist" class="moxing common_head">模型列表</router-link>
          <router-link to="/database" class="shuju common_head">数据集列表</router-link>
          <router-link to="/report" class="pinggu common_head">测评报告</router-link> 
          <router-link to="/show" class="zhanshi common_head">大屏展示</router-link>
        </div>
        <div class="container_header_right">
          <p>帮助中心</p>
          <div><i class="el-icon-user-solid" style="padding: 0 10px;"></i></div>
          <div>用户名称</div>
        </div>
      </div>
      
    </div>
</template>

<script>
export default {
    name: 'HeaderIndex',
    methods: {
        sendActiveName (e) {
            // console.log(e.target.id);
            this.$bus.$emit('changeActiveName', e.target.id)
        }
      }
}
</script>

<style lang="less">
.container_header {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 99;
  width: 100%;
  min-width: 1200px;
  .contain_head {
    display: flex;
    flex-direction: row; 
    align-items: center;
    justify-content: center;
    height: 64px;
    // margin-right: 24px;
    padding: 0 24px;
    font-size: 14px;
    background-color: transparent;
    background: rgb(18, 21, 21); 
    color: rgb(255, 255, 255);
    .container_header_left {
      display: flex;
      flex-direction: row; 
      align-items: center;
      justify-content: center;
      height: 64px;
      margin-right: 24px;
      padding: 0 24px;
      font-size: 14px;
      background-color: transparent;
    }
    .container_header_middle {
      display: flex;
      flex-direction: row; 
      align-items: center;
      justify-content: left;
      height: 64px;
      margin-right: 24px;
      padding: 0 24px;
      font-size: 16px;
      background-color: transparent;
      .common_head{
        padding-right: 20px;
        padding-left: 20px;
        color: #fff;
      }
    }
    .container_header_right {
      display: flex;
      flex-direction: row; 
      align-items: center;
      justify-content: center;
      height: 64px;
      margin-right: 24px;
      padding: 0 24px;
      font-size: 14px;
      background-color: transparent;
    }
    
    
    .logo_text {
      margin-left: 16px;
      color: #fff;
      font-weight: 600;
      font-size: 18px;
      font-family: PingFangSC;
      line-height: 20px;
      letter-spacing: 0;
    }
    .el-tabs__item {
      font-size: 16px;
      color: #fff;
    }
  }
}
</style>