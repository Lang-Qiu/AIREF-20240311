<template>
    <div class="register-container" style="margin-left: 500px">
        <h1>Register</h1>
        <!-- <form class="login-form">
            <input type="text" required="required" placeholder="Email" v-model.trim="User.username">
            <br />
            <input type="password" required="required" placeholder="Password" v-model.trim="User.password">
            <br />
            <input type="password" required="required" placeholder="Password" v-model.trim="User.password">
            <button @click="submit">Register</button>
        </form> -->
        <el-form ref="ruleForm" :model="ruleForm" :rules="rules" label-width="80px" autocomplete="off"
            :hide-required-asterisk="true" size="medium">
            <div style="padding-top: 10px">
                <el-form-item label="用户名" prop="username">
                    <el-col :span="10">
                        <el-input v-model="ruleForm.username" placeholder="输入用户名" />
                    </el-col>
                    <!-- <el-button :loading="codeLoading" :disabled="isDisable" size="small" round @click="sendMsg">发送验证码
                    </el-button> -->

                    <!-- <span class="status">{{ statusMsg }}</span> -->
                </el-form-item>
                <!-- <el-form-item label="验证码" prop="code">
                    <el-col :span="10">
                        <el-input v-model="ruleForm.code" maxlength="6" placeholder="请登录邮箱接收验证码" />
                    </el-col>
                </el-form-item> -->
                <el-form-item label="密码" prop="pwd">
                    <el-col :span="10">
                        <el-input v-model="ruleForm.pwd" type="password" />
                    </el-col>
                </el-form-item>
                <el-form-item label="确认密码" prop="cpwd">
                    <el-col :span="10">
                        <el-input v-model="ruleForm.cpwd" type="password" />
                    </el-col>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" style="width: 40%" @click="register">注册</el-button>
                </el-form-item>
            </div>
        </el-form>

    </div>
</template>
<script>
import { encrypt } from '@/utils/encrypt'
import axios from 'axios'
export default {
    name: 'RegisterIndex',
    data() {
        return {
            ruleForm: {
                username: '',
                pwd: '',
                cpwd: ''
            },
            rules: {
                // email: [{
                //     required: true,
                //     type: 'email',
                //     message: '请输入邮箱',
                //     trigger: 'blur'
                // }],
                username: [
                    { required: true, message: "用户名不能为空", trigger: "blur" },
                    { min: 5, max: 14, message: "长度在 5 到 14 个字符", trigger: "blur" }
                ],
                // code: [{
                //   required: true,
                //   type: 'string',
                //   message: '请输入验证码',
                //   trigger: 'blur'
                // }],
                pwd: [{
                    required: true,
                    message: '创建密码',
                    trigger: 'blur'
                }, { pattern: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$/, message: '密码必须同时包含数字与字母,且长度为 8-20位' }],
                cpwd: [{
                    required: true,
                    message: '确认密码',
                    trigger: 'blur'
                }, {
                    validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('请再次输入密码'))
                        } else if (value !== this.ruleForm.pwd) {
                            callback(new Error('两次输入密码不一致'))
                        } else {
                            callback()
                        }
                    },
                    trigger: 'blur'
                }]

            }
        }
    },
    methods: {
        register: function () {
            this.$refs['ruleForm'].validate((valid) => {
                if (valid) {
                    const user = {
                        username: this.ruleForm.username,
                        password: encrypt(this.ruleForm.pwd)
                    }
                    console.log(user)
                    axios({
                        method: 'post',
                        url: this.$api.registerUrl,
                        data: user,
                    }).then(res => {
                        if (res.data.status === true) {
                            console.log(res)
                            this.$message({
                                showClose: true,
                                message: '注册成功，正在跳转到登录界面...',
                                type: 'success'
                            })
                            setTimeout(() => {
                                this.$router.push('/login')
                            }, 2000)
                        }
                        else {
                            console.log(res)
                            this.$message({
                                showClose: true,
                                message: '注册失败，用户名已存在!',
                                type: 'error'
                            })
                        }

                    }).catch(err => {
                        console.log(err.response.data.message)
                    })
                }
            })
        }

    }
}
</script>