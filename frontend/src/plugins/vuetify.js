import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import ja from 'vuetify/es5/locale/ja.js'

Vue.use(Vuetify)

const opts = {
    lang: {
        locales: {ja},
        current: 'ja'
    }
}

export default new Vuetify(opts)