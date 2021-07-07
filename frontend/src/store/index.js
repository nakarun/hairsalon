import Vue from "vue";
import Vuex from "vuex";
import api from "@/services/api";

Vue.use(Vuex);

// 認証情報
const authModule = {
  namespaced: true,
  state: {
    useruuid: "",
    username: "",
    isLoggedIn: false
  },
  mutations: {
    set(state, payload) {
      state.useruuid = payload.user.uuid;
      state.username = payload.user.username;
      state.isLoggedIn = true;
    },
    clear(state) {
      state.useruuid = "";
      state.username = "";
      state.isLoggedIn = false;
    }
  },
  actions: {
    /**
     * ログイン
     */
    login(context, payload) {
      return api
        .post("/auth/jwt/create/", {
          username: payload.username,
          password: payload.password
        })
        .then(response => {
          // 認証用トークンをlocalStorageに保存
          localStorage.setItem("access", response.data.access);
          // ユーザー情報を取得してstoreのユーザー情報を更新
          return context.dispatch("renew");
        });
    },
    /**
     * ログアウト
     */
    logout(context) {
      // 認証用トークンをlocalStorageから削除
      localStorage.removeItem("access");
      // storeのユーザー情報をクリア
      context.commit("clear");
    },
    /**
     * ユーザー情報更新
     */
    renew(context) {
      return api.get("/auth/users/me/").then(response => {
        const user = response.data;
        // storeのユーザー情報を更新
        context.commit("set", { user: user });
      });
    }
  }
};

// グローバルメッセージ
const messageModule = {
  namespaced: true,
  state: {
    error: "",
    warnings: [],
    info: ""
  },
  mutations: {
    set(state, payload) {
      if (payload.error) {
        state.error = payload.error;
      }
      if (payload.warnings) {
        state.warnings = payload.warnings;
      }
      if (payload.info) {
        state.info = payload.info;
      }
    },
    clear(state) {
      state.error = "";
      state.warnings = [];
      state.info = "";
    }
  },
  actions: {
    /**
     * エラーメッセージ表示
     */
    setErrorMessage(context, payload) {
      context.commit("clear");
      context.commit("set", { error: payload.message });
    },
    /**
     * 警告メッセージ（複数）表示
     */
    setWarningMessages(context, payload) {
      context.commit("clear");
      context.commit("set", { warnings: payload.messages });
    },
    /**
     * インフォメーションメッセージ表示
     */
    setInfoMessage(context, payload) {
      context.commit("clear");
      context.commit("set", { info: payload.message });
    },
    /**
     * 全メッセージ削除
     */
    clearMessages(context) {
      context.commit("clear");
    }
  }
};

// salon data
const salonModule = {
  namespaced: true,
  state: {
    uuid: "",
    salonname: "",
  },
  mutations: {
    set(state, payload) {
      state.uuid = payload.salon.uuid;
      state.salonname = payload.salon.name;
    },
    clear(state) {
      state.uuid = "";
      state.salonname = "";
    }
  },
  actions: {
    getSalonData(context, payload) {
      return api
        .get('/salon/', {
          params: {
            staff: payload.staff,
          }
        })
        .then(response => {
          if (typeof response.data === 'object') {
            // store の salon data を更新
            const salon = response.data;
            context.commit("set", { salon: salon });
          }
          else {
            // 今の所想定していない
          }
        })
        .catch(function(error) {
          console.log(error);
        })
    },
  }
};

const pointcardsModule = {
  namespaced: true,
  state: {
    pointcards: [],
  },
  mutations: {
    set(state, payload) {
      state.pointcards = payload.pointcards;
    },
    clear(state) {
      state.pointcards = [];
    }
  },
  actions: {
    getPointcards(context, payload) {
      return api.get('/pointcard/', {
        params: {
          salon: payload.salon,
        }
      })
      .then(response => {
        const pointcards = response.data;
        context.commit("set", { pointcards: pointcards });
      })
    }
  },
};

const store = new Vuex.Store({
  modules: {
    auth: authModule,
    message: messageModule,
    salon: salonModule,
    pointcards: pointcardsModule,
  }
});

export default store;
