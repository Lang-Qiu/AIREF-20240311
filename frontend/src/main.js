import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'  //引入vue-router
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from '@/router'
import store from './store'
import api from '@/api/index'
import dataV from '@jiaminghi/data-view'
import '@/style/common.css'
import iView from 'iview'
import Banner from '@/components/banner'
import TDesign from 'tdesign-vue';

// 引入组件库的少量全局样式变量
import 'tdesign-vue/es/style/index.css';

import Message from 'element-ui';
// 挂载到 Vue 全局对象
Vue.prototype.message = Message.message;


Vue.prototype.$api = api
Vue.config.productionTip = false

Vue.component('Banner', Banner)


Vue.use(dataV)
Vue.use(Router)  
Vue.use(ElementUI)
Vue.use(iView)
Vue.use(TDesign)
new Vue({
  router,
  store,
  render: h => h(App),
  beforeCreate() {
    Vue.prototype.$bus = this
  }
}).$mount('#app')
