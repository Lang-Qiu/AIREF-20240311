const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      '/m1/3648993-0-default/test': {
        target: 'http://127.0.0.1:4523',
        // pathRewrite: { '^/test': '' },
      },
      '/m1/3648993-0-default/title': {
        target: 'http://127.0.0.1:4523',
        // pathRewrite: { '^/test': '' },
      }
    } 
  }
})
