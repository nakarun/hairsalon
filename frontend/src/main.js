import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// Vuetify
import vuetify from '@/plugins/vuetify';
// BootstrapVue
import bootstrap from '@/plugins/bootstrap-vue';

Vue.config.productionTip = false;

new Vue({
  bootstrap,
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
