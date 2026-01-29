const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/auth': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/upload': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/getFolderList': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/getFileList': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/getEvalHistory': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/uploadText': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/deleteFile': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/shareFile': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '/unshareFile': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
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
