import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import ja from 'vuetify/es5/locale/ja.js';
import '@mdi/font/css/materialdesignicons.css';

Vue.use(Vuetify);

const opts = {
    lang: {
        locales: {ja},
        current: 'ja'
    },
    icons: {
      iconfont: 'mdi', // 追加
    },
};

export default new Vuetify(opts);