<template>
  <div>

    
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="综合评估" name="first">
        <router-view></router-view>
      </el-tab-pane>
      <el-tab-pane label="图像模型评估" name="second">
        <router-view></router-view>
      </el-tab-pane>
      <el-tab-pane label="文本模型评估" name="third">   
        <router-view></router-view>
      </el-tab-pane>
      <el-tab-pane label="音频模型评估" name="fourth">
        
        <router-view></router-view>
      </el-tab-pane>
      <el-tab-pane label="视频模型评估" name="fifth">
        
        <router-view></router-view>
      </el-tab-pane>
      <el-tab-pane label="表格模型评估" name="sixth">
        
        <router-view></router-view>
      </el-tab-pane>
      <el-tab-pane label="知识图谱评估" name="seventh">
        
        <router-view></router-view>
      </el-tab-pane>
      <el-tab-pane label="强化学习评估" name="eight">
        
        <router-view></router-view>
      </el-tab-pane>
    </el-tabs>
    
  </div>
</template>

<script>

export default {
    name: 'ModelAssess',
    components: {

    },
    data() {
      return {
        activeName: 'first'
      };
    },
    mounted () {
      this.$bus.$on('changeActiveName', (aname) => {
        this.activeName = aname
        // console.log(aname);
        if (this.$route.path.includes('image')) {
                this.$bus.$emit('changeActiveName', 'second')
            } else if (this.$route.path.includes('audio')) {
                this.$bus.$emit('changeActiveName', 'third')
            } else if (this.$route.path.includes('knowledge')) {
                this.$bus.$emit('changeActiveName', 'fourth')
            } else if (this.$route.path.includes('reinforce')) {
                this.$bus.$emit('changeActiveName', 'fifth')
            } else if (this.$route.path.includes('tab')) {
                this.$bus.$emit('changeActiveName', 'sixth')
            } else if (this.$route.path.includes('text')) {
                this.$bus.$emit('changeActiveName', 'seventh')
            } else if (this.$route.path.includes('visual')) {
                this.$bus.$emit('changeActiveName', 'eight')
            }
      })
    },
    methods: {
      handleClick(tab) {
        if (tab.index === '0') {
          this.$router.push('/modelassess/sketch')
        } else if (tab.index === '1') {
          this.$router.push('/modelassess/image/data')
        } else if (tab.index === '2') {
          this.$router.push('/modelassess/text/data')
        } else if (tab.index === '3') {
          this.$router.push('/modelassess/audio/data')
        } else if (tab.index === '4') {
          this.$router.push('/modelassess/visual/data')
        } else if (tab.index === '5') {
          this.$router.push('/modelassess/tab/data')
        } else if (tab.index === '6') {
          this.$router.push('/modelassess/knowledge/data')
        } else if (tab.index === '7') {
          this.$router.push('/modelassess/reinforce/data')
        }
      }
    },
    
}
</script>

<style>
.el-tabs__nav-wrap {
  margin: 20px 0 50px 20px;
}
</style>