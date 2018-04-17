// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VuePaginate from 'vue-paginate'

import App from './App'
import router from './router'

import './styles/mdb-theme-min.css'
import './styles/style.css'

Vue.config.productionTip = false

Vue.use(VuePaginate)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
  components: { App },
  template: '<App/>'
})
