<template>
    <el-form style="margin:100px auto;width:40%;min-width:500px;">
        <el-steps :space="600" :active="active" finish-status="success" :align-center="isTrue" style="margin-top: 30px;margin-bottom: 30px;">
            <el-step title="数据测评" icon="el-icon-document-remove"></el-step>
            <el-step title="模型测评" icon="el-icon-s-help"></el-step>
            <el-step title="综合评测" icon="el-icon-cpu"></el-step>
        </el-steps>
        <el-checkbox :indeterminate="isIndeterminate" v-model="checkAll" @change="handleCheckAllChange">全选</el-checkbox>
        <div style="margin: 15px 0;"></div>
        <el-checkbox-group v-model="checkedWays" @change="handleCheckedChange">
        <div class="checkedColumn" style="margin: 20px auto;">
            <el-checkbox v-for="way in ways" :label="way" :key="way">{{way}}</el-checkbox>
        </div>
        </el-checkbox-group>
        
        <router-link to="model" style="color:#606266;">
            <el-button class="nextButton" style="margin-top: 12px;" :round='true'>
                上一步
            </el-button>
        </router-link>
        <el-button style="margin: 20px 10px 20px" :round='true' @click="getTestResult">
            测试
        </el-button>
        <el-button class="nextButton" style="margin-top: 12px;" :round='true' @click="getSubmitResult">提交</el-button>
    </el-form>
</template>

<script>
import { getSubmitResultThree } from '@/api/submit';
import { getTestResultThree } from '@/api/test';

const wayOptions = ['FGM', 'BIM', 'PGD', '随机裁剪', '随机旋转', '失真', '噪声变换']
export default {
    name: 'AttackIndex',
    data() {
        return {
            isTrue: true,
            active: 2,
            checkAll: false,
            checkedWays: [],
            ways: wayOptions,
            isIndeterminate: false,
            status: '',
            submit_pic: '',
            attack_pic: '',
            submit_type: ''
        }
    },
    mounted() {
        if (this.$route.path.includes('image')) {
          this.submit_type = '图像模型'                
        } else if (this.$route.path.includes('audio')) {
          this.submit_type = '音频模型'
        } else if (this.$route.path.includes('knowledge')) {
          this.submit_type = '知识图谱'
        } else if (this.$route.path.includes('reinforce')) {
          this.submit_type = '强化学习'
        } else if (this.$route.path.includes('tab')) {
          this.submit_type = '表格模型'
        } else if (this.$route.path.includes('text')) {
          this.submit_type = '文本模型'
        } else if (this.$route.path.includes('visual')) {
          this.submit_type = '视频模型'
        } else if (this.$route.path.includes('compete')) {
          this.submit_type = '对抗攻击'
        } else if (this.$route.path.includes('backdoor')) {
          this.submit_type = '后门检测'
        } else if (this.$route.path.includes('strengthen')) {
          this.submit_type = '模型加固'
        }
    },
    methods: {
        async getTestResult() {
            let attack_list = this.checkedWays
            this.$store.commit('addReport', attack_list)
            let reportData = { ...this.$store.state.modelList, ...this.$store.state.fileList, attack_list}
            console.log(reportData);
            // getTestResultThree()
            const { data } = await getTestResultThree(reportData)
            console.log(data);
            this.status = data.status
            this.attack_pic = data.attack_pic
            let time = new Date().toLocaleString()
            let attackTestList = {
                attack_pic: this.attack_pic,
                attack_time: time,
            }
            this.$store.commit('addAttackTest', attackTestList)
            this.$message.info({
            content: '测试成功',
            duration: 3000,
            closeBtn: true,
            theme: 'success'
            });
        },
        async getSubmitResult() {
            let attack_list = this.checkedWays
            this.$store.commit('addReport', attack_list)
            let reportData = { ...this.$store.state.modelList, ...this.$store.state.fileList, attack_list}
            console.log(reportData);
            // getSubmitResultThree()
            const { data } = await getSubmitResultThree(reportData)
            this.status = data.status
            if(this.status==200) {
                this.submit_status = '队列中'
            } else {
                this.submit_type = '排队中'
            }
            this.submit_pic = data.submit_pic
            let time = new Date().toLocaleString()
            let attackSubmitList = {
                submit_pic: this.submit_pic,
                submit_time: time,
                submit_type: this.submit_type,
                submit_status: this.submit_status
            }
            this.$store.commit('addSubmit', attackSubmitList)
            this.$message.info({
            content: '提交成功',
            duration: 3000,
            closeBtn: true,
            theme: 'success'
            });
        },
        handleCheckAllChange(val) {
            this.checkedWays = val ? wayOptions : [];
            this.isIndeterminate = false;
        },
        handleCheckedChange(value) {
            let checkedCount = value.length;
            this.checkAll = checkedCount === this.ways.length;
            this.isIndeterminate = checkedCount > 0 && checkedCount < this.ways.length;
        },
        
    }
}
</script>

<style lang="less" scoped>

    .checkedColumn {
      width: 50px;
      display: flex;
      flex-direction: column!important;
      justify-content: center;
      align-items: flex-start;
      margin: 0 auto;
      /deep/ .el-checkbox__label {
        align-self: flex-start;
      }
    }

</style>