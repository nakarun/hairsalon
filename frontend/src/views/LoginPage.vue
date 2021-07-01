<template>
  <div id="login-page">
    <main class="container mt-5 p-5">
      <p class="h5 mb-5">Login</p>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
        >
          <v-text-field
            v-model="username"
            :counter="10"
            :rules="usernameRules"
            label="Name"
            required
          ></v-text-field>

          <v-text-field
            v-model="password"
            :rules="passwordRules"
            label="Password"
            required
          ></v-text-field>

          <v-btn
            :disabled="!valid"
            color="primary"
            class="mt-4"
            block
            @click="validate"
          >
            Login
          </v-btn>

        </v-form>
    </main>
  </div>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      username: '',
      usernameRules: [
        v => !!v || 'ユーザー名を入力してください。',
        v => (v && v.length <= 10) || 'ユーザー名は10文字以内です。',
      ],
      password: '',
      passwordRules: [
        v => !!v || 'パスワードを入力してください。',
        v => (v && v.length <= 10) || 'パスワードは10文字以内です。',
      ],
    }),

    methods: {
      validate () {
        if (this.$refs.form.validate()) {
          this.submitLogin()
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
      // ログインボタン押下
      submitLogin: function() {
        // ログイン実行
        this.$store
          .dispatch("auth/login", {
            username: this.username,
            password: this.password
          })
          .then(() => {
            console.log("Login succeeded.");
            this.$store.dispatch("message/setInfoMessage", {
              message: "ログインしました。"
            });
            // クエリ文字列に「next」がなければ、ホーム画面へ
            const next = this.$route.query.next || "/";
            this.$router.replace(next);
          });
      }
    },
  }
</script>

<style scoped>

</style>