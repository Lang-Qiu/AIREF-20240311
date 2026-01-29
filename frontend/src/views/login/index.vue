<template>
    <div class="login-container" style="margin-left: 500px">
        <!-- <form class="login-form">
            <input type="text" required="required" placeholder="Username" v-model.trim="User.username">
            <br />
            <input :type="passwordType" required="required" placeholder="Password" v-model.trim="User.password">
            <br />
            <button @click="submit">Login</button>
        </form> -->
        <div class="title-container">
            <h1 class="title">Login</h1>
        </div>
        <div style="padding-top: 10px">
            <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-width="80px" class="login-form"
                auto-complete="on">
                <!-- label-width="500px"> -->
                <el-form-item prop="userName" label="用户名">
                    <el-col :span="10">
                        <el-input ref="userName" v-model="loginForm.userName" placeholder="用户名" name="userName"
                            type="text" tabindex="1" auto-complete="on" />
                    </el-col>
                </el-form-item>

                <el-form-item prop="password" label="密码">
                    <el-col :span="10">
                        <el-input :key="passwordType" ref="password" v-model="loginForm.password" :type="passwordType"
                            placeholder="密码" name="password" tabindex="2" auto-complete="on"
                            @keyup.enter.native="login" />
                    </el-col>
                </el-form-item>
                <el-form-item>
                    <el-button :loading="loading" type="primary" style="width:40%;" @click.native.prevent="login">登录
                    </el-button>
                </el-form-item>
                <el-form-item>
                    <router-link to="/register">还没有帐号？立即注册</router-link>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>
<script>
import { encrypt } from '@/utils/encrypt'
import axios from 'axios'

export default {
    name: 'LoginIndex',
    // data() {
    //     return {
    //         User: {
    //             username: "jackchen",
    //             password: "abc123456"
    //         },
    //         passwordType: "password"
    //     }
    // },
    data() {
        return {
            loginForm: {
                username: "jackchen",
                password: "abc123456"
            },
            loginRules: {
                // userName: [{
                //     type: 'email',
                //     required: true,
                //     trigger: 'blur',
                //     // message: '请输入邮箱' 
                // }],
                userName: [
                    { required: true, message: "用户名不能为空", trigger: "blur" },
                    { min: 5, max: 14, message: "长度在 5 到 14 个字符", trigger: "blur" }
                ],
                password: [{
                    required: true,
                    // message: '创建密码',
                    trigger: 'blur'
                }, {
                    pattern: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$/, message: '密码必须同时包含数字与字母,且长度为 8-20位'
                }]
            },
            loading: false,
            passwordType: 'password',
            redirect: undefined
        }
    },
    methods: {
        login: function () {
            this.$refs['loginForm'].validate((valid) => {
                if (valid) {
                    const user = {
                        username: this.loginForm.userName,
                        password: encrypt(this.loginForm.password)
                    }
                    console.log(user.password)
                    console.log('***')
                    axios({
                        method: 'post',
                        url: this.$api.loginUrl,
                        data: user,
                    }).then(res => {
                        if (res.data.status === 200) {
                            console.log(res)
                            sessionStorage.setItem("username", user.username)
                            this.$message({
                                showClose: true,
                                message: '登录成功!',
                                type: 'success'
                            })
                            setTimeout(() => {
                                this.$router.push('/home')
                            }, 2000)
                        }
                        else {
                            console.log(res)
                            this.$message({
                                showClose: true,
                                message: '登录失败!',
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