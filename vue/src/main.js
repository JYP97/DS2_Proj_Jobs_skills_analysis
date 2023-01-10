// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import ElementUi from 'element-ui'
import JaysonRpcVue from 'jayson-rpc-vue'
// import * as https from 'https'

Vue.config.productionTip = false
Vue.use(JaysonRpcVue, '127.0.0.1:5672', false)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
