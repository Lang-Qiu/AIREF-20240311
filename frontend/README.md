# 目录结构

```
.
├── babel.config.js
├── .env.development			// 配置后端服务器地址
├── jsconfig.json
├── package.json                // npm包管理所需模块及配置信息
├── package-lock.json
├── public
│   ├── favicon.ico				// 图标
│   └── index.html				// 入口html文件（暂时没用到）
├── README.md
├── src
│   ├── api
│   │   └── index.js 			// 统一封装API接口调用方法
│   ├── App.vue					// 根组件
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   ├── Home.vue			// 上传文件、文本
│   │   ├── Login.vue			// 登录界面
│   │   └── Register.vue		// 注册界面
│   ├── icons					// 图标（暂时没用到）
│   │   └── svg
│   ├── main.js					// 程序入口文件
│   ├── router
│   │   └── index.js			// 单页面路由注册组件 
│   └── utils
│       └── encrypt.js 			// 对表单中的密码加密
└── vue.config.js				// webpack配置
```

# 技术栈

 * vue2.6
 * axios
 * webpack

# 前期准备

1. 更新包管理器apt与apt-get：

   ```shell
   $ sudo apt update
   $ sudo apt-get update
   ```

2. 安装nodejs：

   ```shell
   $ sudo apt-get install nodejs
   ```

3. 安装并升级npm：

   ```shell
   $ sudo apt-get install npm
   $ npm config set registry http://registry.npm.taobao.org 	// 设置国内资源镜像
   $ npm install -g npm
   ```

4. 安装cnpm：

   ```shell
   $ npm install -g cnpm 	// 国内的npm不是很好用，使用cnpm代替npm的日常使用
   ```

5. 安装Vue：

   ```shell
   $ cnpm install -g vue
   ```

6. 安装Vue脚手架vue-cli：

   ```shell
   $ cnpm install -g vue-cli
   ```

7. 安装webpack、vue-router、JSEncrypt：

   ```shell
   $ sudo cnpm install -g webpack
   $ npm install vue-router@3.0.6
   $ npm install jsencrypt
   ```

# 下载安装依赖

```shell
$ git clone http://202.120.1.152:8080/haiyang_yu/airef.git
$ cd airef/frontend
$ npm install
```

# 开发模式

```shell
$ npm run serve
```

