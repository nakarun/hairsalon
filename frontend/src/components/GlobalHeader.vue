<template>
  <!-- ヘッダナビゲーション -->
  <div id="header">
    <v-app-bar
        color="primary"
        prominent
        dark
    >
      <v-app-bar-nav-icon dark></v-app-bar-nav-icon>
      <v-toolbar-title>Salon Admin</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" icon>
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-title>
              {{ username }}
            </v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title
              @click="clickLogout"
            >
              ログアウト
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  computed: {
    username: function() {
      return this.$store.state.auth.username;
    },
    isLoggedIn: function() {
      return this.$store.state.auth.isLoggedIn;
    }
  },
  methods: {
    // ログアウトリンク押下
    clickLogout: function() {
      this.$store.dispatch("auth/logout");
      this.$store.dispatch("message/setInfoMessage", {
        message: "ログアウトしました。"
      });
      this.$router.replace("/login");
    },
    // ログインリンク押下
    clickLogin: function() {
      this.$store.dispatch("message/clearMessages");
      this.$router.replace("/login");
    }
  }
};
</script>
