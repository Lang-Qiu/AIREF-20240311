
import Vue from 'vue'
import Vuex from 'vuex'
// vuex持久化存储插件
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    fileList: {},
    modelList: {},
    reportList: {},
    dataTest: [],
    modelTest: [],
    attackTest: [],
    submitList: [],
  },
  getters: {
    
  },
  mutations: {
    updateToken (state, newToken) {
      state.token = newToken
    },
    addFile(state, value) {
      state.fileList = value
    },
    addModel(state, value) {
      state.modelList = value
    },
    addReport(state, value) {
      state.reportList = value
      // state.reportList.push(value)
    },
    addSubmit(state, value) {
      // state.reportList = value
      state.submitList.push(value)
    },
    addDataTest(state, value) {
      state.dataTest.push(value)
      // console.log(state.dataTest);
    },
    addModelTest(state, value) {
      state.modelTest.push(value)
    },
    addAttackTest(state, value) {
      state.attackTest.push(value)
    },
  },
  actions: {
  },
  modules: {

  },
  plugins: [
    createPersistedState()
  ]
})