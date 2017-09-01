// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import api_ from '@/api';

Vue.config.productionTip = false
Vue.prototype.api = api_;
Vue.prototype.axios = axios;
Vue.use(ElementUI);

// axios hook
// axios.interceptors.request.use(function (config) {
//     config.headers.token = localStorage.token;
//     return config;
//   }, function (err) {
//     return Promise.reject(err);
//   });
//   axios.interceptors.response.use(function (response) {
//     return response;
//   }, function (error) {
//     if (error.response.status === 401) {
//       store.commit('un_auth');
//       setTimeout(window.location.href = '/#/account/login', 1500)
//     }
  
//     return Promise.reject(error);
//   });

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

